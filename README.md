# Smart-Detection-System
Smart-Firewall written in python to filter traffic on any GNU\Linux system<br>
This can be use as an easy to use local hostbased firewall to block unwanted traffic such as bad ip,malware sites,ads,unwanted content on web pages.<br>
Usage is quite simple just hit -h and every command should have a proper description if not feel free to write me an issue or email.<br>

Small PoC:
<br><br>
._________________.<br>
 | _______________ |<br>
 | I             I |<br>
 | I             I |<br>
 | I    HOST     I |<br>
 | I             I |<br>
 | I_____________I |        --->    Any Linux Device     --->   Internet or Gateway  <br>                                      
 !_________________!              (Raspberry pi,Desktop pc,DD-WRT router)<br>
    ._[_______]_.<br>
.___|___________|___.<br>
|::: ____           |<br>
|    ~~~~ [CD-ROM]  |<br>
!___________________!<br>
<br>
<br>
A Forced Way to be the firewall on the network even if you are not the administrator could be :<br>
-ARP Poisoning then Running the SDS Firewall<br>
-ICMP Redirect then Running the SDS firewall<br>
<br>

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



