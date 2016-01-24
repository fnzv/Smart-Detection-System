# Smart-Detection-System
Smart-Firewall written in python to filter traffic on any GNU\Linux system<br>
This can be use as an easy to use local hostbased firewall to block unwanted traffic such as bad ip,malware sites,ads,unwanted content on web pages.<br>
Usage is quite simple just hit -h and every command should have a proper description if not feel free to write me an issue or email.<br>





# Small PoC
<br><br>

Your Host(s)  <--->    Any Linux Device    <--->   Internet or Gateway  <br>                                      
Could be LAN or WLAN network,
My original idea was a raspberry pi as a local firewall that filters any unwanted content from the internet and this script is doing pretty well, a good feature is to force dns traffic to go trough a known dns server to avoid dns leaks and at the same time apply filters on traffic via blacklists or whitelists(Not suggested as might block a lot)

Device Examples: (Raspberry pi,odroid,Desktop pc,DD-WRT or custom router,Virtual Machine)<br>

<br>
<br>
I Call these below part of the "Offensive SDS Firewall"<br>
A Forced Way to be the firewall on the network even if you are not the administrator could be :<br>
-ARP Poisoning <br>
-ICMP Redirect <br>
-DNS Redirect<br>
-Transparent Proxy Redirect<br>
-Traffic control(Bandwidth,Delays,Packets..) <br>
<br>

***WARNING***:Keyword based filtering could fail as it's an experimental feature of iptables .. overall works fine and blocks unwanted sites

<br>
#######  Smart Detecton System - An Easy to use Smart-Firewall coded in python
#######  STATUS: Still under developement
####### Features: 
#######    - Block unwanted Sites,URLs,IP,DNS requests (using filter lists)
#######    - Analize processes running on host and allow only used connections     
#######    - Anti-Malware Scanning realtime
#######    - Show network connections on an easy-adaptive webGUI
#######    - Optimize most used network connections with a local dns
#######    - Parse capture files and extract ip addresses,domains,dns for firewall rules
#######    - Everytime someone hits the firewall via blacklist or whitelist is being logged
#######    - Captive Portal Registration to the firewall to force users to subscribe
#######    - Distinct releases SDS for server & client... "cloud" distributed firewall system  
#######    - Redirect ALL DNS Requests to any DNS Server specified(Example : OpenDNS and then log access or local DNS) 

####  Author: Yessou Sami 



