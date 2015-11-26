
#!/usr/bin/python
#######  Smart Detecton System - An Easy to use Smart-Firewall coded in python
####### Features: 
#######    - 
#######    -      
#######    -   
#######    -    
###  Author: Yessou Sami 

#!/usr/bin/python

import os,time,argparse,socket

parser = argparse.ArgumentParser()


parser.add_argument('-i', action='store', dest='int', default="wlan0",
                    help='Interface to log packets')


parser.add_argument('-log', action='store_true', default=False,
                    dest='log',
                    help='Enable logging everypacke packets on /var/log')

parser.add_argument('--blacklist', action='store', default="blacklist.txt",
                    dest='blacklist',
                    help='Load a list with banned keywords\IP\Domains that will be applied on the firewall')
            
parser.add_argument('--whitelist', action='store', default="whitelist.txt",
                    dest='whitelist',
                    help='Load a list with the only permitted keywords\IP\Domains on the firewall')

parser.add_argument('--loadpcap', action='store', default="none",
                    dest='loadpcap',
                    help='Load a list with banned keywords\IP\Domains that will be applied on the firewall')
                    
parser.add_argument('--loadweb', action='store', default="none",
                    dest='loadpcap',
                    help='Load a list with banned keywords\IP\Domains from the web')
                    
parser.add_argument('--GUI', action='store_true', default=False,
                    dest='gui',
                    help='Load the webGUI and start browser to check stats\traffic analysis')      
              


parser.add_argument('-R', action='store_true', default=False,
                    dest='flush',
                    help='Restore default iptables rules')


parser.add_argument('-rule', action='store', dest='ena', default="none", help='Manually create firewall rules via an easy syntax language')


parser.add_argument('--deny', action='store', dest='denyrules', default="none", help='Write deny rules')



parser.add_argument('--permit', action='store', dest='permitrules', default="none", help='Write permit rules')



##Still alpha.. not implemented mitm firewall yet
#parser.add_argument('--spoof', action='store_true', dest='arpspoof',
   #                 help='Enable arp spoofing to apply firewall rules on eth0')


#parser.add_argument('--dg', action='store', dest='dgIP', default="192.168.1.1", help='Specify the ip address of the default gateway to spoof ')





results = parser.parse_args()

if not(results.loadpcap == "none"):
                        print "Reading capture file and parsing ip addresses"
                        print "Only ip addresses found on .pcap will be allowed to pass on this firewall"
                        try:
                                allowedIP=os.popen("""tshark  -o column.format:'"Source", "%s"' -r """+results.loadpcap+" |sort|uniq").read()
                                print allowedIP
                                for line in allowedIP.split():
                                        try:
                                                 socket.inet_aton(line)
                                                 print "Loaded from pcap  ",line
                                                 os.popen("iptables -I FORWARD -p ALL -m string --string  "+line+" --algo kmp -j ACCEPT")
                                        except:
                                                print "This isn't an IP"
                                os.popen("iptables -P FORWARD DROP")
                        except:
                                print "Error Parsing capture"


if(results.log):
        


if(results.flush): #Restore iptables
        os.popen("iptables-restore < /etc/iptables/rules.v4")
   





