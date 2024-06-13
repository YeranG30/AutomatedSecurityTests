import sys
import subprocess


def run_ffuf(url, wordlist):
    try:
        # Hardcoded paths
        ffuf_path = r'C:\Users\yeran\go\bin\ffuf.exe'  # Path to ffuf executable

        # Command to run ffuf
        command = [ffuf_path, '-u', url, '-w', wordlist]

        # Running the command and capturing the output
        result = subprocess.run(command, capture_output=True, text=True)

        # Checking if the command was successful
        if result.returncode == 0:
            print("ffuf Results:\n")
            print(result.stdout)
        else:
            print("An error occurred:\n")
            print(result.stderr)
    except Exception as e:
        print(f"An exception occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Script_ffuf_scan.py <url> <wordlist>")
        sys.exit(1)

    url = sys.argv[1]
    wordlist = sys.argv[2]
    run_ffuf(url, wordlist)
