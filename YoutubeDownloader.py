# KienKid
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
import sys

def download_youtube_as_mp4(url, output_folder='downloads'):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")

        # Get the highest resolution progressive stream (includes audio)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if video_stream:
            print(f"Downloading in {video_stream.resolution}...")
            video_stream.download(output_path=output_folder)
            print("Download complete.")
        else:
            print("No suitable MP4 stream found with PyTube.")

    except Exception as e:
        print(f"Error: {e}")
        print("There is something wrong with the URL, please recheck")

def download_youtube_as_mp3(url, output_folder='downloads'):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        # Download the highest quality audio stream
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        print(f"Downloading: {yt.title}")
        downloaded_file = audio_stream.download(output_path=output_folder)

        # Convert to MP3 using moviepy
        mp3_filename = os.path.splitext(downloaded_file)[0] + '.mp3'
        print(f"Converting to MP3: {mp3_filename}")
        audio_clip = AudioFileClip(downloaded_file)
        audio_clip.write_audiofile(mp3_filename)
        audio_clip.close()

        #  Remove the original video
        os.remove(downloaded_file)
        print("Download and conversion complete.")

    except Exception as e:
        print(f"Error: {e}")
        print("There is something wrong with the URL, please recheck")

# Example usage
if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    extension_output = input("Output extension (Currently available: MP3, MP4): ")
    if extension_output == "MP3":
        download_youtube_as_mp3(video_url)
    elif extension_output == "MP4":
        download_youtube_as_mp4(video_url)
    else :
        sys.exit("The output extension is not available for now, please re-run the script and choose the available extension")
