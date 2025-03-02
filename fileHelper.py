'''
This document mainly deals with files other than "Python" files.
---Author: Season
---Language: Python
---Signature: S and A
              PHJsi
#############
#####---#####
###--   --###
#--S and A--#
###--   --###
#####---#####
#############
~~~~~~~~~~~~~
#############
#####---#####
###--   --###
#---PHJsi---#
###--   --###
#####---#####
#############
'''





import cv2
import numpy as np
import os



def cv_imread(file_path) -> list:
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    return cv_img

def numberOfRows(filePath,lineStart = 0,intLineStart = 0,strLineStart = "") -> list:
    intLine = intLineStart
    line = 0
    strLine = strLineStart
    for thisLine,thisStrLine in enumerate(filePath,lineStart):
        intLine += 1
        line = thisLine
        strLine = thisStrLine
    return [intLine,line,strLine]


'''
class OpenFunction:
    def __init__(self) -> None:
        self.function = {"cv_imread","numberOfRows"}
        self.explain = "Automatically use \"open\" to get the path when calling the function"
 
    def cv_imread(self,filepath = __file__) -> list:
        file_path = open(filepath,"r")
        cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_COLOR)
        return cv_img

    def numberOfRows(self,filepath,lineStart = 0,intLineStart = 0,strLineStart = "") -> list:
        file_path = open(filepath,"r")
        intLine = intLineStart
        line = 0
        strLine = strLineStart
        for thisLine,thisStrLine in enumerate(file_path,lineStart):
            intLine += 1
            line = thisLine
            strLine = thisStrLine
        return [intLine,line,strLine]

    def get_functionSet(self) -> set:
        return self.function

    def __str__(self) -> str:
        return self.explain
'''

class File:
    def __init__(self,pathName:str,mode:str = "a+") -> None:
        self.path = open(pathName,mode)
        self.pathName = pathName
    
    def changeMode(self,mode:str = "a+") -> None:
        self.path = open(self.pathName,mode)
    
    def get_list(self) -> list:
        return [self.path,self.pathName]
    
    def end(self) -> None:
        self.path.close()
    

    class ChangeFileSuffix:
        def __init__(self,pathName:str) -> None:
            self.pathName = pathName
            self.mode = {"pathName":0,"newPathName":1}
        
        def run(self,suffix:str) -> None:
            ext = os.path.splitext(self.pathName)
            new_name = ext[0] + suffix
            os.rename(self.pathName, new_name)
            self.newPathName = ext[0] + suffix
        
        def open(self,mode:int = 0,encoding ="utf-8"):
            if mode == 0:
                return open(self.pathname,encoding = encoding)
            elif mode == 1:
                return open(self.newPathName,encoding = encoding)





if __name__ == "__main__":
    print("Welcome to my library: fileReader.py!")
