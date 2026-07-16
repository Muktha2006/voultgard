from scapy.all import sniff
from scapy.layers.inet import IP, TCP

def parse_packet(packet):
    if IP in packet and TCP in packet:
        print("=" * 50)
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        print("Source Port    :", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)

        if packet[TCP].sport == 502 or packet[TCP].dport == 502:
            print(">>> Modbus TCP Packet Detected <<<")

print("Listening for packets...")
sniff(count=10, prn=parse_packet)

print("Finished.")
