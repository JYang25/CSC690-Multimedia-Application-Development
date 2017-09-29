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
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QSoundEffect


# import the model class from Model.py
from Model import model 

# import the view class from View.py
from View import view 

def Usage():
    print("Usage: Python3 ImageBrowser.py Width")
    print("If width is not provided, default width will be used.")
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    imgmodel = model()
    # view the models
    defaultWidth = 800
    if len(sys.argv) == 1:
        ImgView = view(imgmodel, defaultWidth)
    elif len(sys.argv) == 2:
        ImgView = view(imgmodel, sys.argv[1])
    else:
        Usage()
        exit()
    
    sys.exit(app.exec_())