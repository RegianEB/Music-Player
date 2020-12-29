import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer= tkr.Tk();

musicplayer.title("music player")

musicplayer.geometry("450x350")

directory=askdirectory()

os.chdir(directory)

songlist=os.listdir()

playlist = tkr.Listbox(musicplayer,font="Canbira 14 bold", bg="cyan", selectmode=tkr.SINGLE)
for item in songlist:
    pos=0
    playlist.insert(pos, item)#memasukkan item ke playlist
    pos = pos+1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():#untuk pause
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()


Button_play = tkr.Button(musicplayer, height=3, width=5, text="Play Music", font="Cambriac 14 bold", command=play, bg="lime green",fg="black")
Button_Exit = tkr.Button(musicplayer, height=3, width=5, text="Stop music", font="Cambriac 14 bold", command=ExitMusicPlayer, bg="red",fg="black")
Button_pause = tkr.Button(musicplayer, height=3, width=5, text="Pause Music", font="Cambriac 14 bold", command=pause, bg="green",fg="black")
Button_resume = tkr.Button(musicplayer, height=3, width=5, text="Resume Music", font="Cambriac 14 bold", command=resume, bg="pink",fg="black")

Button_play.pack(fill="x")
Button_Exit.pack(fill="x")
Button_pause.pack(fill="x")
Button_resume.pack(fill="x")

playlist.pack(fill="both", expand="yes")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Cambria 12 bold", textvariable=var)
songtitle.pack()
musicplayer.mainloop()