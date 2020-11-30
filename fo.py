import os
import shutil
from os import listdir
from os.path import isfile, join
files = [f for f in listdir("./") if isfile(join("./", f))]

imagefileextensions = []
videofileextensions = []
codefileextensions = []
images = []
videos = []
code = []

def initSorting():
    with open("fileextensions.txt", "r") as fileextensions:
        for line in fileextensions:
            stripped_line = line.strip()
            if stripped_line == "Images":
                if not os.path.exists("Images"):
                    os.mkdir("Images")
                    shutil.move('./Images/','')


def sortfiles():
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            if not os.path.exists("./Images"):
                os.mkdir("Images")
                shutil.move('./asd.txt', './Images/asd.txt')
            else:
                shutil.move('asd.txt', 'Images/asd.txt')

sortfiles()
