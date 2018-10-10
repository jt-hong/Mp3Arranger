from mutagen.easyid3 import EasyID3
import os
import shutil
Path = '/Users/jthong/Desktop/Arranger/01、对你的思念.mp3'
Tags = EasyID3(Path)
print(Tags['album'])

path = '/Users/jthong/Desktop/Mus'
filetype ='.mp3'#指定文件类型

def get_filename(path,filetype):
    FileName =[]
    FilePath = []
    for root,dirs,files in os.walk(path):
        for i in files:
            if filetype in i:
                RealPath = os.path.join(root,i)
                FilePath.append(RealPath)
    return FilePath  

def FileCopy(SourcePath,TargetPath):    #SourcePath:List, TargetPath = String
    for i in SourcePath:
        Tags = EasyID3(Path)
        if Tags['album']:
            PathBuffer = os.path.join(TargetPath,Tags['album'])
            if os.path.exists(PathBuffer):
                #Copy File
            else:
                os.makedirs(PathBuffer)
        else :
            #Doing Nothing

PathList = get_filename(path,filetype)
print(EasyID3(PathList[7]))