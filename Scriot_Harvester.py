import sys
import subprocess


def run_the_harvester(domain):
    try:
        # Provide the correct path to theHarvester.py using a raw string
        harvester_path = r'C:\Users\yeran\theHarvester\theHarvester.py'

        # Command to run theHarvester
        command = ['python', harvester_path, '-d', domain, '-b', 'all']

        # Running the command and capturing the output
        result = subprocess.run(command, capture_output=True, text=True)

        # Checking if the command was successful
        if result.returncode == 0:
            print("TheHarvester Results:\n")
            print(result.stdout)
        else:
            print("An error occurred:\n")
            print(result.stderr)
    except Exception as e:
        print(f"An exception occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Script_theHarvester.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    run_the_harvester(domain)
