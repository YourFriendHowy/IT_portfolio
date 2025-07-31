---
obsidianUIMode: preview
Language:
  - Python 3
Category: Programming
Topic:
  - Scanner
Type: working Code
System: Linux
Element type:
  - Code Block
Arguments: Y
Source:
  - Matthew Howard(Myself)
Complexity: Intermediate
Keywords: 
aliases: 
DateCreated: 2025-07-30
LastEdited: 2025-07-30
---
# Updates
- Added argparse features for CLI interaction
- 

```python
import socket as skt
import argparse
import sys
parser = argparse.ArgumentParser()

# Positionals
parser.add_argument("ip", nargs="?", help="Target IP address")
parser.add_argument("ports", nargs="?", help="Comma-separated list of ports or ranges")

#Flags
parser.add_argument("-i", "--local", action="store_true", help="Print local IP and exit")
parser.add_argument("-l", "--long", action="store_true", help="Show closed ports too")
parser.add_argument("-v", "--verbose", action="store_true", help="Show banner info for open ports")

args = parser.parse_args()



# -i displays local IP
if args.local:
    hostname = skt.gethostname()
    local_IP = skt.gethostbyname(hostname)
    print("Local IP: " + local_IP)
    sys.exit()

if not args.ip or not args.ports:
    parser.error("IP and ports are required unless using -i")


# variables
portList = []



def main(): # collect IP and ports, then parse ports into list.
    trgtIP = args.ip
    trgtPorts = args.ports
    portInput = trgtPorts.split(",") # splits port list at commas
    p = parse_ports(portInput) # runs portas through parse_ports function
    #print(f"Target IP: {trgtIP}")
    #print(f"Ports to scan: {p}")
    scanner(trgtIP, p, long=args.long, verbose=args.verbose)


def parse_ports(portInput): # Takes port list from main and parses further, splitting ranges into full lists.
    portList = []
    for i in portInput:
        if "-" in i:# checks for a hyphen in current position in list
            start,end = i.split("-") # splits at hyphen saving the start and end numbers 
            portList.extend(range(int(start), int(end)+1)) # used stand and end to determine a range and extend into a full list
        else:
            portList.append(int(i)) # appends numbers w/o hyphens present

    return portList # returns list

def scanner(trgtIP, p, long=False, verbose=False):
    closed = 0
    total = 0

    for port in p:
        total += 1
        try:
            with skt.socket(skt.AF_INET, skt.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((trgtIP, port))
                if result == 0:
                    print(f"Port {port} is OPEN")
                    if verbose:
                        try:
                            s.send(b"HEAD / HTTP/1.1\r\n\r\n")
                            banner = s.recv(1024)
                            print(f"  Banner: {banner.decode(errors='ignore').strip()}")
                        except:
                            print("  No banner received.")
                elif long:
                    print(f"Port {port} is CLOSED or FILTERED")
                    closed += 1
                else:
                    closed += 1
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
            closed += 1

    print(f"\nScan Complete: {closed} of {total} ports CLOSED or FILTERED")



if __name__ == "__main__":
    main()
```