import shutil
import urllib.request as request
from contextlib import closing

def download(filename):
    with closing(request.urlopen("ftp://username:password@ftp.example.com/"+filename)) as r:
        with open('C:/MyPath/recievingfolder/'+filename,'wb') as f:
            shutil.copyfileobj(r, f)

files = ["file.mp3", "fild1.html"]
for file in files:
    download(file)


