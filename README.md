# Stehos Reddit Markdown With Fabric
![cover](./stehos-reddit-markdown-fabric.jpg)

## Description
A simple tool to extracts text from Reddit posts, converts them into markdown files, and processes them with Fabric. It utilizes several python scripts to achieve this functionality.

### iTerm in action
![iPhone Shortcut](./output.gif)

### iOS Shortcut in action
![iPhone Shortcut](./output2.gif)

## Apple Shortcut for Reddit App Integration
To launch this directly from your iPhone via SSH, use the following link: [Apple Shortcut - Reddit to Markdown](https://www.icloud.com/shortcuts/5c37b952172445238cccb42d7813d00b).

## CLI Usage
To run the main script, use the following command:

```bash
./run-redditpost.sh <reddit_url> <output_directory>
```

### Arguments
- reddit_url: The URL of the Reddit post to process.
- output_directory: The directory path to store the generated markdown file.

### Script Insights
**run-redditpost.sh**

This shell script orchestrates the process by:
- Validating input arguments.
- Activating a Python virtual environment.
- Running redditpost.py to get Reddit text and convert it to markdown.
- Adding Fabric summaries to the markdown file.

**redditpost.py**
- Handles argument parsing for URL and output path.
- Runs reddit2txt.py to fetch the text content from the Reddit post.
Passes the output to reddit2md.py to convert the text into a markdown file.

**reddit2txt.py**
- Uses Reddit API credentials to extract text from a specified Reddit post URL.

Ensure you have the necessary environment variables set for accessing the Reddit API. You should have a .env file or export them in your shell environment with the following keys:

- REDDIT_CLIENT_ID
- REDDIT_CLIENT_SECRET
- REDDIT_USER_AGENT

**reddit2md.py**
- Converts the plain text from reddit2txt.py into a structured markdown format containing the post title, author, upvotes, body text, and comments.
- Output: Saves a markdown file in the specified output directory, ensuring unique filenames.

## Requirements
1. Fabric [https://github.com/danielmiessler/fabric] Make sure the Fabric tool is installed and configured correctly as it is used for appending summaries to the markdown file.
2. Python 3.x and Required Python packages (can be installed via pip)
3. Reddit API credentials (Client ID, Client Secret, User Agent). These are required to access the Reddit API. [https://github.com/NFeruch/reddit2text]


## Installation
0. Install [Fabric](https://github.com/danielmiessler/fabric) on your server & [Generate](https://github.com/NFeruch/reddit2text) your Reddit API Creddentials
1. Clone this repo to your server wherever you want
2. Create env in your app folder: ```python3 -m venv path/to/venv```
3. Activate env via ```source path/to/venv/bin/activate```
4. Install requirements with pip: ```pip3 install -r requirements.txt```
5. Make this script available to run from anywhere you want. Update ```~/.bash_profile``` or ```~/.zshrc```
- Add new line: ```export PATH=$PATH:/path/to/your/cloned/folder```
1. Run script via: ```run-redditpost https://www.reddit.com/r/selfhosted/comments/1g8jytd/best_firewall_for_debian/ ./test```

### Notes
Do not forget change Fabric Pattern to your own. You can find this in run-redditpost file. My is ```--pattern reddit_summary```
- You can add your custom patterns in ~/.config/fabric/my_patterns (if folder does not exist, just create it)
 - Then inside patterns create pattern folder: ```mkdir reddit_summary```
 - Run command: ```fabric --updatepatterns```
 - Copy your patterns into main pattern folder that can be updated by Fabric Team. Inside my_patterns run: ```cp -r ./* ../patterns```
 - Finally list patterns ```fabric --listpatterns```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

## Support

[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/stehos)

