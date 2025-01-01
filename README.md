# YouTube Downloader

This is a simple YouTube downloader script that allows you to download videos as MP3 or MP4 files using `yt_dlp`.

## Requirements

- Python 3.x
- `yt_dlp` library
- `ffmpeg` (for audio and video processing)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install `yt_dlp` using pip:
   ```sh
   pip install yt-dlp
   ```
3. Install `ffmpeg` from ffmpeg.org and make sure it is available in your system's PATH.

## Usage

To use the downloader, you can run the ytdl.bat script from the command line

The downloaded file will be placed on the folder you're currently on

### Download MP3

To download a video as an MP3 file, use the `m` mode:

```sh
ytdl m "<url_link>"
```

### Download MP4

To download a video as an MP4 file, use the `v` mode:

```sh
ytdl v "<url_link>"
```

## Note

- Change the file path in your preferred directory in the source code
- Change the file path in the batch file to match your source code location
- You can put the `ytdl.bat` in the system32 folder for easy access
