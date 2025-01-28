from pytube import YouTube
from pytube.cli import on_progress
import requests
from pytube import request

# Function to set headers manually
def set_custom_headers(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.content

# URL of the YouTube video
video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Replace with your video URL

# Create YouTube object and use the custom headers
yt = YouTube(video_url, on_progress_callback=on_progress)

# Override the default request method with custom headers
yt.streams.get_highest_resolution().download()

print(f"Video '{yt.title}' downloaded successfully.")
