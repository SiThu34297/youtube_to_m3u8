from pytubefix import YouTube
import os
import shlex
import shutil

def download(link):
    youtube_object = YouTube(link)
    yt = youtube_object.streams.filter(only_audio=True).get_by_itag(251)

    newpath = 'audios/' + yt.title

    if os.path.exists(newpath + '.zip'):
        return True,newpath + '.zip',newpath + '.zip'

    if not os.path.exists(newpath):
        os.makedirs(newpath)
        os.makedirs(newpath + "/track1")

    try:
        audio = yt.download(output_path=newpath)
    except:
        print("An error has occurred")
        raise

    print("Download is completed successfully")
    mp3_path = shlex.quote(newpath + "/" + yt.title + ".mp3")
    webm_path = shlex.quote(audio)

    os.system("ffmpeg -i %s -vn -ab 320k -ar 44100 -y %s"%(webm_path,mp3_path))
    print("Convert is completed successfully")

    # delete webm file
    os.unlink(audio)

    # segement file
    input_path = mp3_path
    master_path = shlex.quote(newpath + "/track1/track1.m3u8")
    segement_path = shlex.quote(newpath + "/track1/track1_%05d.ts")

    os.system("ffmpeg -i %s -vn -ac 2 -acodec aac  -f segment -segment_format mpegts -segment_time 10  -segment_list %s %s"%(input_path,master_path,segement_path))
    print("segment_format is completed successfully")

    # zip folder
    if(__name__ == "__main__"):
        print("archive is completed successfully")
        shutil.make_archive(newpath, 'zip', newpath)
        return

    print("archive is completed successfully and return")
    return False,shutil.make_archive(newpath, 'zip', newpath), newpath



if __name__ == "__main__" : 
    link = input("Enter the YouTube video URL: ")
    download(link)
