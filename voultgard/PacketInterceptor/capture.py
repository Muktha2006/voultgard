from scapy.all import sniff

# Function to display packet information
def packet_callback(packet):
    print(packet.summary())

print("Capturing 10 packets...")

sniff(count=10, prn=packet_callback)

print("Capture completed.")
