import sys
import subprocess


def run_wafwoof(url):
    try:
        # Provide the full path to the Python executable
        python_path = r'C:\Users\yeran\AppData\Local\Programs\Python\Python312\python.exe'

        # Path to wafw00f script
        wafw00f_script = r'C:\Users\yeran\AppData\Local\Programs\Python\Python312\Scripts\wafw00f'

        # Command to run WAFW00F using Python
        command = [python_path, wafw00f_script, url]

        # Running the command and capturing the output
        result = subprocess.run(command, capture_output=True, text=True)

        # Checking if the command was successful
        if result.returncode == 0:
            print("WAFW00F Results:\n")
            print(result.stdout)
        else:
            print("An error occurred:\n")
            print(result.stderr)
    except Exception as e:
        print(f"An exception occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Script_wafwoof_scan.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    run_wafwoof(url)
