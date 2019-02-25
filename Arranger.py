from mutagen.easyid3 import EasyID3
import os
import shutil
import re
Tags = EasyID3(Path)
if not Tags.get('album'):
    print(Tags)

path = '/Users/jthong/Desktop/Mus'
filetype ='.mp3'#指定文件类型

def get_filename(path,filetype):
    FileName =[]
    FilePath = []
    for root,dirs,files in os.walk(path):
        for i in files:
            if filetype in i:
                FileName.append(i)
                RealPath = os.path.join(root,i)
                FilePath.append(RealPath)
    return FilePath, FileName

def FileCopy(SourcePath,TargetPath,NameList):    #SourcePath:List, TargetPath = String
    Count = 0
    for i in SourcePath:
        print('Now:', i)
        Tags = EasyID3(i)
        if Tags.get('album'):
            AlName = Tags['album']
            Buf = AlName[0]
            Buf = re.sub(' [\/:*?"<>|]','-',Buf)
            PathBuffer = os.path.join(TargetPath,Buf)
            print('Processing',PathBuffer)
            if os.path.exists(PathBuffer):
                TargetBuffer = os.path.join(PathBuffer,NameList[Count])
                shutil.copyfile(i,TargetBuffer)
                #Copy File
            else:
                os.makedirs(PathBuffer)
                TargetBuffer = os.path.join(PathBuffer,NameList[Count])
                shutil.copyfile(i,TargetBuffer)
        else :
            print('Not Album',i)
            #Doing Nothing
        Count+=1
    print(Count)

PathList , FileNameList= get_filename(path,filetype)
TargetPath = '/Users/jthong/Desktop/TargetDict'
FileCopy(PathList,TargetPath,FileNameList)