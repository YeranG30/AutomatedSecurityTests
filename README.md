# AutomatedSecurityTest

**AutomatedSecurityTest** is a comprehensive Python-based framework designed to automate the entire network reconnaissance and vulnerability detection process. This tool integrates several powerful security tools, including Amass, Nmap, GoBuster, theHarvester, and WafWoof, to streamline assessments and significantly reduce testing time.

## Features
- **Automated Network Reconnaissance:** Seamlessly integrate and run multiple reconnaissance tools to gather detailed information about the target network.
- **Vulnerability Detection:** Identify potential security vulnerabilities, including those listed in the OWASP Top 10, to facilitate targeted testing and remediation.
- **Tool Integration:** Combines the capabilities of Amass, Nmap, GoBuster, theHarvester, and WafWoof into a single automated workflow.
- **Efficiency:** Reduces manual testing time by up to 50%, allowing security professionals to focus on analysis and remediation.
- **Custom Scripting:** Includes dynamic, context-specific scripts to enhance troubleshooting and increase overall testing reliability.
- **Modular Design:** Allows the user to operate individual tools as standalone applications or in various combinations through the main script, offering flexibility in conducting assessments.

## Tool Descriptions
- **Amass:** Performs DNS enumeration to map the network's exposure on the internet by discovering assets associated with domain names.
- **Nmap:** Scans for open ports and detects services and configurations on network devices.
- **GoBuster:** Conducts directory and file brute-forcing to discover hidden resources on web servers.
- **theHarvester:** Gathers emails, subdomains, hosts, and employee names from different public sources to aid in reconnaissance.
- **WafWoof:** Identifies and fingerprints Web Application Firewalls (WAF) that protect websites.


## Usage:
1. **Clone the repository:**
   ```sh
   git clone https://github.com/YeranG30/AutomatedSecurityTest.git
   cd AutomatedSecurityTest
   #run the script:
   python main.py
   # To run individual scripts
   python <script>.py
   ```
Prerequisites:
Python 3.x
Installation of Amass, Nmap, GoBuster, theHarvester, and WafWoof
PyQt5 for the GUI interface
Wordlist for Directory Bruteforcing 
