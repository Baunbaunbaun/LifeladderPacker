from datetime import datetime
import os

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

saveFile('chr er god','pack')
saveFile('chr er god','freight')