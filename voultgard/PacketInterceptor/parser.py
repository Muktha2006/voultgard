from scapy.all import sniff
from scapy.layers.inet import IP, TCP

def parse_modbus(packet):
    if IP in packet and TCP in packet:
        if packet[TCP].sport == 502 or packet[TCP].dport == 502:
            print("=" * 50)
            print("Modbus Packet Detected")
            print("Source IP      :", packet[IP].src)
            print("Destination IP :", packet[IP].dst)
            print("Source Port    :", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

print("Waiting for Modbus packets on port 502...")
sniff(prn=parse_modbus)
