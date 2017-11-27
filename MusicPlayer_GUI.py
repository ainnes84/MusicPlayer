import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *

root = Tk()
root.minsize(300,300)

listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root, textvariable = v, width = 35)

index = 0

def playsong(event):
    global index
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()

def updatelabel():
    global index
    v.set(realnames[index])

def endprogram(event):
    root.destroy()
    
def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(files)
            
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()

directorychooser()
label = Label(root, text = 'Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()


playbutton = Button(root, text = 'Play', bg = 'green', fg = 'white')
playbutton.pack()

nextbutton = Button(root, text = 'Next Song', bg = 'blue', fg = 'white')
nextbutton.pack()

previousbutton = Button(root, text = 'Previous Song', bg = 'orange', fg = 'white')
previousbutton.pack()

stopbutton = Button(root, text = 'Stop', bg = 'red', fg = 'white')
stopbutton.pack()

destroybutton = Button(root, text = 'Close Program', font = ('Arial', 12, 'bold'), bg = 'black', fg = 'red')
destroybutton.pack()

playbutton.bind("<Button-1>",playsong)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
destroybutton.bind("<Button-1>",endprogram)

songlabel.pack()


root.mainloop()
