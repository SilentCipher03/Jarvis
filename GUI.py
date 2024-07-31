from tkinter import *
from PIL import Image, ImageTk, ImageSequence 
import time 
import pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("2000x1000") # Size of your screen 

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img 
    img = Image.open("C:/Users/Lenovo/Documents/Ironman.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("C:\\Users\\Lenovo\\Desktop\\Music\\Scam_1992_Theme_Music(128k).mp3")
    mixer.music.play()
    for img in ImageSequence.Iterator(img):
        img = img.resize((2000,1000))
        img = ImageTk.PhotoImage(img)
        lbl.config(image = img)
        root.update()
        time.sleep(0.5)
    root.destroy()

play_gif()
root.mainloop

