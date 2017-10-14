#!/usr/bin/python3

# Customize your error message
str_exp = 'Python greeting not working'

from ansi.colour import rgb
from PIL import Image

import os, sys, magic
import numpy as np


def get_image(fname):
    """Open image and format it correctly
    :param fname: path of the image
    :type fname: str
    """
    my_img = Image.open(fname)
    data   = my_img.getdata()
    s1, s2 = my_img.size
    return np.array(list(data)).reshape((s2,s1,4)).astype(int)

def img_to_colorcode(img):
"""
    :param img: Image to process
    :type img: np.array, dim=(s1,s2,4)
    """
    s1, s2  = img.shape[:2]
    col_mat = np.zeros((s1, s2)).astype(str)

    for idx, i in enumerate(img):
        r = np.array([-1,-1,-1,-1])
        for jdx, j in enumerate(i):
            if (j == np.array(r)).all() :
                col_mat[idx][jdx] = ""
            else :
                col_mat[idx][jdx] = rgb.rgb256(j[0], j[1], j[2])
                r = j

    # remove background
    A,B = np.where(img[:,:,3] == 0)
    for a,b in zip(A,B):
        if col_mat[a][b] != '':
            col_mat[a][b] = '\x1b[49m'
    return col_mat

def mat_to_string(mat):
    """Convert a matrice of colorcodes to printable str
    """
    my_str = ""
    for row in mat:
        my_str += '  '.join(row).replace("\x1b", '\e') + ' \e[30;30m \\n'

    return my_str.replace('[38;', "[48;")


try :


    amax = int(sys.argv[1]) //2
    
    # change me, better to take absolute path !!
    Path = '/PATH/TO/FOLDER/Poke/'
    files = os.listdir(Path)

    # Get resolution of images, and keep only the one with size lower than the width of the terminal
    flst = np.array(files)[np.array(list(map(lambda x: int(magic.from_file(Path + x).split()[3]), files))) <= amax]
    l = len(flst)

    i = np.random.randint(0, l)
    fname = Path + flst[i]

    img     = get_image(fname)
    col_mat = img_to_colorcode(img)
    str_exp = mat_to_string(col_mat)

except:
    # Error in the script, avoid big warning
    str_exp = ""
    pass

with open("str_img.txt", 'w') as fp:
    fp.write(str_exp)
