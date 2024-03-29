import argparse
from scapy.all import sniff, wrpcap, Ether
# I used chatgpt to help a bit with the specifying type of file

def packet_handler(packet):
    """
    Customizes the handling of packets
    :param packet:
    :return:
    """
    print(packet.summary())
    start_sniffing.sniffed_packets.append(packet)  # Append packet to list


def start_sniffing(interface, log_file, packet_type=None):
    """
    Main function to sniff incoming and outgoing network packets
    :param interface:
    :param log_file:
    :param packet_type:
    :return:
    """
    start_sniffing.sniffed_packets = []  # defines sniffed_packets as a list

    # Set the filter based on the specified type
    packet_filter = f"type {packet_type}" if packet_type else ""
    # Use the sniff function to capture packets on the specified interface
    sniff(prn=packet_handler, iface=interface, filter=packet_filter)
    # Optionally, save captured packets to a log file
    if log_file:
        wrpcap(log_file, start_sniffing.sniffed_packets)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Packet Sniffer")
    parser.add_argument("-i", "--interface", help="Network interface to sniff packets from", required=True)
    parser.add_argument("-l", "--log", help="Log file to save captured packets (optional)")
    parser.add_argument("-t", "--type", help="Type of packet to filter (Ether, IP, ARP, etc.)")
    args = parser.parse_args()

    sniffed_packets = []  # Store packets in memory if a log file is specified

    try:
        start_sniffing(args.interface, args.log, args.type)
    except KeyboardInterrupt:
        print("Sniffing stopped by the user.")