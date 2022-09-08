from pytube import YouTube, Playlist
from tqdm import tqdm
import sys, time
from src.cls import cls

def menu():
    while True:
        cls()
        option = input('Choose an option: \n1: Download video \n2: Download playlist \n3: Exit\n\nType here and press Enter key: ')

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
    yt = input('Paste video URL here and press Enter key: ')
    try:
        video = YouTube(yt)
    except:
        print('Invalid video URL, please try again...')
        time.sleep(3)
        menu()

    cls()
    print('Title: ' + video.title)
    option = input('Which format do you want?\n1: MP4 high-resolution \n2: MP4 low-resolution \n3: MP4 audio-only \n\nType here and press Enter key: ')

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
        print('\nError, please try again...\n')
    else: 
        print('Download complete!\n')
    time.sleep(3)
    menu()

def downloadPlaylist():
    yt = input('Paste playlist url here and press Enter key: ')
    try:
        playlist = Playlist(yt)
        playlist.title
    except:
        print('Invalid playlist URL, please try again...')
        time.sleep(3)
        menu()
    
    cls()
    print('Title: ' + playlist.title)
    option = input('Which format do you want?\n1: MP4 high-resolution \n2: MP4 low-resolution \n3: MP4 audio-only \n\nType here and press Enter key: ')

    if option not in ["1", "2", "3"]:
        print('Invalid option, please try again...')
        time.sleep(3)
        menu()

    cls()
    print(playlist.title + '\nDownloading...\n')

    try:
        if option == '1':
            for video in tqdm(playlist.videos):
                video.streams.get_highest_resolution().download()
        if option == '2':
            for video in tqdm(playlist.videos):
                video.streams.get_lowest_resolution().download()
        if option == '3':
            for video in tqdm(playlist.videos):
                video.streams.get_audio_only().download()
    except:
        print('\nError, please try again...\n')
    else: 
        print('\nDownload complete\n')
    time.sleep(3)
    menu()    

menu()
