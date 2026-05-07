# NAScan
NAScan is a lightweight subnet analyzer that detects alive hosts, resolves hostnames, identifies MAC addresses and vendors, and scans for open ports. Designed for fast local network reconnaissance, it helps pentesters and sysadmins quickly profile devices on a subnet.

**How to download:**
1. Clone the repository :
   git clone https://github.com/AnonGuy098/nascan.git
   cd NAScan

2. Run the python file :
   python3 nascan.py

**Make NAScan system-wide:**
1. Make the script executable :
   chmod +x nascan.py

2. Move it to the path : (/usr/local/bin)
   sudo mv nascan.py /usr/local/bin/nascan

3. Now you can run NAScan from anywhere in the system
   nascan

**Features**  
Bullet list of what NAScan does right now (alive host detection, MAC/vendor lookup, hostname resolution, port scanning).
Example:

    Detects alive hosts on a subnet

    Resolves hostnames automatically

    Identifies MAC addresses and vendors

    Scans for open TCP ports


**Python dependencies used:**
-ipaddress
-socket
-subprocess


**License:**
- This project is active under the GPL GNU License. Kindly read the license file to know more.

**This project is only for educational purposes and is not meant to cause harm to any individuals, organizations or groups. Any damage to such cannot hold me, as a creator responsible for such actions**. 
