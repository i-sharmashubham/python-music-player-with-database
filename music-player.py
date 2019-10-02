import os
import pygame
from tkinter.filedialog import askdirectory
from tkinter import *
from mutagen.id3 import ID3
import mysql.connector

mydb = mysql.connector.connect(
  host="INSERT_HOST_NAME_HERE",
  user="INSERT_USERNAME_HERE",
  passwd="INSERT_PASSWORD_HERE",
  database="ENTER DATABASE NAME HERE"
)

mycursor = mydb.cursor()

root = Tk()
root.configure(background='black')
root.wm_iconbitmap('icon.ico')
root.title('Music Player')
root.minsize(800,500)

playlist = []
musicname = []
index = 0
v=StringVar()
songlabel=Label(root,textvariable=v,fg = 'white',bg = 'black')

def addsong(event):
    directory=askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
         if files.endswith(".mp3"):
          realdir=os.path.realpath(files)
          audio=ID3(realdir)
          name=audio["TIT2"].text[0]
          mycursor.execute("INSERT INTO musiclist(path, name) VALUES(%s,%s)",(realdir,name))
          mydb.commit() 

    loadsong()

def clearsong(event):
    global playlist,musicname,index,v
    mycursor.execute("TRUNCATE musiclist")
    playlist = []
    musicname = []
    index = 0
    v.set("")
    loadsong()
    stopsong(event)

def playsong(event):
    global index
    if playlist:
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()
        updatelabel()

def nextsong(event):
    global index
    if playlist:
        if index == len(playlist) - 1:
            index = -1
        index+=1
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()
        updatelabel()

def previoussong(event):
    global index
    if playlist:
        if index == 0:
            index = len(playlist)
        index-=1
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()
        updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

def updatelabel():
    global index
    v.set('Now Playing : '+musicname[index])


addbutton=Button(root,text="ADD SONGS", width = 13, bg = 'blue')
addbutton.place(x=660,y=40)
addbutton.bind("<Button-1>",addsong)

addbutton=Button(root,text="CLEAR PLAYLIST", width = 13, bg = 'red')
addbutton.place(x=660,y=100)
addbutton.bind("<Button-1>",clearsong)

playbutton=Button(root,text="PLAY SONG", width = 13, bg = 'green')
playbutton.place(x=40,y=430)
playbutton.bind("<Button-1>",playsong)

nextbutton=Button(root,text="NEXT SONG", width = 13, bg = 'orange')
nextbutton.place(x=250,y=430)
nextbutton.bind("<Button-1>",nextsong)

previousbutton=Button(root,text="PREVIOUS SONG", width = 13, bg = 'orange')
previousbutton.place(x=450,y=430)
previousbutton.bind("<Button-1>",previoussong)

stopbutton=Button(root,text="STOP SONG", width = 13,bg='red')
stopbutton.place(x=650,y=430)
stopbutton.bind("<Button-1>",stopsong)

myplaylist = Message(root, text = 'My Playlist',fg = 'white',bg = 'black')
myplaylist.place(x=40,y=10)

def loadsong():
    global playlist,musicname
    listbox=Listbox(root,width = 100, height = 20, bg = 'skyblue')
    i=0
    mycursor.execute("SELECT * FROM musiclist")
    for music in mycursor:
        i+=1
        listbox.insert(i,music[2])
        playlist.append(music[1])
        musicname.append(music[2])
    if mycursor.rowcount < 0:
        listbox.insert(0,'Your Playlist is empty, please add some songs to your playlist')
    listbox.place(x=30,y=40)

    pygame.mixer.init()

loadsong()

songlabel.place(x=50,y=385)

render = PhotoImage(file='music.png')
img = Label(root, image=render, bg = 'black')
img.image = render
img.place(x=675, y=200)

root.mainloop()
