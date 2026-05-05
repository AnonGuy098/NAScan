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
-This is currently active under the MIT license. You may copy, edit, distribute, publish, modify, merge, sublicense and sell the software. 
-The only requirement is that original copyright notice and license text  must be included in any and all copies or substancial portions of the software.
-The software is provided “as is”, without warranty — meaning the author isn’t responsible for any issues, damages, or liabilities that arise from using it.

**This project is only for educational purposes and is not meant to cause harm to any individuals, organizations or groups. Any damage to such cannot hold me, as a creator responsible for such actions**. 
