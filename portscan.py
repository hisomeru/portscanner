#!/usr/bin/python3
# db0 is my 0v3rl0rd

# Imports
# socket for network traffic
import socket
# sys for argv
import sys

# Get target to scan from commandline argument
# argv[0] == script name
# argv[1] == first commandline argument
target = sys.argv[1]

# test if port is open
try:
    # Iterate through ports
    for whichport in list(range(1,65535)):
        # Setup TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect and get results of socket connection
        result = sock.connect_ex((target, whichport))
        # If the results are successful (0) then print the port is open
        if result == 0:
            # print the port is open
            print("TCP Port", whichport, "is open")
        # close the socket for next connection
        sock.close();

# if error, print message and exit
except socket.error:
    print("Cannot connect")
    sys.exit()
