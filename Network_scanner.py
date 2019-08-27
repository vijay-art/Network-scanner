#!usr/bin/env python

import scapy.all as scapy

 



def scanning(ip):
    
    arp_packets = scapy.ARP(pdst=ip)
    broadcast  = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    arp_broadcast_packets = broadcast/arp_packets

    answered_list = scapy.srp(arp_broadcast_packets, timeout=5,verbose =False)[0]

    print("IP\t\t\t\tMAC_address\n-------------------------------------------")

    for element in answered_list:
         print(element[1].psrc)
         print("\t\t\t"+element[1].hwsrc)
         print("-------------------------------------------------------------")
 
ip = input("enter IP to scan network > ")
     
scanning(ip)

