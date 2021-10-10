from youtube_dl import YoutubeDL


while True:
    try:
        print("Youtube Downloader".center(40, "_"))
        URL = input("Enter youtube url: ")
        
        # Get video title
        info_dict = YoutubeDL().extract_info(URL, download=False)
        
        # Assign 'm4a' format and set directory for downloaded videos
        ydl_options = {
            'format': 'm4a',
            'outtmpl': f'./downloaded_videos/{info_dict["title"]}.m4a',
    
        }

        with YoutubeDL(ydl_options) as ydl:
            ydl.download([URL])
    
    except Exception:
        print("Couldn't download the audio")
    finally:
        option = int(input("\n1. Download\n2.Exit\n\nOption here: "))
        if option != 1:
            break

