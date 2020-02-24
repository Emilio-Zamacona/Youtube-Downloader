from pytube import YouTube

link = YouTube("https://www.youtube.com/watch?v=JfEIkkDkrmE")

link.streams.filter(progressive=True).first().download()