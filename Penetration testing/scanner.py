#Developing Nmap Scanner
#We had to create a virtual env to run nmap, FYI nmap.PortScanner only runs when you download python-nmap and not python3-nmap
#First we import nmap
import nmap

#nmap port scanner class
scanner = nmap.PortScanner()

print('Welcome, this is an nmap automation tool ')
print('<--------------------------------------->')

ip_addr = input('Please enter the IP address you want to scan: ')
print('The IP address you entered is: ', ip_addr)
type(ip_addr)

