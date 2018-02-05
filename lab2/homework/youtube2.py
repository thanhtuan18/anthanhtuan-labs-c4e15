import pyexcel
song_list = pyexcel.get_records(file_name="itunes.xlsx")

from youtube_dl import YoutubeDL

for song in song_list:
    options = {
        "default_search": "ytsearch",
        "max_downloads": 1
    }
    dl = YoutubeDL(options)
    dl.download([song["Song's name"] + " " + song["Artist"]])
