import sys
import subprocess
import os


def run_amass(domain, output_dir, amass_path):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Amass command
    amass_output_file = os.path.join(output_dir, f'{domain}_subdomains.txt')
    command = [
        amass_path, 'enum', '-passive', '-d', domain, '-o', amass_output_file
    ]

    # Run the command
    try:
        subprocess.run(command, check=True)
        print(f"Subdomain enumeration completed for {domain}. Results saved in {amass_output_file}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python Script_amass_scan.py <domain> <output_dir> <amass_path>")
        sys.exit(1)

    domain = sys.argv[1]
    output_dir = sys.argv[2]
    amass_path = sys.argv[3]

    run_amass(domain, output_dir, amass_path)
