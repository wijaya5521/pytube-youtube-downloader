from pytube import YouTube
from pytube import request
from pytube.cli import on_progress
from Functions import convert_time


request.default_range_size = 1024

url = input("Paste youtube link here : ")
yt = YouTube(url, on_progress_callback=on_progress)
streams = yt.streams
title = yt.title
channel = yt.author
duration = convert_time(yt.length)

print("="*70)
print(f"Title : {title}" )
print(f"Channel : {channel}")
print(f"Duration : {duration}")
print("-"*70)

choose_type = input("Download video (v) or audio only? (a) : ")
if choose_type == "v" :
    while True:
        resolution = input('''Resolution :
1. 144p
2. 240p
3. 360p
4. 480p
5. 720p
6. 1080p

Choose resolution or (q) to quit : ''')
        try:
            match(resolution):
                case "1" : 
                    video = streams.get_by_resolution('144p').first()
                    video.download(output_path=r"C:\Users\HP 520\Downloads\Video")
                case "2" : 
                    video = streams.get_by_resolution('240p').first()
                    video.download(output_path=r"C:\Users\HP 520\Downloads\Video")
                case "3" : 
                    video = streams.get_by_resolution('360p').first()
                    video.download(output_path=r"C:\Users\HP 520\Downloads\Video")
                case "4" : 
                    video = streams.get_by_resolution('480p').first()
                    video.download(output_path=r"C:\Users\HP 520\Downloads\Video")
                case "5" : 
                    video = streams.get_by_resolution('720p').first()
                    video.download(output_path=r"C:\Users\HP 520\Downloads\Video")
                case "6" : 
                    video = streams.get_by_resolution('1080p').first()
                    video.download(output_path=r"C:\Users\HP 520\Downloads\Video")
                case "q" : break
            break
        except:
            print(f"Resolusi video yang dipilih tidak tersedia, silakan pilih resolusi lainnya\n")

if choose_type == "a" :
    while True:
        bitrate = input('''Bitrate :
1. 48 kbps
2. 70 kbps
3. 128 kbps
4. 160 kbps

Choose bitrate or (q) to quit : ''')
        try:
            match(bitrate):
                case "1" : 
                    audio = streams.filter(only_audio=True,abr="48kbps").first()
                    audio.download(output_path=r"C:\Users\HP 520\Downloads\Music")
                case "2" : 
                    audio = streams.filter(only_audio=True,abr="70kbps").first()
                    audio.download(output_path=r"C:\Users\HP 520\Downloads\Music")
                case "3" : 
                    audio = streams.filter(only_audio=True,abr="128kbps").first()
                    audio.download(output_path=r"C:\Users\HP 520\Downloads\Music")
                case "4" : 
                    audio = streams.filter(only_audio=True,abr="160kbps").first()
                    audio.download(output_path=r"C:\Users\HP 520\Downloads\Music")
                case "q" : break
            break
        except:
            print(f"Bitrate tidak tersedia, silakan pilih bitrate lain")
    