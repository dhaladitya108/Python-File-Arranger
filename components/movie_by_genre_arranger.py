import requests
import os


def movieGenreArranger(src, des, fname, file_name):
    url = requests.get(
        f"http://omdbapi.com/?&apikey=82f50d86", params={'t': fname})
    if not(os.path.exists(des+'video')):
        os.makedirs(des+'video')
    try:
        url_dict = url.json()
        genre = url_dict['Genre']
        genre = genre.split(',')
        genre = genre[0]
        if (os.path.exists(des+"video/"+genre)):
            os.rename(src+file_name, des+"video/"+genre+'/'+file_name)
        else:
            if genre != 'N/A':
                os.makedirs(des+"video/"+genre)
                os.rename(src+file_name, des +
                          "video/"+genre+'/'+file_name)
            else:
                os.rename(src+file_name, des+"video/"+file_name)
    except:
        os.rename(src+file_name, des+"video/"+file_name)
