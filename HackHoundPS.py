import socket
from IPy import IP
import pyfiglet

banner = """
██   ██  █████   ██████ ██   ██ ██   ██  ██████  ██    ██ ███    ██ ██████  ██████  ███████ 
██   ██ ██   ██ ██      ██  ██  ██   ██ ██    ██ ██    ██ ████   ██ ██   ██ ██   ██ ██      
███████ ███████ ██      █████   ███████ ██    ██ ██    ██ ██ ██  ██ ██   ██ ██████  ███████ 
██   ██ ██   ██ ██      ██  ██  ██   ██ ██    ██ ██    ██ ██  ██ ██ ██   ██ ██           ██ 
██   ██ ██   ██  ██████ ██   ██ ██   ██  ██████   ██████  ██   ████ ██████  ██      ███████ 
                                                                                            
                                                                                               
"""
print(banner)


def scan(sip, num, rate = 0.3):  
    try:       
        checked_ip = check_ip(sip)
        for port in range(1, num):
            port_scan(checked_ip, port, rate)
        print('\nscan completed ....')
    except:
        print('invalide address : ' + sip)



def get_banner(s):                     
    return s.recv(1024)


def check_ip(cip):                      
    try:
        IP(cip)
        return cip
    except ValueError:
        return socket.gethostbyname(cip)



def port_scan(sip, port, rate):         
    try:
        sock = socket.socket()
        sock.settimeout(rate)
        sock.connect((sip, port))
        try:
            banner = get_banner(sock)
            print("\n[+] open port "+str(port)+" of "+str(sip)+" : "+str(banner.decode().strip('\n')))
        except:
            print("\n[+] open port "+str(port)+" of "+str(sip))
    except:
        print('#',end = '')


if __name__ == "__main__":
    num = int(input('\nEnter the number of ports needed to be scanned: '))
    rate = float(input('enter the rate of scan(0.3 - 1) (note the more fasert the scan the less accurate the scan will be) default (rate = 0.3) : ' ) or '0.3')
    ip_add = input("ENTER THE TARGET/s (use ',' to specify multiple targets) : ")
    print('searching for open ports pls wait........')
    if ',' in ip_add:
        for ip in ip_add.split(','):
            scan(ip.strip(' '), num)
    else:
        scan(ip_add, num, rate)
        