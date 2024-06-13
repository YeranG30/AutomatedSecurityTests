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
    domain = ""  # Replace with your target domain
    output_dir = ""  # Output directory for the results
    amass_path = "C:\Users\ExampleUser\Documents\Tools"  # Replace with the full path to your Amass executable

    run_amass(domain, output_dir, amass_path)
