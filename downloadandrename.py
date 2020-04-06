import shutil
import urllib.request as request
from contextlib import closing

def download(filename):
    with closing(request.urlopen("ftp://username:password@ftp.example.com/"+filename)) as r:
       with open('C:/MyPath/recievingfolder/'+filename[1],'wb') as f:
            shutil.copyfileobj(r, f)

files = [("file.mp3","new_name_1.mp3"), ("filed.html","new_name_1.html")]
for file in files:
    download(file)
