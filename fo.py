from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("./") if isfile(join("./", f))]

##
imagefileextensions = []
videofileextensions = []
codefileextensions = []
images = []
videos = []
code = []
##
extensiontype = [imagefileextensions, videofileextensions, codefileextensions]
##

def initSorting():
    with open("fileextensions.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            if stripped_line == '-':



def sortfiles():
    for file in onlyfiles:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            images.append(file)

initSorting()
sortfiles()
