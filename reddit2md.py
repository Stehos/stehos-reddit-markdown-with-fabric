import re
import os
import argparse

def ensure_directory_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def generate_unique_filename(folder, title):
    # Generate a base filename from the title
    base_filename = title.replace(" ", "-").replace(",", "").lower() + ".md"
    filepath = os.path.join(folder, base_filename)

    # Check if the file already exists, and append a number if necessary
    if os.path.exists(filepath):
        # If the file exists, append a number to the filename
        counter = 1
        while os.path.exists(filepath):
            # Create new filename with number appended
            new_filename = f"{title.replace(' ', '-').replace(',', '').lower()}-{counter}.md"
            filepath = os.path.join(folder, new_filename)
            counter += 1

    return filepath

# Function to parse the basic sections
# Function to parse the basic sections with default values for missing fields
def parse_basic_info(text):
    # Safely search for each section
    title_match = re.search(r'Title: (.*)', text)
    author_match = re.search(r'Author: (.*)', text)
    upvotes_match = re.search(r'Upvotes: (\d+)', text)
    body_match = re.search(r'Body text: (.*?)(\d+ Comments)', text, re.DOTALL)
    comments_match = re.search(r'(\d+) Comments:\n--------\n(.+)', text, re.DOTALL)

    # Extract values or set defaults
    title = title_match.group(1) if title_match else "Unknown Title"
    author = author_match.group(1) if author_match else "Unknown Author"
    upvotes = int(upvotes_match.group(1)) if upvotes_match else 0
    body_text = body_match.group(1).strip() if body_match else "No body text available."
    comment_count = int(comments_match.group(1)) if comments_match else 0
    raw_comments = comments_match.group(2).strip() if comments_match else "No comments available."

    return {
        "Title": title,
        "Author": author,
        "Upvotes": upvotes,
        "Body text": body_text,
        "Comment count": comment_count,
        "Raw comments": raw_comments
    }


# Function to parse comments and threads
def parse_comments(raw_comments):
    comments = []
    pattern = re.compile(r'\| (.*?) \((\d+) upvotes\): (.*)')
    subcomment_pattern = re.compile(r'\| \| (.*?) \((\d+) upvotes\): (.*)')

    current_comment = None

    for line in raw_comments.splitlines():
        match = pattern.match(line)
        sub_match = subcomment_pattern.match(line)

        if match:
            if current_comment:
                comments.append(current_comment)
            current_comment = {
                'author': match.group(1),
                'upvotes': int(match.group(2)),
                'text': match.group(3),
                'replies': []
            }
        elif sub_match:
            reply = {
                'author': sub_match.group(1),
                'upvotes': int(sub_match.group(2)),
                'text': sub_match.group(3),
            }
            if current_comment:
                current_comment['replies'].append(reply)

    if current_comment:
        comments.append(current_comment)

    return comments

def save_as_markdown(parsed_data, comments, folder="markdown_files"):
    # Create folder if it doesn't exist
    ensure_directory_exists(folder)
    filepath = generate_unique_filename(folder, parsed_data["Title"])

    # Start building the markdown content
    markdown_content = f"# {parsed_data['Title']}\n\n"
    markdown_content += f"**Author**: {parsed_data['Author']}\n"
    markdown_content += f"**Upvotes**: {parsed_data['Upvotes']}\n\n"
    markdown_content += f"## Body\n{parsed_data['Body text']}\n\n"
    markdown_content += f"## Comments ({parsed_data['Comment count']})\n"

    # Function to recursively format comments and replies
    def format_comment(comment, indent_level=0):
        indent = "    " * indent_level
        comment_text = f"{indent}- **{comment['author']}** ({comment['upvotes']} upvotes): {comment['text']}\n"
        if comment['replies']:
            for reply in comment['replies']:
                comment_text += format_comment(reply, indent_level + 1)
        return comment_text

    # Add comments to markdown
    for comment in comments:
        markdown_content += format_comment(comment)

    # Write the markdown content to a file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Markdown saved as: {filepath}")

# Check for input text from command line arguments
parser = argparse.ArgumentParser(description='Create markdown file')
parser.add_argument('text', type=str, help='Content that markdown should be created from.')
parser.add_argument('outputPath', type=str, nargs='?', default='markdown_files', help='The output path for your md file.')

args = parser.parse_args()

# Parsing the text
basic_info = parse_basic_info(args.text)
comments = parse_comments(basic_info['Raw comments'])

save_as_markdown(basic_info, comments, args.outputPath)