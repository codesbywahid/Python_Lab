from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title : ", yt.title)
print("Views : ", yt.views)

yd = yt.streams.get_highest_resolution()

# Change the path below to the folder where you want the video saved
# Example (Windows): 'C:/Users/YourName/Downloads'
# Example (Mac/Linux): '/Users/YourName/Downloads'
# Or use '.' to save in the same folder as this script
yd.download('.')

# To download a video, run this in your terminal:
# python ytdownloader.py "videolink"