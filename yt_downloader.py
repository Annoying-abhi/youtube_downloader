from sys import path_importer_cache
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil

#functions 
def select_path():
     #it allow user to select path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get user path 
    get_link = link_field.get()
    #get selected path 
    user_path = path_label.cget("text")
    screen.title('Downloading')
    #download video
    mp4_video =  YouTube(get_link).streams.get_highest_resolution().download()
    video_clip =  VideoFileClip(mp4_video)
    video_clip.close()

    #move to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download complete! Download Another file..")

screen = Tk()
title = screen.title('Youtube video downloader')
canvas = Canvas(screen, width = 500, height =  500)
canvas.pack()

#image logo

logo_img = PhotoImage(file = "ytt.png")
#resize

logo_img = logo_img.subsample(15, 15)

canvas.create_image(250,110, image = logo_img)

#link fields
link_field = Entry(screen, width = 50)
link_label = Label(screen, text = "Enter the download link: ", font = "Arial",)

#select path for saving the path
path_label = Label(screen, text = ' select path for download' ,font = " Arial",)
select_btn = Button(screen, text = 'select Path', command= select_path)
# add to screen 
canvas.create_window(230, 270, window = path_label)
canvas.create_window(230, 320, window = select_btn)

#add widgets to window 
canvas.create_window(250,200, window = link_label)
canvas.create_window(240,230, window = link_field)

#download buttons 
donwload_btn = Button(screen, text = 'Download file', command = download_file)


#add to canvas
canvas.create_window(230,360, window = donwload_btn)
screen.mainloop()