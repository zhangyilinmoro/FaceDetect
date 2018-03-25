# -*- coding: utf-8 -*-

"""
Module implementing ReadCam.
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2
from Ui_ReadCam import Ui_Dialog


global file_name
file_name = ''

#qpiximg = QPixmap()
#qpiximgGray = QPixmap()
class MyThread(QThread):
    #signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.flag = 1
        self.delay = 1000
    def run(self):
        face_cascade = cv2.CascadeClassifier('H:\study\pyqt5\ReadCam\haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier("H:\study\pyqt5\ReadCam\haarcascade_eye.xml")

        cap = cv2.VideoCapture(file_name)
        while(cap.isOpened()):
            if(self.flag == 1):
                ret, frame = cap.read()
                img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = img_rgb.shape
                imgGray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY);  
                
                
                faces = face_cascade.detectMultiScale(imgGray, 1.3, 5)
                
                for (x,y,w,h) in faces:
                    img_rgb = cv2.rectangle(img_rgb,(x,y),(x+w,y+h),(255,0,0),2)
                    imgGray = cv2.rectangle(imgGray,(x,y),(x+w,y+h),(255,0,0),2)
                    '''face_roi = imgGray[x:x+w, y:y+h]
                    eyes = eye_cascade.detectMultiScale(face_roi,1.03,5,0,(30,30)) 
                    for (ex,ey,ew,eh) in eyes:
                        img_rgb = cv2.rectangle(img_rgb, (ex+x,ey+y), (ex+x+ew,ey+y+eh),(0,255,0),2) 
                        imgGray = cv2.rectangle(imgGray, (ex+x,ey+y), (ex+x+ew,ey+y+eh),(0,255,0),2) '''
                qimgGray = QImage(imgGray.data, width, height,width, QImage.Format_Indexed8)
                qpiximgGray = QPixmap.fromImage(qimgGray)
                qimg = QImage(img_rgb.data, width, height,3*width, QImage.Format_RGB888)
                qpiximg = QPixmap.fromImage(qimg)
                dlg.label_imgOri.setPixmap(qpiximg.scaled(dlg.label_imgOri.width(), dlg.label_imgOri.height()))
                dlg.label_imgPro.setPixmap(qpiximgGray.scaled(dlg.label_imgPro.width(), dlg.label_imgPro.height()))
                self.msleep(self.delay)
            else:
                self.sleep(1)
        self.cap.release()
        #cv2.destroyAllWindows()
        #self.signal.emit()
    def stopPlay(self):
        self.flag = 0
    def playAgain(self):
        self.flag = 1
    def changeDelay(self, delayTime):
        self.delay = delayTime
       
    
        
class ReadCam(QDialog, Ui_Dialog):
    pause = pyqtSignal()
    play = pyqtSignal()
    delaySignal = pyqtSignal(int)
    def __init__(self, parent=None):
        super(ReadCam, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('视频处理')
        self.horizontalSlider_playSpeed.setMinimum(0)
        self.horizontalSlider_playSpeed.setMaximum(5000)
        self.horizontalSlider_playSpeed.setValue(500)
        self.horizontalSlider_playSpeed.setSingleStep(100)
        self.horizontalSlider_playSpeed.setTickInterval(500)
        self.horizontalSlider_playSpeed.setTickPosition(QSlider.TicksBelow)
        self.update_tag = 0
        self.thread = MyThread()
        self.pause.connect(self.thread.stopPlay)
        self.play.connect(self.thread.playAgain)
        self.horizontalSlider_playSpeed.valueChanged.connect(self.valuechange)
        self.delaySignal.connect(self.thread.changeDelay)
    def valuechange(self):
        delayTime = self.horizontalSlider_playSpeed.value()
        self.delaySignal.emit(delayTime)
    
    
    
        
    @pyqtSlot()
    def on_pushButton_bro_clicked(self):
        global file_name
        file_name, file_type = QFileDialog.getOpenFileName(self,"选择一个视频",".","*.avi")
        self.label_camAdr.setText(file_name)
        cap = cv2.VideoCapture(file_name)
        ret, frame = cap.read()
        img_rgb =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, bytesPerComponent = img_rgb.shape
        imgGray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        qimgGray = QImage(imgGray.data, width, height,width, QImage.Format_Indexed8)#灰度图
        qpiximgGray = QPixmap.fromImage(qimgGray)
        qimg = QImage(img_rgb.data, width, height,3*width, QImage.Format_RGB888)#原始图
        qpiximg = QPixmap.fromImage(qimg)
        dlg.label_imgOri.setPixmap(qpiximg.scaled(dlg.label_imgOri.width(), dlg.label_imgOri.height()))
        dlg.label_imgPro.setPixmap(qpiximgGray.scaled(dlg.label_imgPro.width(), dlg.label_imgPro.height()))
        cap.release()
    
    @pyqtSlot()
    def on_pushButton_nextImg_clicked(self):
        
        self.thread.start()#启动线程
        if(self.update_tag == 0):
            #thread.pause.emit()
            self.update_tag = 1
            self.play.emit()#发送重新播放的信号
        else:
            #thread.pause.emit()
            self.update_tag = 0
            self.pause.emit()#发送暂停信号
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = ReadCam()
    dlg.show()
    sys.exit(app.exec_())
