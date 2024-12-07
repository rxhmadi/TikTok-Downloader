import requests
import os
import re

# ANSI escape codes for colored text
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def sanitize_filename(filename):
    """
    Sanitize the filename to ensure it is safe for saving.
    """
    return re.sub(r'[\\/*?:"<>|]', "_", filename)

def bulk_download(api_url, input_file, output_folder):
    """
    Bulk download TikTok videos using the provided API.

    :param api_url: The TikTok downloader API URL
    :param input_file: Text file containing TikTok URLs
    :param output_folder: Folder to save downloaded videos
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read TikTok URLs from the input file
    with open(input_file, 'r') as file:
        urls = file.readlines()

    for index, video_url in enumerate(urls):
        video_url = video_url.strip()  # Clean up whitespace
        if not video_url:
            continue

        try:
            print(f"{Colors.OKBLUE}Processing URL {index + 1}/{len(urls)}: {video_url}{Colors.ENDC}")
            
            # Send POST request to API
            response = requests.post(api_url, json={"url": video_url})
            response.raise_for_status()

            # Parse the API response
            data = response.json()

            # Extract video URL with "hd_no_watermark" quality
            medias = data.get("medias", [])
            video_link = None
            for media in medias:
                if media.get("type") == "video" and media.get("quality") == "hd_no_watermark":
                    video_link = media.get("url")
                    break

            if not video_link:
                print(f"{Colors.WARNING}No video with 'hd_no_watermark' quality found for URL: {video_url}{Colors.ENDC}")
                continue

            # Prepare filename using "author" and "title"
            author = data.get("author", "unknown_author")
            title = data.get("title", "unknown_title")
            sanitized_filename = sanitize_filename(f"{author} - {title}.mp4")
            video_filename = os.path.join(output_folder, sanitized_filename)

            # Log the original CDN URL
            print(f"{Colors.OKGREEN}Downloading video from CDN: {video_link}{Colors.ENDC}")

            # Download the video
            video_response = requests.get(video_link, stream=True)
            video_response.raise_for_status()

            # Save the video to the output folder
            with open(video_filename, 'wb') as video_file:
                for chunk in video_response.iter_content(chunk_size=8192):
                    video_file.write(chunk)

            print(f"{Colors.BOLD}✅ Downloaded: {video_filename}{Colors.ENDC}")

        except requests.exceptions.RequestException as e:
            print(f"{Colors.FAIL}Error processing URL {video_url}: {e}{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    # API URL for TikTok downloader
    api_url = "https://myapi.app/api/analyze"

    # Input file containing TikTok URLs
    input_file = "urls.txt"

    # Output folder to save videos
    output_folder = "downloads"

    bulk_download(api_url, input_file, output_folder)
