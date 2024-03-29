import pickle
import csv

"""DESCRIPTION OF THE MODULE GOES HERE

Author: James Nicholls
Class: CSI-260-01
Assignment: Library Project
Due Date: 10/17/2023 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

"""
Contains definitions for the abstract base class LibraryItem as well as CategoryTags
"""


class CategoryTag:
    _all_tags = []

    def __init__(self, name):
        self.name = name
        CategoryTag._all_tags.append(self)

    def __str__(self):
        return self.name

    @classmethod
    def all_category_tags(cls):
        return ", ".join(str(tag) for tag in cls._all_tags)


class LibraryItem:
    """Base class for all items stored in a library catalog

    Provides a simple LibraryItem with only a few attributes

    """

    def __init__(self, name, isbn, tags=None):
        """Initialize a LibraryItem

        :param name: (string) Name of item
        :param isbn: (string) ISBN number for the item
        :param tags: (list) List of CategoryTags
        """
        self.name = name
        self.isbn = isbn
        if tags:
            self.tags = tags
        else:
            self.tags = list()
        self.resource_type = 'Generic'  # This is the type of item being stored

    def match(self, filter_text):
        """True/False whether the item is a match for the filter_text

        match should be case insensitive and should search all attributes of
        the class.  Depending on the attribute, match requires an exact match or
        partial match.

        match needs to be redefined for any subclasses.  Please see the
        note/notebook case study from Chapter 2 as an example of how match
        is designed to work.

        :param filter_text: (string) string to search for
        :return: (boolean) whether the search_term is a match for this item
        """
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() == self.isbn.lower() or \
            filter_text.lower() in (str(tag).lower() for tag in self.tags)

    def __str__(self):
        """Return a well formatted string representation of the item

        All instance variables are included.

        All subclasses must provide a __str__ method
        """
        return f'{self.name}\n{self.isbn}\n{self.type}\n{", ".join(self.tags)}'

    def to_short_string(self):
        """Return a short string representation of the item

        String contains only the name of the item and the ISBN of the item
        I.E.
        Moby Dick - 235253234
        """
        return f'{self.name} - {self.isbn}'


'''
On the following subclasses I used chatgpt for help specifically on syntax since I was a bit off
'''


class Book(LibraryItem):
    """
    SubClass of Library Item that allows you to add a book to the catalog
    """
    def __init__(self, name, isbn, author, publisher, tags=None):
        super().__init__(name, isbn, tags)
        self.resource_type = 'Book'
        self.author = author
        self.publisher = publisher

    def __str__(self):
        return f'{self.name}\n{self.isbn}\n{self.resource_type}\nAuthor: {self.author}\nPublisher: {self.publisher}\n{" ".join(map(str, self.tags))}'


class DVD(LibraryItem):
    """
    SubClass of Library Item that allows you to add a DVD to the catalog
    """
    def __init__(self, name, isbn, director, release_date, tags=None):
        super().__init__(name, isbn, tags)
        self.resource_type = 'DVD'
        self.director = director
        self.release_date = release_date

    def __str__(self):
        return f'{self.name}\n{self.isbn}\n{self.resource_type}\nDirector: {self.director}\nRelease Date: {self.release_date}\n{" ".join(map(str, self.tags))}'


class MusicAlbum(LibraryItem):
    """
    SubClass of Library Item that allows you to add a Music Album to the catalog
    """
    def __init__(self, name, isbn, artist, release_date, tags=None):
        super().__init__(name, isbn, tags)
        self.resource_type = 'Music Album'
        self.artist = artist
        self.release_date = release_date

    def __str__(self):
        return f'{self.name}\n{self.isbn}\n{self.resource_type}\nArtist: {self.artist}\nRelease Date: {self.release_date}\n{" ".join(map(str, self.tags))}'


class Catalog:
    """
    Class that creates the catalog to store information
    """
    def __init__(self, name):
        """
        Initializes Class Catalog
        :param name:
        """
        self.name = name
        self.items = []

    def add_items(self, items):
        """
        Allows you to add items to the catalog
        :param items:
        :return:
        """
        self.items.extend(items)

    def remove_items(self, items):
        """
        Allows you to remove items from the catalog
        :param items:
        :return:
        """
        for item in items:
            if item in self.items:
                self.items.remove(item)

    def search_items(self, filter_text, item_type=None):
        """
        Allows you to search in the catalog
        :param filter_text:
        :param item_type:
        :return:
        """
        results = []
        for item in self.items:
            if item_type is None or item_type == item.resource_type:
                if item.match(filter_text):
                    results.append(item)
        return results

    def print_catalog(self):
        """
        Prints the entire catalog
        :return:
        """
        for item in self.items:
            print(item.to_short_string())

    def save_catalog(self, data):
        with open(data, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_catalog(cls, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def export_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                ['Name', 'ISBN', 'Resource Type', 'Author', 'Publisher', 'Director', 'Release Date', 'Artist', 'Tags'])
            for item in self.items:
                if isinstance(item, Book):
                    writer.writerow([item.name, item.isbn, item.resource_type, item.author, item.publisher, '', '', '',
                                     ', '.join(map(str, item.tags))])
                elif isinstance(item, DVD):
                    writer.writerow(
                        [item.name, item.isbn, item.resource_type, '', '', item.director, item.release_date, '',
                         ', '.join(map(str, item.tags))])
                elif isinstance(item, MusicAlbum):
                    writer.writerow([item.name, item.isbn, item.resource_type, '', '', '', '', item.artist,
                                     ', '.join(map(str, item.tags))])

    def import_from_csv(self, data):
        with open(data, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Resource Type'] == 'Book':
                    new_item = Book(row['Name'], row['ISBN'], row['Author'], row['Publisher'],
                                    [tag.strip() for tag in row['Tags'].split(',')])
                elif row['Resource Type'] == 'DVD':
                    new_item = DVD(row['Name'], row['ISBN'], row['Director'], row['Release Date'],
                                   [tag.strip() for tag in row['Tags'].split(',')])
                elif row['Resource Type'] == 'Music Album':
                    new_item = MusicAlbum(row['Name'], row['ISBN'], row['Artist'], row['Release Date'],
                                          [tag.strip() for tag in row['Tags'].split(',')])
                else:
                    new_item = LibraryItem(row['Name'], row['ISBN'], [tag.strip() for tag in row['Tags'].split(',')])
                self.add_items([new_item])
# Creating the User interface


if __name__ == "__main__":
    catalog = Catalog("Library Catalog")

    while True:
        print("Library Catalog Menu")
        print("1. Search catalog")
        print("2. Print the entire catalog")
        print("3. Add item to catalog")
        print("4. Remove item from catalog")
        print("5. Open catalog from file")
        print("6. Save catalog to file")
        print("7. Export to CSV")
        print("8. Import from CSV")
        print("9. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_text = input("Enter search text: ")
            item_type = input("Enter item type (or press Enter to search all types): ")
            results = catalog.search_items(search_text, item_type)
            if results:
                for item in results:
                    print(item)
            else:
                print("No matching items found.")

        elif choice == "2":
            catalog.print_catalog()

        elif choice == "3":
            item_type = input("Enter item type (e.g., Book, DVD, Music Album): ")
            name = input("Enter item name: ")
            isbn = input("Enter ISBN: ")
            tags = input("Enter tags (comma-separated): ").split(",")
            if item_type == "Book":
                author = input("Enter author: ")
                publisher = input("Enter publisher: ")
                new_item = Book(name, isbn, author, publisher, tags)
            elif item_type == "DVD":
                director = input("Enter director: ")
                release_date = input("Enter release date: ")
                new_item = DVD(name, isbn, director, release_date, tags)
            elif item_type == "Music Album":
                artist = input("Enter artist: ")
                release_date = input("Enter release date: ")
                new_item = MusicAlbum(name, isbn, artist, release_date, tags)
            else:
                new_item = LibraryItem(name, isbn, tags)
            catalog.add_items([new_item])
            print("Item added to the catalog.")

        elif choice == "4":
            remove_isbn = input("Enter ISBN of the item to remove: ")
            items_to_remove = [item for item in catalog.items if item.isbn == remove_isbn]
            if items_to_remove:
                catalog.remove_items(items_to_remove)
                print("Item(s) removed from the catalog.")
            else:
                print("Item not found in the catalog.")
        elif choice == "5":
            filename = input("Enter the filename to open: ")
            try:
                catalog = Catalog.load_catalog(filename)
                print("Catalog loaded from file.")
            except FileNotFoundError:
                print("File not found. Make sure the file exists.")
        elif choice == "6":
            filename = input("Enter the filename to save: ")
            catalog.save_catalog(filename)
            print("Catalog saved to file.")
        elif choice == "7":
            filename = input("Enter the filename to export to CSV: ")
            catalog.export_to_csv(filename)
            print("Catalog exported to CSV.")
        elif choice == "8":
            filename = input("Enter the filename to import from CSV: ")
            catalog.import_from_csv(filename)
            print("Catalog imported from CSV.")
        elif choice == "9":
            break
