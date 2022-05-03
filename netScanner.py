## Created By: Cody Vantienen
## May 2 2022
## Python script to simple ICMP (Internet Control Message Protocol)
# scanner to identify potential targets on the network

# IMPORNTANT _ CHANGE INTERFACE AND IP_RANGE VARIABLES ACCORDINGLY

from scapy.all import *

interface = "eth0"
ip_range = "10.10.X.X/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range) 

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%")) 