from pytube import YouTube, Playlist
import sys, time
from src.cls import cls

def menu():
    while True:
        cls()
        option = input('Do you want to...\n1: Download video \n2: Download playlist \n3: Exit\n\nType here and press Enter key: ')

        if option == '1':
            downloadVideo()
        elif  option == '2':
            downloadPlaylist()
        elif option == '3':
            print('Exiting...')
            time.sleep(3)
            sys.exit()
        else:
            print('Invalid option, please try again...')
            time.sleep(3)

def downloadVideo():
    yt = input('Paste video url here and press Enter key: ')
    video = YouTube(yt)

    cls()
    print('Title: ' + video.title)
    option = input('What format do you want?\n1: MP4 high-resolution \n2: MP4 low-resolution \n3: MP4 audio-only \n\nType here and press Enter key: ')

    if option == '1':
        video = video.streams.get_highest_resolution()
    elif option == '2':
        video = video.streams.get_lowest_resolution()
    elif option == '3':
        video = video.streams.get_audio_only()
    else:
        print('Invalid option, please try again...')
        time.sleep(3)
        menu()
    
    cls()
    print(video.title + '\nDownloading...\n')

    try:
        video.download()
    except:
        print('Error, please try again...\n')
    else: 
        print('Download complete!\n')
    time.sleep(3)
    menu()

def downloadPlaylist():
    yt = input('Paste playlist url here and press Enter key: ')
    playlist = Playlist(yt)

    cls()
    print(playlist.title + '\nDownloading...\n')

    try:
        for video in playlist.videos:
            video.streams.first().download()
    except:
        print('Error, please try again...\n')
    else: 
        print('Download complete!\n')
    time.sleep(3)
    menu()
    
menu()
