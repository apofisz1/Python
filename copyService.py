import time, os, shutil, threading

def main (sourceFolder, destinationFolder, interval):
    print "Start.."

    print "Checkfolder"
    t1 = threading.Thread(target=checkFolder, args=[sourceFolder, destinationFolder, interval])
    t1.start()

def checkFolder(sourceFolder, destinationFolder, interval):
    while True:
        print "folder Check"
        files = [sourceFolder + i for i in os.listdir(sourceFolder) if os.path.isfile(sourceFolder + i)]

        if files:
            moveFile(destinationFolder, files)
            print "go"

        time.sleep(interval)

def moveFile(destinationFolder, fileList):
    print "Copying Files from {}...".format(destinationFolder)
    for f in fileList:
        baseName = os.path.basename(f)
        shutil.move(f, destinationFolder + baseName)


main("C:/testmappa/","C:/testmappa/1/",  3)

