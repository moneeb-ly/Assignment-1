import socket
print("moneb 2191807632")
def hostInfo():
    hostname = socket.gethostname()

    ip_address = socket.gethostbyname(hostname)

    print("Hostname: " + hostname)
    print("IP Address: " + ip_address)

# test the function
hostInfo()