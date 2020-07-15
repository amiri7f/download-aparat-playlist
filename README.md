# Get  Aparat PlayList Downlaod links
![](https://upload.wikimedia.org/wikipedia/commons/4/4b/Aparat_logo_%28fa%29_black_2014.png)
![python](https://fedoramagazine.org/wp-content/uploads/2015/11/Python_logo-945x400.png "python")
## How to use
To run aparat.py ;

- Install `Python3` and `pip3`
- Install requirement library
- Run aparat.py
- Run rename.py to rename files

### step 1
------------
    Install python3 and pip3

### step 2
------------
Install requirement library , `requests` and ` bs4`

    pip3 install requests bs4
    
### step 3
------------
    python3 aparat.py YourAparatUrl Quality
 
#####  Example
 python3 aparat.py https://www.aparat.com/v/x45Wr?playlist=206420 720p
######  will generate `index.html` in same Directory that contain download links

## Rename Download File in real names
##### copy rename.py in directory that contain Downloaded files and run it
    python3 rename.py YourAparatUrl QualityDownload