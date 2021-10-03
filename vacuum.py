import socket
import sys
import binascii

# https://github.com/OpenMiHome/mihome-binary-protocol/pull/8/files

if len(sys.argv) == 2:
    # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
    ip = sys.argv[1]
    port = 54321
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102>")
    exit(1)

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("Do Ctrl+c to exit the program !!")

# Let's send data through UDP protocol
hello = "21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
payload = bytearray.fromhex(hello)
s.sendto(payload, (ip, port))
print("\n Hello packet sent ...\n")
data, address = s.recvfrom(4096)
#print("\nResponse : ", data.decode('utf-8'), "\n")

print ("\nData: ", binascii.hexlify(bytearray(data)), "\n")
# close the socket
s.close()
