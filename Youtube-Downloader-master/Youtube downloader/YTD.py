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

yt_list=[]

def addToList():
	url=urlEntry.get()
	urlEntry.delete(0,END)
	ytObj = YouTube(url)
	yt_list.append(ytObj)
	displayNames()

def destroy(master):
	for i in master.winfo_children():
		i.destroy()


def displayNames():
	for i in yt_list:
		videoName = i.title
		Button(urlsFrame,text="borrar",command=lambda urlsFrame=urlsFrame, yt_list=yt_list, i=i:refresh(urlsFrame,yt_list,i)
			).grid(row=yt_list.index(i),column=2)
		Label(urlsFrame, text=videoName).grid(row=yt_list.index(i), column=1)



def refresh(master, group, obj):
	group.remove(obj)
	destroy(master)
	displayNames()

def download_all():
	for i in yt_list:
		i.streams.filter(progressive=True).first().download()



Label(upperFrame,text="ingrese el link de YouTube aquí: ").grid(row=0,column=0)
urlEntry = Entry(upperFrame,width=50)
urlEntry.grid(row=0, column=1)

linkBtn = Button(upperFrame, text="Agregar a lista de descargas",command=lambda:addToList(), bd=5,padx=0)
linkBtn.grid(row=1, column=1)


dlButton = Button(lowerFrame,text="DESCARGAR TODO",command=lambda:download_all())
dlButton.grid(row=0, column=0)

Label(infoFrame,text="f",pady=40).grid(row=0,column=0)




#video = YouTube("https://www.youtube.com/watch?v=DLbY7iTNzj4")

#video.streams.get_by_itag(248).download()

root.mainloop()