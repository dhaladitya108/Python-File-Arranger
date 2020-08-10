# arranging movie by genre
from components.movie_by_genre_arranger import movieGenreArranger
from components.file_extention import fe  # file extention dictionary
import os  # getting list of files from a directory, moving files
import time  # seeing the excution time of the program
from tqdm import tqdm  # progressive bar

src = "C:/Users/Adi/Desktop/folder1/"  # files are moved from here
des = "C:/Users/Adi/Desktop/folder2/"  # files are moved here

start_time = time.time()
fl_name = os.listdir(src)
if len(fl_name) != 0:
    for file_name in tqdm(fl_name):
        fname, fextention = os.path.splitext(file_name)
        if fextention in fe.keys():
            if not os.path.exists(des+fe[fextention]):
                os.makedirs(des+fe[fextention])
            os.rename(src+file_name, des+fe[fextention]+'/'+file_name)

        elif fextention == '.mp4' or fextention == '.avi' or fextention == '.mkv':
            movieGenreArranger(src, des, fname, file_name)

        else:
            fextention = fextention[1:]
            if not(os.path.exists(des+fextention)):
                os.makedirs(des+fextention)
            os.rename(src+file_name, des+fextention+'/'+file_name)
print(time.time()-start_time)
