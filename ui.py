#!/bin/python
import tkinter as tk
import requests
import os
import CatalogParsingClass

#http://is2.4chan.org/g/
BASE_IMAGE_URL = 'http://is2.4chan.org/g/'

def load_pls():
	num = li.curselection()[0]
	lab0['text'] = str(thread_list[num][0])+ '\n' + str(thread_list[num][1])+ '\n' + str(thread_list[num][3]) + '\n' + str(thread_list[num][2])
	url_to_image = BASE_IMAGE_URL + str(thread_list[num][6]) + str(thread_list[num][7])
	print(url_to_image)
	data = requests.get(url_to_image)
	filedir = '/tmp/img' + str(thread_list[num][7])
	print(filedir)
	f = open(filedir, 'wb')
	f.write(data.content)
	f.close()
	comman = 'ffmpeg -i /tmp/img' + str(thread_list[num][7] + ' -s 300x300 out.gif')
	print(comman)
	os.system(comman)
	imbox.config(file='/tmp/out.gif')
	lab.config(image=imbox) 

root = tk.Tk()
li = tk.Listbox(root)
li.pack(fill=tk.Y)
but = tk.Button(root, text="Load", command=load_pls)
but.pack()
cpc = CatalogParsingClass.CatalogParsingClass('g')
thread_list = []

for i in range(cpc.return_number_of_total_threads()):
	thread_list.append(cpc.return_thread_parsed(i))
	li.insert(tk.END, thread_list[i][2][:30])

x = 1
lab = tk.Label(root)
lab.pack()

lab0 = tk.Message()
lab0.pack()

imbox = tk.PhotoImage()


root.mainloop()