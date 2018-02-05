from youtube_dl import YoutubeDL

options = {
    "default_search": "ytsearch", # tell downloader to search instead of directly downloading
    "max_downloads": 1, # Tell downloader to download only the first entry (audio)
}
dl = YoutubeDL(options)
dl.download(["dạy cac con vật hay nhất"])
