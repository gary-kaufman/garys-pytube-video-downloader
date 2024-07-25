from pytubefix import YouTube
from pytubefix.cli import on_progress


def download_yt_video():

    # Insert your url
    url = "https://youtu.be/2jVBWyih-RU?si=Gne7gjpW_XlFIu5G"

    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    # Use a breakpoint on the line below and debug the program. Inspect the `itag_index` under the `streams` object.
    # I have found that the best way to get the highest quality is to download the highest video and audio separately
    # and merge them in a video editor.
    yt.streams.filter()

    # Change the parameter for the `itag` to the index that you prefer and run the program
    stream = yt.streams.get_by_itag(248)
    stream.download()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download_yt_video()
