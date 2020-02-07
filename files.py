"""
from datetime import datetime
from tkinter import filedialog
import os
from tkinter import *

root = Tk()
root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

def saveFile(content, type):
    os.chdir('/Users/baunbaun/desktop')
    title = type+'-'+str(datetime.now())[:19]
    title = title.replace(":","h",1)
    title = title.replace(":","m",1)
    title = title+"s"
    title += '.txt'
    print(title)
    f = open(title, "x")
    f.write(content)
    f.close()


filedialog.asksaveasfile()
"""

#saveFile('chr er god','pack')
#saveFile('chr er god','freight')