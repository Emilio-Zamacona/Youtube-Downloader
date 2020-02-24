from tkinter import *
from pytube import YouTube

root = Tk()
root.title("YouTube Downloader")
upperFrame = Frame(root)
upperFrame.grid(row=0,column=0)
urlsFrame = Frame(root)
urlsFrame.grid(row=0, column=1)
lowerFrame = Frame(root)
lowerFrame.grid(row=1, column=0)
infoFrame = Frame(root)
infoFrame.grid(row=1, column=1)

urlList=["https://www.youtube.com/watch?v=MfmoIHY7Z-k","https://www.youtube.com/watch?v=CiCZddanoXQ"]


def addToList(ytObject):
	urlList.append(ytObject)

def destroy(master):
	for i in master.winfo_children():
		i.destroy()


def displayNames():
	for i in urlList:
		video = YouTube(i)
		videoName = video.title
		Button(urlsFrame,text="borrar",command=lambda urlsFrame=urlsFrame, urlList= urlList, i=i:refresh(urlsFrame,urlList,i)
			).grid(row=urlList.index(i),column=2)
		Label(urlsFrame, text=videoName).grid(row=urlList.index(i), column=1)



def refresh(master, group, url):
	group.remove(url)
	destroy(master)
	displayNames()


displayNames()

Label(upperFrame,text="ingrese el link de YouTube aquí: ").grid(row=0,column=0)
urlEntry = Entry(upperFrame,width=50)
urlEntry.grid(row=0, column=1)

linkBtn = Button(upperFrame, text="Agregar a lista de descargas", bd=5,padx=0)
linkBtn.grid(row=1, column=1)


dlButton = Button(lowerFrame,text="DESCARGAR TODO")
dlButton.grid(row=0, column=0)

Label(infoFrame,text="f",pady=40).grid(row=0,column=0)




#video = YouTube("https://www.youtube.com/watch?v=DLbY7iTNzj4")

#video.streams.get_by_itag(248).download()

root.mainloop()