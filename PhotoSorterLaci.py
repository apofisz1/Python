# -*- coding:Utf-8 -*-

import os, shutil, time
from PIL import Image, ExifTags
from datetime import datetime
print " Give me the from folder path:\n(forexample: C:\Users\\asdasd\Desktop\hőön) "
userInputFrom = raw_input().decode("utf-8")
print userInputFrom
folder = userInputFrom.replace("\\", "/") + "/"
#print folder


print "Give me the destination folder path:"
userInputDest = raw_input().decode("utf-8")
destFolder = userInputDest.replace("\\", "/") + "/"
# print destFolder
# time.sleep(5)


# get all .jpg files in folder
files = [folder + i for i in os.listdir(folder) if i.lower().endswith(".jpg")]


for i in files:
    # get date from file
    timestamp = os.path.getmtime(i)
    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

    # load photo into Image module
    img = Image.open(i)

    # get exif data
    exifData = img._getexif()

    # if exif data and type is dictionary
    if exifData and type(exifData) == dict:

        # iterate on dictionary
        for key, value in exifData.items():

            # check if tag in ExifTags
            if key in ExifTags.TAGS:
                #print ExifTags.TAGS[key], value # if you want to change


                # we need only eiftags value value
                if ExifTags.TAGS[key] == "DateTimeOriginal":

                    # create folders with ISO value
                    if not os.path.exists(destFolder + date):
                        os.mkdir(destFolder + date)

                    # copy files
                    sourceFileName = os.path.basename(i)
                    shutil.copy2(i, destFolder + date + "/" + sourceFileName)