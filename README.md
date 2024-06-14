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
Requirements: 
Manually add path to all tools within code (done with repeated use of script in mind, saving time) 
Python 3.x
Installation of Amass, Nmap, GoBuster, theHarvester, and WafWoof
PyQt5 for the GUI interface
Wordlist for Directory Bruteforcing 



# Comprehensive Security Assessment Report for OWASP Juice Shop

## Executive Summary

### Introduction
This report provides a comprehensive security assessment of the OWASP Juice Shop infrastructure with thorough security insights using a plethora of the latest security tools such as theHarvester, Nmap, Fluff, WafWoof, and Amass. The purpose of this analysis is to cherry-pick all possible security vulnerabilities to then be able to form well-founded actionable advice and suggestions to improve the security framework of OWASP Juice Shop. This evaluation will assess compliance with network services patterns, the robustness of Web application protections, and the extent of exposure to external threats, all aimed at enhancing the security robustness of OWASP Juice Shop.

### Disclaimer
This security assessment is conducted purely for educational purposes. All activities are performed under clear rules of engagement that include only scanning and no other intrusive actions. Permission has been obtained to perform these scans within the specified scope.

## In-Depth Analysis
![image](https://github.com/YeranG30/AutomatedSecurityTests/assets/74067706/f0d70471-6336-4b60-bc35-d50938fe4f14)

![image](https://github.com/YeranG30/AutomatedSecurityTests/assets/74067706/e0e11b6a-6695-4717-b3c7-296eb61e99a1)

### 1. Objective Purpose
The purpose of this post-exploit objective is to deploy Amass to perform a name-server sweep of DNS enumeration to discover a vast amount of subdomains related to OWASP Juice Shop in the hope of uncovering key organizational aspects and potential attack or infection vectors. They find a lot of DNS records and subdomains for OWASP Juice Shop, like an exhaustively detailed and broad range of services from complex load balancing systems to pretty complex messaging platforms.

#### Amass Findings:
- **General Risk**: The open visibility of internal domain names may pose a substantial risk in that threat actors may be able to use this to tailor attacks, possibly resulting in the release of sensitive information or unauthorized system access.

#### Strategic Recommendations:
- **Action Steps**: Bolster DNS security protocols, limit exposure of sensitive subdomain data, and enforce meticulously extensive DNS query and response monitoring to prevent exploitations.

#### Supporting Evidence:
- owasp-juice.shop (FQDN) --> mx_record --> smtpin.rzone.de (FQDN)
- demo.owasp-juice.shop (FQDN) --> mx_record --> smtpin.rzone.de (FQDN)

### 2. Analysis theHarvester

#### Objective Purpose
Extract publicly available emails, subdomains, and employee data from theHarvester to assess the threat landscape in terms of exposure of information.

#### Critical Findings
- **Main Discovery**: Discovery of many unsecured subdomains and their associated email addresses which can be exploited to run Phishing attack or any form of social engineering.

#### Increased Risk Due to Security Concerns
- **Risk**: This release makes it significantly easier to target assets such as email addresses and subdomains that could lead to highly targeted, spear-phishing campaigns against OWASP Juice Shop employees that could result in mass theft of trial or unauthorized access.

#### Takeaway Advice for Prudent Actions
- **Recommendations**: Apply stringent email filtering rules, conduct regular cybersecurity training programs for all employees, and deploy a high-grade threat detection solution to minimize the phishing risks efficiently.

#### Documentary Evidence

![image](https://github.com/YeranG30/AutomatedSecurityTests/assets/74067706/2eec9bb3-c9b4-4d10-8833-d38b4940eed8)

### 3. Objective Nmap Network Scanning

#### Purpose
Perform Nmap scans to identify open ports, running services, and evaluate the network threat exposure from outside threats, validate service configurations and security.

#### Observations Analysis
- **Analysis**: Ensuring the security of ports containing critical services such as HTTPS and DNS and authentication mechanisms are up-to-date to secure the main data flows of OWASP Juice Shop. Open ports can leave OWASP Juice Shop vulnerable to security breaches, unauthorized access, and a host of exploits that could have a serious impact on the overall network security.

#### Preventative Tools Measures
- **Recommendations**: Continue to update and patch for the services those ports are associated with, do strict penetration tests for the purpose of identifying and mitigating existing vulnerabilities.

#### Visual Documentation
- ![image](https://github.com/YeranG30/AutomatedSecurityTests/assets/74067706/8c8966d0-b0b9-43fb-977a-4440cb2f5e20)
- ![image](https://github.com/YeranG30/AutomatedSecurityTests/assets/74067706/d12a30f0-7b40-45c8-8733-637cc2bf9265)
- ![image](https://github.com/YeranG30/AutomatedSecurityTests/assets/74067706/ff42e468-6dac-4d46-97d4-31de626b09d0)
-![image](https://github.com/YeranG30/AutomatedSecurityTests/assets/74067706/fc6e508d-b3a4-406a-a4bc-c0084622d872)
- ![image](https://github.com/YeranG30/AutomatedSecurityTests/assets/74067706/dc72f4be-6bcf-45ab-85ed-3cfd7e76b620)
- ![image](https://github.com/YeranG30/AutomatedSecurityTests/assets/74067706/eb564a9a-3a0d-4b65-b046-9bb5ed6d8acd)



- 


### 4. Fluff Directory Enumeration

#### Objective Goal
To perform directory and file brute-forcing using Fluff to discover open resources and poorly configured permissions on the web servers of OWASP Juice Shop.

#### Findings Results
- **Findings**: Discovered multiple disjoint directories which might contain sensitive information and even though are not available directly on the main website but could have been exploited by malicious people in case they are discovered.

#### Security Implications
- **Risk**: Unauthorized access to sensitive directories could possibly result in major data breaches if these resources are not adequately secured.

#### Security Guidelines Recommendations
- **Recommendations**: Reduce the threat surface by enforcing some access controls on sensitive directories, use strong methods for authentication, and audit frequently all the assets in the platform.

#### Evidence
![image](https://github.com/YeranG30/AutomatedSecurityTests/assets/74067706/9bf41e02-db86-44ae-9f66-cf54eaf9ddd4)



### 5. Objective of WafWoof Investigation
![image](https://github.com/YeranG30/AutomatedSecurityTests/assets/74067706/90261c2b-c9e2-4e1b-90aa-5a09a29e80e6)

#### Purpose
To assess how well OWASP Juice Shop's web applications are protected against common web-based attacks by Web Application Firewalls (WAFs).

#### Analytical Results Insight
- **Insight**: Not finding standard Web Application Firewalls, they are using custom security solutions or obfuscating the settings for standard detection.

#### Web Application Vulnerabilities
- **Risk**: The absence of detectable WAFs may hint at invaluable gaps in the web application security framework or that the WAF configurations are so complex and customized.

## OWASP Juice Shop Information
- **Domain**: `demo.owasp-juice.shop`
- **URL**: [https://demo.owasp-juice.shop/](https://demo.owasp-juice.shop/)
- **IP Address**: Use `nslookup` or `dig` to resolve the current IP address for the domain.

### Command to Find IP Address:
- **nslookup**:
  ```bash
  nslookup demo.owasp-juice.shop

### Conclusion 
This security assessment provides a comprehensive evaluation of the OWASP Juice Shop's security posture, uncovering various potential vulnerabilities and areas for improvement. By addressing the recommendations outlined in this report and implementing robust security measures, OWASP Juice Shop can significantly enhance its resilience against cyber threats. This exercise also underscores the importance of continuous monitoring and regular security audits to maintain a strong defense against evolving threats. The attached evidence supports the detailed analysis, offering a clear path forward for fortifying the security framework of OWASP Juice Shop.

This report and its findings should be used responsibly and solely for educational purposes, respecting the ethical guidelines of cybersecurity practices.
