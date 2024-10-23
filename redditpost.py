import sys
import subprocess
import argparse
import os

def main(url, outputPath):
    # Find the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Paths to the other scripts (reddit2txt.py and reddit2md.py)
    reddit2txt_path = os.path.join(script_dir, 'reddit2txt.py')
    reddit2md_path = os.path.join(script_dir, 'reddit2md.py')

    try:
        # Run the first script (reddit2txt.py)
        result = subprocess.run(['python3', reddit2txt_path, url],
                                capture_output=True, text=True, check=True)
        output = result.stdout.strip()  # Get the output from the first script

        # Now call the second script (reddit2md.py) with the output
        subprocess.run(['python3', reddit2md_path, output, outputPath], check=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get text from a Reddit post.')
    parser.add_argument('url', type=str, help='The URL of the Reddit post to textualize.')
    parser.add_argument('outputPath', type=str, help='The output path for your md file.')
    args = parser.parse_args()
    main(args.url, args.outputPath)
