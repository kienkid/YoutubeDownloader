# 🎬 YouTube Downloader

This Python project allows you to download YouTube videos via URL and convert them to either **MP3** (audio only) or **MP4** (video with audio). It's ideal for saving music, podcasts, lectures, or any video content for offline use.

---

## 📦 Requirements

Make sure you have Python installed, then install the required packages:

```bash
pip install pytubefix moviepy==1.0.3
```
## 🚀 How to Use

```bash
python YoutubeDownloader.py
```

Enter the YouTube video URL when prompted.

Enter the desirable extension (Now supporting MP3 and MP4)

The video is saved in the downloads/ folder.

## 📄 License

This project is open-source and free to use. Attribution appreciated but not required.

## ⚠️ Notes

To handle YouTube's frequent backend changes that lead to pytubefix lib broke. I will update backup function using (yt-dlp) lib function in the future
