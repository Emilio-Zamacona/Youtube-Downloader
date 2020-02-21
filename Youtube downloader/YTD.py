from tkinter import *
from pytube import YouTube

root = Tk()
root.title("YouTube Downloader")
upperFrame = Frame(root)
upperFrame.grid(row=0,column=0)

urlList=["https://www.youtube.com/watch?v=MfmoIHY7Z-k","https://www.youtube.com/watch?v=CiCZddanoXQ"]


def newUrl(url):
	urlList.append(url)

def displayNames():
	for i in urlList:
		video = YouTube(i)
		videoName = video.title
		Label(upperFrame, text=videoName).grid(row=urlList.index(i), column=1)

displayNames()


linkBtn = Button(upperFrame, text="Añadir Link", bd=5,padx=30)
linkBtn.grid(row=0, column=0)








#video = YouTube("https://www.youtube.com/watch?v=DLbY7iTNzj4")

#video.streams.get_by_itag(248).download()

root.mainloop()