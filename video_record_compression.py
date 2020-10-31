import os 
import subprocess 
import time 
import glob


def video_recording():
    time_minutes = input("How long should the registration take? (in minutes)\n\r")
    time_seconds = int(time_minutes) * 60
    OBS_path = os.getcwd()+ r"\OBS_portable\bin\64bit"
    print("Start recording!")
    try:
        subprocess.run("obs64 --minimize-to-tray --startrecording", shell=True, cwd=OBS_path, timeout = 5)
    except subprocess.TimeoutExpired as e:
        print(e)
    time.sleep(time_seconds) 
    subprocess.run('taskkill /IM "OBS64.exe" /F')
    print("Recording stopped!\n\r")
    list_of_videos = glob.glob(os.getcwd()+'\*.mkv') # * means all, if need specific format then *.format  
    latest_video = max(list_of_videos, key=os.path.getctime)
    video_name, video_extension = os.path.splitext(latest_video)
    # Use line 1 instead of line 2 if you want to keep the compressed video in the same format as the original one 
    # output_video = video_name + "_compressed" + video_extension # line 1
    output_video = video_name + ".mp4" # line 2
    print("Starting compression!\n\r")
    # Use line 3 instead of line 4 if you want to reduce the video resolution to 720p (in the case of horizontally oriented videos)
    # subprocess.run(["ffmpeg", "-i", latest_video, "-preset", "veryfast", "-vf", "scale=-2:720", "-vcodec", "h264", "-acodec", "aac", output_video]) # line 3
    subprocess.run(["ffmpeg", "-i", latest_video, "-preset", "veryfast", "-vcodec", "h264", "-acodec", "aac", output_video]) # line 4
    os.remove(latest_video)
    print("Compression done!")
    

def video_compression():
    input_video = input("Enter the name of the video you want to compress (file extension included)!\n\r")
    video_name, video_extension = os.path.splitext(input_video)
    # Use line 1 instead of line 2 if you want to keep the compressed video in the same format as the original one 
    # output_video = video_name + "_compressed" + video_extension # line 1
    output_video = video_name + "_compressed.mp4" # line 2
    print("Starting compression!\n\r")
    # Use line 3 instead of line 4 if you want to reduce the video resolution to 720p (in the case of horizontally oriented videos)
    # subprocess.run(["ffmpeg", "-i", input_video, "-preset", "veryfast", "-vf", "scale=-2:720", "-vcodec", "h264", "-acodec", "aac", output_video]) # line 3
    subprocess.run(["ffmpeg", "-i", input_video, "-preset", "veryfast", "-vcodec", "h264", "-acodec", "aac", output_video]) # line 4
    print("Compression done!")


if __name__ == "__main__":
    while True:  
        tempvar = input("Do you want to record or compress a video? Valid: r (= record) / c (= compress)\n\r")
        if(tempvar == "r"):
            video_recording()
            break       
        elif(tempvar == "c"):
            video_compression()
            break
        else: 
            print("\n\rNot a valid command, choose again!\n\r")