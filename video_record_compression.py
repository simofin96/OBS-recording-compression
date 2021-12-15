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
    video_compression(latest_video)


def video_compression(input_video):
    start_time = time.time() 
    input_video_array = input_video.split('"')
    if len(input_video_array) == 1:
        video_name, video_extension = os.path.splitext(input_video_array[0])
        # Use line 2 instead of line 1 if you want the compressed video to be always in mp4 format 
        output_video = video_name + "_compressed" + video_extension # line 1
        # output_video = video_name + "_compressed.mp4" # line 2
        print("Starting compression!\n\r")
        # Use line 4 instead of line 3 if you want to reduce the video resolution to 720p (in the case of horizontally oriented videos)
        subprocess.run(["ffmpeg", "-i", input_video_array[0], "-preset", "veryfast", "-vcodec", "h264", "-acodec", "aac", output_video]) # line 3
        # subprocess.run(["ffmpeg", "-i", input_video_array[0], "-preset", "veryfast", "-vf", "scale=-2:720", "-vcodec", "h264", "-acodec", "aac", output_video]) # line 4
    else:
        counter = 0
        while(counter < len(input_video_array)):
            video_name, video_extension = os.path.splitext(input_video_array[counter])
            if(len(video_extension) != 0):
                # Use line 2 instead of line 1 if you want the compressed video to be always in mp4 format 
                output_video = video_name + "_compressed" + video_extension # line 1
                # output_video = video_name + "_compressed.mp4" # line 2
                print("Starting compression!\n\r")
                # Use line 4 instead of line 3 if you want to reduce the video resolution to 720p (in the case of horizontally oriented videos)
                subprocess.run(["ffmpeg", "-i", input_video_array[counter], "-preset", "veryfast", "-vcodec", "h264", "-acodec", "aac", output_video]) # line 3
                # subprocess.run(["ffmpeg", "-i", input_video_array[counter], "-preset", "veryfast", "-vf", "scale=-2:720", "-vcodec", "h264", "-acodec", "aac", output_video]) # line 4
            counter += 1
    time_required = round(time.time()) - round(start_time)
    if time_required < 60:
        print("Compression done!\n--- %s seconds required ---" %time_required)
    else:
        minutes = time_required // 60
        seconds = time_required - (minutes * 60)
        print("Compression done!\n--- " + str(minutes) + " minutes and " + str(seconds) + " seconds required ---")


if __name__ == "__main__":
    while True:  
        tempvar = input("Do you want to record or compress a video? Valid: r (= record) / c (= compress)\n")
        if(tempvar == "r"):
            video_recording()
            break       
        elif(tempvar == "c"):
            input_video = input("Drag and drop here the videos you want to compress, or just enter their paths (file extension included)!\n")
            if len(input_video) != 0:
                video_compression(input_video)
                break
            else:   
                print("No valid path has been entered! Choose again.\n")
        else: 
            print("Not a valid command! Choose again.\n")