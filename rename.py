import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from sys import argv


os.chdir(os.getcwd+"/")
# Extract Download Link
def mylinks(Downlink,DException):
    mainpage=urlparse(Downlink)
    website="{}://{}".format(mainpage[0],mainpage[1])
    al0=BeautifulSoup(requests.get(Downlink).content,features="html.parser")
    na=al0.title.string
    na=na.replace("\n","")
    na=na.replace("        ","")
    na=na.replace("--","")
    al=al0.find_all('a')
    li=[]
    for i in al:
        li.append(i.get("href"))
    newlist=[]
   
    for i in li:
        if None == i:
            continue
        elif DException in i:
            if list(i)[0] == '/':
                newlist.append("{}{}".format(website,i))
            else:
                newlist.append(i)
    newlist.sort()
    return newlist,na

# aparat play list link 
def aparatPlayList(AparatUrl):
    li=BeautifulSoup(requests.get(AparatUrl).content,"html.parser").find_all('a')
    li2=[]
    for i in li:
        li2.append(i.get('href'))
    myli=[]
    for i in li2:
        if "?" in i and list(i)[1]== 'v':
            myli.append("https://www.aparat.com{}".format(i).split("?")[0])
    # remove dublicated item
    myli = list(dict.fromkeys(myli))
    return myli

playlistsurls=(aparatPlayList(argv[1]))
quality=argv[2]

# Rename files
for i in playlistsurls:
    fin=mylinks(i,quality)
    # Download link
    tmp=fin[0][0]
    t=tmp.split('/')
    # Name of Download link
    nam=fin[1]
    print(t[-1])
    print(nam+'.mp4')
    oldn=t[-1]
    newn=nam+'.mp4'
    os.renames(oldn,newn)
  
