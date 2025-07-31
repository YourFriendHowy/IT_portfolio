import socket as skt
import argparse
import sys
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--local", action="store_true", help="Print local IP and exit")

parser.add_argument("ip", nargs="?", help="Target IP address")
parser.add_argument("ports", nargs="?", help="Comma-separated list of ports or ranges")

args = parser.parse_args()



# Used to pull local IP, simple reminded protocol while I work on memorizing it
if args.local:
    hostname = skt.gethostname()
    local_IP = skt.gethostbyname(hostname)
    print("Local IP: " + local_IP)
    sys.exit()

if not args.ip or not args.ports:
    parser.error("IP and ports are required unless using -i")

portInput = []
portList = []
trgtIP =""



def main(): # collect IP and ports, then parse ports into list.
    trgtIP = args.ip
    trgtPorts = args.ports
    portInput = trgtPorts.split(",") # splits port list at commas
    p = parse_ports(portInput) # runs portas through parse_ports function
    #print(f"Target IP: {trgtIP}")
    #print(f"Ports to scan: {p}")
    scanner(trgtIP,p)

def parse_ports(portInput): # Takes port list from main and parses further, splitting ranges into full lists.
    portList = []
    for i in portInput:
        if "-" in i:# checks for a hyphen in current position in list
            start,end = i.split("-") # splits at hyphen saving the start and end numbers 
            portList.extend(range(int(start), int(end)+1)) # used stand and end to determine a range and extend into a full list
        else:
            portList.append(int(i)) # appends numbers w/o hyphens present

    return portList # returns list

def scanner(trgtIP, p):
    notEQ = 0
    count = 0
    for i in p:
        count += 1
        try:
            s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((trgtIP, i))
            if result != 0:
                notEQ += 1 #fix iterator
            else:
                print(f"\nPort {i} is OPEN")
            s.close()
        except Exception as e:
            print(f"Error scanning port {i}: {e}")
    print(notEQ, "of", count, "ports are CLOSED or FILTERED")


main()