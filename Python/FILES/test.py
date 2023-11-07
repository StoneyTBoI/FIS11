# FILEPATH: /C:/Users/Stoney/Desktop/FIS11/Python/FILES/yt_dlp_gui.py

import tkinter as tk
import yt_dlp
import tkinter.ttk as ttk

class YTDLP_GUI:
    def __init__(self, master):
        self.master = master
        master.title("yt-dlp GUI")

        # URL input field
        self.url_label = tk.Label(master, text="Enter video URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        self.progress_bar.pack()

    def download(self):
        url = self.url_entry.get()
        format = self.format_var.get()
        ydl_opts = {
            'format': format,
            'progress_hooks': [self.update_progress],
            'outtmpl': 'C:/Users/Stoney/Desktop/FIS11/Python/FILES/%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def update_progress(self, d):
        if d['status'] == 'downloading':
            self.progress_bar['value'] = d['_percent_str']
            self.master.update_idletasks()

root = tk.Tk()
gui = YTDLP_GUI(root)
root.mainloop()
