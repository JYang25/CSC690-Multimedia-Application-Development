"""

File:            ImageBrowser.py
By:              Jizhou Yang
Date:            9-22-2017
Compile:         Python3 
Usage:           Python3 ImageBrowser.py Width
System:          macOS Sierra, version 10.12.6
Description:     This is a simple image browser implemented by python3 and pyqt5. It provides full screen view and 
                 thumbnail view of the images. It rescale the image as needed. Use arrow key, <, >, and mouse click
                 to browse the images. There will be sound effect when browsing the images. Tags will shown below 
                 the image. Users can also add new tags to each individual image or all images.
Data:            *** A folder named "data" that contain images has to be in the same directory as this script ***
                 *** A folder named "sounds" that contain wav files for sound effects ***
                 *** A folder named "tags" that contain all tags text files. Each tag file is for one image ***
                 *** Model.py contains the model class that store image data information ***
                 *** View.py contains the view class that provide view and control ***
                 *** ImageBrowser2.py contains the main function ***

"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QSoundEffect

class model():
    def __init__(self):
        
        
        
        self.datapath = os.getcwd() + "/data/"
        self.tagpath = os.getcwd() + "/tags/"
        self.imglist = os.listdir(self.datapath)
        self.taglist = os.listdir(self.tagpath)   
        
        # create a list to hold all img models
        self.imgs = []
        self.tags = []
        for i in range(len(self.imglist)):
            self.imgs.append(QPixmap(self.datapath + self.imglist[i]))
            fin = open(self.tagpath + self.taglist[i])
            lines = fin.read().splitlines()
            fin.close()
            self.tags.append(lines)
        
        
       
            

            
        
        
        
 