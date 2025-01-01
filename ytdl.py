import yt_dlp
import sys
import os

current_dir = os.getcwd()
output_path = os.path.join(current_dir)

def download_vid_to_mp3(url, output_path=output_path):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {
                'key': 'EmbedThumbnail',
            },
        ],
        'writethumbnail': True,
        'quiet': True,
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
    print("Download complete.")


def download_vid_to_mp4(url, output_path=output_path):
    options = {
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }
        ],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
    print("Download complete.")


if len(sys.argv) > 2:
    mode = sys.argv[1]
    urls = sys.argv[2:]
    for url in urls:
        if mode == 'v':
            download_vid_to_mp4(url)
        elif mode == 'm':
            download_vid_to_mp3(url)
        else:
            print("Invalid mode. Use 'v' for video or 'm' for mp3.")
else:
    print("Usage: ytdl <mode> '<url_link1>' ")
    print("Modes: 'v' for video, 'm' for mp3")
