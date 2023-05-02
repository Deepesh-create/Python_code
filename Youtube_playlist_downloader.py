# youtube_playlist downloader program.
# module required :- pytube

from pytube import Playlist

# To get input of the link of the youtube playlist.
link = input("\nEnter the playlist link :")

# To get the resolution of the video that is to be downloaded.
resolution = input("\nEnter the video quality :")

# To get the path from where the playlist video is store
path = input(r"Enter the path address:")


py = Playlist(link)

#loop for downloading the individual video.
for video in py.videos:
    stream = video.streams.filter(file_extension="mp4").get_by_resolution(resolution)
    print("\nDownloading :",video.title)
    stream.download(path)
print("\nDownload sucessfully")
