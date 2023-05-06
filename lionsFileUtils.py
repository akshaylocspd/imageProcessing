# make crud functions here
import os
import json
import shutil

def readFile(filepPath):
    with open(filepPath,'r') as f:# there is no need to close this file, it creats filehandling.txt file if it is not exist
        return f.read()

def getCurrentDirPath():
    return os. getcwd() 
def writeFile(filePath,data):
    with open(filePath,'w') as f:# there is no need to close this file, it creats filehandling.txt file if it is not exist
        f.write(data)
def saveFile(filePath,data):
    with open(filePath,'wb') as f:# there is no need to close this file, it creats filehandling.txt file if it is not exist
        f.write(data)

def createFolder(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def copyFile(oldPath,newPath):
    writeFile(newPath,readFile(oldPath))

def moveFile(oldPath,newPath):
    if os.path.exists(oldPath):
        shutil.move(oldPath,newPath)

def deleteFolder(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def deleteFile(path):
    if os.path.exists(path):
        os.remove(path)


def listOfFilesInAFolder(path):
    return os.listdir(path)

def renameFile(src,dst):
    os.rename(src, dst)
    
# f=open('filePath','r') r means read mode ,w means write mode
# json_data = data)
# print(json_data)

