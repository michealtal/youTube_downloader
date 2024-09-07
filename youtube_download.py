from pytube import YouTube
from sys import argv
import os
import urllib.request
import urllib.error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def download_video(link, output_path):
    try:
        # Initialize YouTube object without OAuth
        yt = YouTube(link)
        
        print("Title: ", yt.title)
        print("Views: ", yt.views)
        print("Length: ", yt.length, "seconds")
        
        # Handle case where description might be None
        description = yt.description if yt.description else "No description available"
        print("Description: ", description[:100] + "..." if len(description) > 100 else description)

        # Filter for MP4 streams and get the highest resolution
        yd = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        
        # Create the output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Download the video
        print("Downloading...")
        yd.download(output_path)
        print("Download completed!")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    if len(argv) < 2:
        print("Please provide a YouTube URL as an argument.")
    else:
        link = argv[1]
        output_path = '/Users/Micheal/Desktop/downloadedvid'
        download_video(link, output_path)
