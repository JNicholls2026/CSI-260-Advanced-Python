"""DESCRIPTION OF THE MODULE GOES HERE UPDATE THIS WITH YOUR OWN

Author: James Nicholls
Class: CSI-260-01
Assignment: Week 3 Lab

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


class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other_country):
        return self.area > other_country.area

    def population_density(self):
        return self.population / self.area

    def summary(self):
        return f"{self.name} has a population of {self.population} people and is {self.area} square km. " \
          f"It therefore has a population density of {self.population_density:.4f} people per square km."

# Hard Coded Countries
canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040, 9826675)

# Testing the basic functions
print(canada.name)  # Should print 'Canada'
print(canada.population)  # Should print'34482779'
print(canada.area)  # Should print '9984670'

# Testing the self-made functions
print(canada.is_larger(usa))  # Should print 'True'
print(canada.population_density())  # Should print '3.4535'
print(usa.summary())