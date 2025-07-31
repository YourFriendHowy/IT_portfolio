import socket as skt

hostname = skt.gethostname()
local_IP = skt.gethostbyname(hostname)
portInput = []
portList = []
trgtIP =""
print(local_IP)


def main(): # collect IP and parse port list.
    trgtIP = input("Input target IP: ")
    trgtPorts = input("Input target port(s): ")
    portInput = trgtPorts.split(",")
    p = parse_ports(portInput)
    print(f"Target IP: {trgtIP}")
    print(f"Ports to scan: {p}")
    scanner(trgtIP,p)

def parse_ports(portInput):
    portList = []
    for i in portInput:
        if "-" in i:
            start,end = i.split("-")
            portList.extend(range(int(start), int(end)+1))
        else:
            portList.append(int(i))

    return portList

def scanner(trgtIP, p):
    for i in p:
        try:
            s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((trgtIP, i))
            if result == 0:
                print(f"Port {i} is OPEN")
            else:
                print(f"Port {i} is CLOSED or FILTERED")
            s.close()
        except Exception as e:
            print(f"Error scanning port {i}: {e}")



main()