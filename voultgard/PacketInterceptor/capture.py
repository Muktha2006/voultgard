from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        print("=" * 50)
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)

        if TCP in packet:
            print("Protocol       : TCP")
            print("Source Port    :", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif UDP in packet:
            print("Protocol       : UDP")
            print("Source Port    :", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

print("Capturing 10 packets...")
sniff(count=10, prn=packet_callback)
print("Capture completed.")
