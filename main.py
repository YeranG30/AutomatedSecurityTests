import sys
import subprocess
import os
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox

def run_amass(domain, output_file):
    amass_path = r'C:\Users\yeran\Downloads\amass_Windows_amd64\amass.exe'
    command = [amass_path, 'enum', '-passive', '-d', domain]
    return run_command(command, "Amass", output_file)

def run_nmap(ip_address, output_file):
    nmap_path = "nmap"  # Assuming nmap is in your PATH; otherwise provide the full path
    output_dir = os.path.dirname(output_file)  # Use the directory of the output file

    nmap_commands = {
        "full_ping_scan": [nmap_path, "-Pn", "-p-", ip_address, "-oA", os.path.join(output_dir, "full_ping_scan")],
        "syn_scan_version": [nmap_path, "-sS", "-Pn", "-sV", "-O", "-p-", ip_address, "-oA", os.path.join(output_dir, "syn_scan_version")],
        "connect_scan_scripts": [nmap_path, "-sT", "-Pn", "-sC", "-O", "-p-", ip_address, "-oA", os.path.join(output_dir, "connect_scan_scripts")],
        "intense_scan": [nmap_path, "-A", "-Pn", "-T4", ip_address, "-oA", os.path.join(output_dir, "intense_scan")],
        "vuln_scan": [nmap_path, "--script", "vuln", "-Pn", ip_address, "-oA", os.path.join(output_dir, "vuln_scan")],
        "top_ports_scan": [nmap_path, "--top-ports", "1000", "-Pn", ip_address, "-oA", os.path.join(output_dir, "top_ports_scan")],
        "owasp_top10_scan": [nmap_path, "--script", "http-sql-injection,http-sql-injection-detect,http-auth-finder,http-brute,http-enum,http-config-backup,http-xxe,http-methods,http-vuln-cve2017-5638,http-default-accounts", "-Pn", ip_address, "-oA", os.path.join(output_dir, "owasp_top10_scan")],
        "http_sitemap_scan": [nmap_path, "--script", "http-sitemap-generator", "-Pn", ip_address, "-oA", os.path.join(output_dir, "http_sitemap_scan")],
        "dns_brute_scan": [nmap_path, "--script", "dns-brute", "-Pn", ip_address, "-oA", os.path.join(output_dir, "dns_brute_scan")],
        "whois_scan": [nmap_path, "--script", "whois*", "-Pn", ip_address, "-oA", os.path.join(output_dir, "whois_scan")],
        "http_xss_scan": [nmap_path, "-p80", "--script", "http-unsafe-output-escaping,http-sql-injection", "-Pn", ip_address, "-oA", os.path.join(output_dir, "http_xss_scan")]
    }

    for scan_name, command in nmap_commands.items():
        run_command(command, f"Nmap {scan_name}", output_file)

def run_wafwoof(url, output_file):
    python_path = r'C:\Users\yeran\AppData\Local\Programs\Python\Python312\python.exe'
    wafw00f_script = r'C:\Users\yeran\AppData\Local\Programs\Python\Python312\Scripts\wafw00f'
    command = [python_path, wafw00f_script, url]
    return run_command(command, "WAFW00F", output_file)

def run_ffuf(url, wordlist, output_file):
    ffuf_path = r'C:\Users\yeran\go\bin\ffuf.exe'
    command = [ffuf_path, '-u', f'{url}/FUZZ', '-w', wordlist, '-o', output_file]
    return run_command(command, "FFUF", output_file)

def run_theharvester(domain, output_file):
    harvester_path = r'C:\Users\yeran\theHarvester\theHarvester.py'
    command = ['python', harvester_path, '-d', domain, '-b', 'all']
    return run_command(command, "TheHarvester", output_file)

def run_command(command, tool_name, output_file):
    try:
        with open(output_file, 'a') as f:
            f.write(f"Running {tool_name}:\n")
            f.write(f"Command: {' '.join(command)}\n")
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            f.write("Output:\n")
            f.write(result.stdout)
            f.write("\nErrors (if any):\n")
            f.write(result.stderr)
            if result.returncode == 0:
                f.write(f"{tool_name} completed successfully.\n")
            else:
                f.write(f"{tool_name} encountered an error.\n")
            f.write("=" * 40 + "\n\n")
    except Exception as e:
        with open(output_file, 'a') as f:
            f.write(f"An exception occurred while running {tool_name}: {e}\n")
            f.write("=" * 40 + "\n\n")

class PenTestingTool(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pen Testing Tool Integrator')
        self.resize(600, 400)  # Set the initial size of the window

        layout = QVBoxLayout()

        self.domain_label = QLabel('Domain:')
        layout.addWidget(self.domain_label)
        self.domain_entry = QLineEdit(self)
        layout.addWidget(self.domain_entry)

        self.target_label = QLabel('Target IP:')
        layout.addWidget(self.target_label)
        self.target_entry = QLineEdit(self)
        layout.addWidget(self.target_entry)

        self.url_label = QLabel('URL:')
        layout.addWidget(self.url_label)
        self.url_entry = QLineEdit(self)
        layout.addWidget(self.url_entry)

        self.wordlist_label = QLabel('Wordlist:')
        layout.addWidget(self.wordlist_label)
        self.wordlist_entry = QLineEdit(self)
        layout.addWidget(self.wordlist_entry)

        self.browse_wordlist_button = QPushButton('Browse Wordlist', self)
        self.browse_wordlist_button.clicked.connect(self.browse_wordlist)
        layout.addWidget(self.browse_wordlist_button)

        self.output_file_label = QLabel('Output File:')
        layout.addWidget(self.output_file_label)
        self.output_file_entry = QLineEdit(self)
        layout.addWidget(self.output_file_entry)

        self.browse_output_file_button = QPushButton('Browse Output File', self)
        self.browse_output_file_button.clicked.connect(self.browse_output_file)
        layout.addWidget(self.browse_output_file_button)

        self.run_button = QPushButton('Run Tools', self)
        self.run_button.clicked.connect(self.run_tools)
        layout.addWidget(self.run_button)

        self.setLayout(layout)

    def browse_wordlist(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Wordlist", r"C:\Users\yeran\PycharmProjects\AutomatedPenTestingScript\SecLists\Discovery\Web-Content", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.wordlist_entry.setText(fileName)

    def browse_output_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Select Output File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            self.output_file_entry.setText(fileName)

    def run_tools(self):
        domain = self.domain_entry.text()
        target = self.target_entry.text()
        url = self.url_entry.text()
        wordlist = self.wordlist_entry.text()
        output_file = self.output_file_entry.text()

        if not (domain and target and url and wordlist and output_file):
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        self.thread = threading.Thread(target=self.run_all_tools, args=(domain, target, url, wordlist, output_file))
        self.thread.start()

    def run_all_tools(self, domain, target, url, wordlist, output_file):
        try:
            with open(output_file, 'w') as f:
                f.write("Pen Testing Tool Output\n")
                f.write("=" * 40 + "\n")

            print("Running amass...")
            run_amass(domain, output_file)
            print("Running multiple Nmap scans...")
            run_nmap(target, output_file)
            print("Running wafw00f...")
            run_wafwoof(url, output_file)
            print("Running ffuf...")
            run_ffuf(url, wordlist, output_file)
            print("Running theHarvester...")
            run_theharvester(domain, output_file)

            QMessageBox.information(self, "Done", "All tools have been run.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PenTestingTool()
    ex.show()
    sys.exit(app.exec_())
