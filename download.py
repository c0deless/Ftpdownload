import shutil
import urllib.request as request
from contextlib import closing

def download(filename):
    with closing(request.urlopen("ftp://BUZZ:NotMyPassword@ftp.usaradio.com/"+filename)) as r:
        with open('C:/MyPath/usanews/'+filename,'wb') as f:
            shutil.copyfileobj(r, f)

files = ["newsbreak128.mp3", "toh35.mp3"]
for file in files:
    download(file)


