import cv2
import numpy as np
from tkinter import *

cam=cv2.VideoCapture(0)
cap=cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)
#cap.set(10,100)

cam.set(3, 800)
cam.set(4, 700)
#cam.set(10,100)

coord=[]

def empty(a):
      pass

def AdDrawBlue():
      #o=(255,0,0)

      cv2.namedWindow('Pen Colour Tracker')
      cv2.resizeWindow('Pen Colour Tracker',500,240)
      cv2.createTrackbar('Hue Min','Pen Colour Tracker',0,179,empty)
      cv2.createTrackbar('Hue Max','Pen Colour Tracker',179,179,empty)
      cv2.createTrackbar('Saturation Min','Pen Colour Tracker',0,255,empty)
      cv2.createTrackbar('Saturation Max','Pen Colour Tracker',255,255,empty)
      cv2.createTrackbar('Value Min','Pen Colour Tracker',0,255,empty)
      cv2.createTrackbar('Value Max','Pen Colour Tracker',255,255,empty)

      
      while True:
            ret,Cam=cap.read()
            Cam = cv2.flip(Cam, 1)
            imgHSV=cv2.cvtColor(Cam, cv2.COLOR_BGR2HSV)
            hmin=cv2.getTrackbarPos('Hue Min','Pen Colour Tracker')
            hmax=cv2.getTrackbarPos('Hue Max','Pen Colour Tracker')
            smin=cv2.getTrackbarPos('Saturation Min','Pen Colour Tracker')
            smax=cv2.getTrackbarPos('Saturation Max','Pen Colour Tracker')
            vmin=cv2.getTrackbarPos('Value Min','Pen Colour Tracker')
            vmax=cv2.getTrackbarPos('Value Max','Pen Colour Tracker')
            lower=np.array([hmin,smin,vmin])
            upper=np.array([hmax,smax,vmax])
            mask=cv2.inRange(imgHSV,lower,upper)


            #cv2.imshow('Original',Cam)
            #cv2.imshow('Hsv',imgHSV)
            cv2.imshow('Mask',mask)

            imgResult=cv2.bitwise_and(Cam,Cam,mask=mask)
            cv2.imshow("Camera Screen1",imgResult)
      
      
            if cv2.waitKey(1) & 0xFF==ord('q'):
                  break
            
      #cap.release()
      cv2.destroyAllWindows()

      TT=[255,0,0]
      width=5

      canvas = None
      x1,y1=0,0

      while True:
            _,cam = cap.read()
            cam = cv2.flip( cam, 1 )
      
            if canvas is None:
                  canvas = np.zeros_like(cam)

            cam=cv2.GaussianBlur(cam,(7,7),1)
            hsv = cv2.cvtColor(cam, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower, upper)

            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours and cv2.contourArea(max(contours, key = cv2.contourArea)) >800:
                  c = max(contours, key = cv2.contourArea)
                  x2,y2,w,h = cv2.boundingRect(c)

                  if x1 == 0 and y1 == 0:
                        x1,y1= x2,y2

                  else:
                        canvas = cv2.line(canvas, (x1,y1),(x2,y2), TT, width)
                  x1,y1= x2,y2
            else:
                  x1,y1 =0,0

            cam = cv2.add(cam,canvas)
            #stacked = np.hstack((canvas,cam))
            cv2.imshow('Canvas',canvas)
            cv2.imshow('Camera',cam)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                  win.destroy()
                  break
            if (k == ord('c') or k==ord('C')):
                  canvas = None
            if (k == ord('b') or k==ord('B')):
                  TT=[0,0,0]
                  width=1
            if (k == ord('v') or k==ord('V')):
                  TT=[255,0,0]
                  width=5
            if (k == ord('e') or k==ord('E')):
                  TT=[0,0,0]
                  width=50

      cv2.destroyAllWindows()
      cap.release()

      
def AdDrawRed():
      #o=(0,0,255)

      cv2.namedWindow('Pen Colour Tracker')
      cv2.resizeWindow('Pen Colour Tracker',500,240)
      cv2.createTrackbar('Hue Min','Pen Colour Tracker',0,179,empty)
      cv2.createTrackbar('Hue Max','Pen Colour Tracker',179,179,empty)
      cv2.createTrackbar('Saturation Min','Pen Colour Tracker',0,255,empty)
      cv2.createTrackbar('Saturation Max','Pen Colour Tracker',255,255,empty)
      cv2.createTrackbar('Value Min','Pen Colour Tracker',0,255,empty)
      cv2.createTrackbar('Value Max','Pen Colour Tracker',255,255,empty)

      
      while True:
            ret,Cam=cap.read()
            Cam = cv2.flip(Cam, 1)
            imgHSV=cv2.cvtColor(Cam, cv2.COLOR_BGR2HSV)
            hmin=cv2.getTrackbarPos('Hue Min','Pen Colour Tracker')
            hmax=cv2.getTrackbarPos('Hue Max','Pen Colour Tracker')
            smin=cv2.getTrackbarPos('Saturation Min','Pen Colour Tracker')
            smax=cv2.getTrackbarPos('Saturation Max','Pen Colour Tracker')
            vmin=cv2.getTrackbarPos('Value Min','Pen Colour Tracker')
            vmax=cv2.getTrackbarPos('Value Max','Pen Colour Tracker')
            lower=np.array([hmin,smin,vmin])
            upper=np.array([hmax,smax,vmax])
            mask=cv2.inRange(imgHSV,lower,upper)


            #cv2.imshow('Original',Cam)
            #cv2.imshow('Hsv',imgHSV)
            cv2.imshow('Mask',mask)

            imgResult=cv2.bitwise_and(Cam,Cam,mask=mask)
            cv2.imshow("Camera Screen1",imgResult)
      
      
            if cv2.waitKey(1) & 0xFF==ord('q'):
                  break
      #cap.release()
      cv2.destroyAllWindows()
            
      canvas = None
      x1,y1=0,0

      TT=[0,0,255]
      width=5

      while True:
            _,cam = cap.read()
            cam = cv2.flip( cam, 1 )
      
            if canvas is None:
                  canvas = np.zeros_like(cam)

            cam=cv2.GaussianBlur(cam,(7,7),1)
            hsv = cv2.cvtColor(cam, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower, upper)

            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours and cv2.contourArea(max(contours, key = cv2.contourArea)) >800:
                  c = max(contours, key = cv2.contourArea)
                  x2,y2,w,h = cv2.boundingRect(c)

                  if x1 == 0 and y1 == 0:
                        x1,y1= x2,y2

                  else:
                        canvas = cv2.line(canvas, (x1,y1),(x2,y2), TT, width)
                  x1,y1= x2,y2
            else:
                  x1,y1 =0,0

            cam = cv2.add(cam,canvas)
            #stacked = np.hstack((canvas,cam))
            cv2.imshow('Canvas',canvas)
            cv2.imshow('Camera',cam)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                  win.destroy()
                  break
            
            if (k == ord('c') or k==ord('C')):
                  canvas = None
            if (k == ord('b') or k==ord('B')):
                  TT=[0,0,0]
                  width=1
            if (k == ord('v') or k==ord('V')):
                  TT=[0,0,255]
                  width=5
            if (k == ord('e') or k==ord('E')):
                  TT=[0,0,0]
                  width=50

      cv2.destroyAllWindows()
      cap.release()
def AdDrawGreen():
      #o=(0,255,0)

      cv2.namedWindow('Pen Colour Tracker')
      cv2.resizeWindow('Pen Colour Tracker',500,240)
      cv2.createTrackbar('Hue Min','Pen Colour Tracker',0,179,empty)
      cv2.createTrackbar('Hue Max','Pen Colour Tracker',179,179,empty)
      cv2.createTrackbar('Saturation Min','Pen Colour Tracker',0,255,empty)
      cv2.createTrackbar('Saturation Max','Pen Colour Tracker',255,255,empty)
      cv2.createTrackbar('Value Min','Pen Colour Tracker',0,255,empty)
      cv2.createTrackbar('Value Max','Pen Colour Tracker',255,255,empty)

      
      while True:
            ret,Cam=cap.read()
            Cam = cv2.flip(Cam, 1)
            imgHSV=cv2.cvtColor(Cam, cv2.COLOR_BGR2HSV)
            hmin=cv2.getTrackbarPos('Hue Min','Pen Colour Tracker')
            hmax=cv2.getTrackbarPos('Hue Max','Pen Colour Tracker')
            smin=cv2.getTrackbarPos('Saturation Min','Pen Colour Tracker')
            smax=cv2.getTrackbarPos('Saturation Max','Pen Colour Tracker')
            vmin=cv2.getTrackbarPos('Value Min','Pen Colour Tracker')
            vmax=cv2.getTrackbarPos('Value Max','Pen Colour Tracker')
            lower=np.array([hmin,smin,vmin])
            upper=np.array([hmax,smax,vmax])
            mask=cv2.inRange(imgHSV,lower,upper)


            #cv2.imshow('Original',Cam)
            #cv2.imshow('Hsv',imgHSV)
            cv2.imshow('Mask',mask)

            imgResult=cv2.bitwise_and(Cam,Cam,mask=mask)
            cv2.imshow("Camera Screen1",imgResult)
      
      
            if cv2.waitKey(1) & 0xFF==ord('q'):
                  break
      #cap.release()
      cv2.destroyAllWindows()
            
      canvas = None
      x1,y1=0,0

      TT=[0,255,0]
      width=5

      while True:
            _,cam = cap.read()
            cam = cv2.flip( cam, 1 )
      
            if canvas is None:
                  canvas = np.zeros_like(cam)

            cam=cv2.GaussianBlur(cam,(7,7),1)
            hsv = cv2.cvtColor(cam, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower, upper)

            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours and cv2.contourArea(max(contours, key = cv2.contourArea)) >800:
                  c = max(contours, key = cv2.contourArea)
                  x2,y2,w,h = cv2.boundingRect(c)

                  if x1 == 0 and y1 == 0:
                        x1,y1= x2,y2

                  else:
                        canvas = cv2.line(canvas, (x1,y1),(x2,y2), TT, width)
                  x1,y1= x2,y2
            else:
                  x1,y1 =0,0

            cam = cv2.add(cam,canvas)
            #stacked = np.hstack((canvas,cam))
            cv2.imshow('Canvas',canvas)
            cv2.imshow('Camera',cam)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                  win.destroy()
                  break
            
            if (k == ord('c') or k==ord('C')):
                  canvas = None
            if (k == ord('b') or k==ord('B')):
                  TT=[0,0,0]
                  width=1
            if (k == ord('v') or k==ord('V')):
                  TT=[0,255,0]
                  width=5
            if (k == ord('e') or k==ord('E')):
                  TT=[0,0,0]
                  width=50

      cv2.destroyAllWindows()
      cap.release()

def AdDrawYellow():
      #o=(0,255,255)

      cv2.namedWindow('Pen Colour Tracker')
      cv2.resizeWindow('Pen Colour Tracker',500,240)
      cv2.createTrackbar('Hue Min','Pen Colour Tracker',0,179,empty)
      cv2.createTrackbar('Hue Max','Pen Colour Tracker',179,179,empty)
      cv2.createTrackbar('Saturation Min','Pen Colour Tracker',0,255,empty)
      cv2.createTrackbar('Saturation Max','Pen Colour Tracker',255,255,empty)
      cv2.createTrackbar('Value Min','Pen Colour Tracker',0,255,empty)
      cv2.createTrackbar('Value Max','Pen Colour Tracker',255,255,empty)

      
      while True:
            ret,Cam=cap.read()
            Cam = cv2.flip(Cam, 1)
            imgHSV=cv2.cvtColor(Cam, cv2.COLOR_BGR2HSV)
            hmin=cv2.getTrackbarPos('Hue Min','Pen Colour Tracker')
            hmax=cv2.getTrackbarPos('Hue Max','Pen Colour Tracker')
            smin=cv2.getTrackbarPos('Saturation Min','Pen Colour Tracker')
            smax=cv2.getTrackbarPos('Saturation Max','Pen Colour Tracker')
            vmin=cv2.getTrackbarPos('Value Min','Pen Colour Tracker')
            vmax=cv2.getTrackbarPos('Value Max','Pen Colour Tracker')
            lower=np.array([hmin,smin,vmin])
            upper=np.array([hmax,smax,vmax])
            mask=cv2.inRange(imgHSV,lower,upper)


            #cv2.imshow('Original',Cam)
            #cv2.imshow('Hsv',imgHSV)
            cv2.imshow('Mask',mask)

            imgResult=cv2.bitwise_and(Cam,Cam,mask=mask)
            cv2.imshow("Camera Screen1",imgResult)
      
      
            if cv2.waitKey(1) & 0xFF==ord('q'):
                  break
      #cap.release()
      cv2.destroyAllWindows()
            
      canvas = None
      x1,y1=0,0

      TT=[0,255,255]
      width=5

      while True:
            _,cam = cap.read()
            cam = cv2.flip( cam, 1 )
      
            if canvas is None:
                  canvas = np.zeros_like(cam)

            cam=cv2.GaussianBlur(cam,(7,7),1)
            hsv = cv2.cvtColor(cam, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower, upper)

            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours and cv2.contourArea(max(contours, key = cv2.contourArea)) >800:
                  c = max(contours, key = cv2.contourArea)
                  x2,y2,w,h = cv2.boundingRect(c)

                  if x1 == 0 and y1 == 0:
                        x1,y1= x2,y2

                  else:
                        canvas = cv2.line(canvas, (x1,y1),(x2,y2), TT, width)
                  x1,y1= x2,y2
            else:
                  x1,y1 =0,0

            cam = cv2.add(cam,canvas)
            #stacked = np.hstack((canvas,cam))
            cv2.imshow('Canvas',canvas)
            cv2.imshow('Camera',cam)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                  win.destroy()
                  break    
            if (k == ord('c') or k==ord('C')):
                  canvas = None
            if (k == ord('b') or k==ord('B')):
                  TT=[0,0,0]
                  width=1
            if (k == ord('v') or k==ord('V')):
                  TT=[0,255,255]
                  width=5
            if (k == ord('e') or k==ord('E')):
                  TT=[0,0,0]
                  width=50

      cv2.destroyAllWindows()
      cap.release()


def Adjust():      
      adIntrolbl= Label(win, text = "Adjust the Pen",
                font = ("Amsterdam",22,'bold'),background = "lemon chiffon",foreground="firebrick1",)
      adIntrolbl.pack(pady=(8,0))
      adStepslbl= Label(win, text ='This section is for the adjustment to the area and color of your pen.\n\nSTEPS:\n1) After choosing the color, a "Pen Colour Tracker" will appear along with a "Mask" and a "Camera Screen1".\n2) Using the Tracker set the values of Hue, Saturation and Value such that the area of the Pen becomes White in Mask Screen.\n3) Hold the Pen or Object in the position in which you want to use, while using the \'Pen Color Tracker\'.\n4) Once the Pen area selection is done, press "q" to continues to the Canvas.\n5) Upon pressing "q", a Canvas screen will appear, use the pen to write or draw anything on it.\n6) To Clear the Screen, Press "c"\n7) To Use Eraser, Press "e"\n8) To break the flow of line, Press "b". And to bring it back, Press "v" .\n\n Once done with the drawing, press "Esc" to close the canvas and end the program.\n\nCOLORS:\nChoose the color of the Pen you would like to use:'
                        ,font = ("Georgia",13,'bold'),background = "lemon chiffon",foreground="black", wraplength=750,justify=LEFT,)
      adStepslbl.pack()
      bluebut=Button(win, text='Blue',font=("Georgia",14,),width=5, relief='raised', border=5, background="cyan2",
                     foreground="black", command= AdDrawBlue)
      bluebut.pack(padx=(300,50),side=LEFT)
      greenbut=Button(win, text='Green',font=("Georgia",14,),width=5, relief='raised', border=5, background="green2",
                     foreground="black", command= AdDrawGreen)
      greenbut.pack(padx=(0,50),side=LEFT)
      yellowbut=Button(win, text='Yellow',font=("Georgia",14,),width=5, relief='raised', border=5, background="yellow",
                     foreground="black", command= AdDrawYellow)
      yellowbut.pack(padx=(0,50),side=LEFT)
      redbut=Button(win, text='Red',font=("Georgia",14,),width=5, relief='raised', border=5, background="firebrick1",
                     foreground="black", command= AdDrawRed)
      redbut.pack(side=LEFT)
      

def screen3():
      headlbl.destroy()
      introlbl.destroy()
      menulbl.destroy()
      menubut1.destroy()
      menubut2.destroy()
      Adjust()

def BlueCanvas():
      canvas = None
      x1,y1=0,0
      
      TT=[255,0,0]
      width=5

      while True:
            _,cam = cap.read()
            cam = cv2.flip( cam, 1 )
      
            if canvas is None:
                  canvas = np.zeros_like(cam)

            cam=cv2.GaussianBlur(cam,(7,7),1)
            lower  = np.array([26,80,147])
            upper = np.array([81,255,255])
            hsv = cv2.cvtColor(cam, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower, upper)

            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours and cv2.contourArea(max(contours, key = cv2.contourArea)) >800:
                  c = max(contours, key = cv2.contourArea)
                  x2,y2,w,h = cv2.boundingRect(c)

                  if x1 == 0 and y1 == 0:
                        x1,y1= x2,y2

                  else:
                        canvas = cv2.line(canvas, (x1,y1),(x2,y2), TT, width)
                  x1,y1= x2,y2
            else:
                  x1,y1 =0,0

            cam = cv2.add(cam,canvas)
            #stacked = np.hstack((canvas,cam))
            cv2.imshow('Canvas',canvas)
            cv2.imshow('Camera',cam)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                  win.destroy()
                  break    
            if (k == ord('c') or k==ord('C')):
                  canvas = None
            if (k == ord('b') or k==ord('B')):
                  TT=[0,0,0]
                  width=1
            if (k == ord('v') or k==ord('V')):
                  TT=[255,0,0]
                  width=5
            if (k == ord('e') or k==ord('E')):
                  TT=[0,0,0]
                  width=50

      cv2.destroyAllWindows()
      cap.release()
      

def GreenCanvas():
      canvas = None
      x1,y1=0,0
      
      TT=[0,255,0]
      width=5

      while True:
            _,cam = cap.read()
            cam = cv2.flip( cam, 1 )
      
            if canvas is None:
                  canvas = np.zeros_like(cam)

            cam=cv2.GaussianBlur(cam,(7,7),1)
            hsv = cv2.cvtColor(cam, cv2.COLOR_BGR2HSV)
            lower  = np.array([26,80,147])
            upper = np.array([81,255,255])
            mask = cv2.inRange(hsv, lower, upper)

            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours and cv2.contourArea(max(contours, key = cv2.contourArea)) >800:
                  c = max(contours, key = cv2.contourArea)
                  x2,y2,w,h = cv2.boundingRect(c)

                  if x1 == 0 and y1 == 0:
                        x1,y1= x2,y2

                  else:
                        canvas = cv2.line(canvas, (x1,y1),(x2,y2), TT, width)
                  x1,y1= x2,y2
            else:
                  x1,y1 =0,0

            cam = cv2.add(cam,canvas)
            #stacked = np.hstack((canvas,cam))
            cv2.imshow('Canvas',canvas)
            cv2.imshow('Camera',cam)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                  win.destroy()
                  break    
            if (k == ord('c') or k==ord('C')):
                  canvas = None
            if (k == ord('b') or k==ord('B')):
                  TT=[0,0,0]
                  width=1
            if (k == ord('v') or k==ord('V')):
                  TT=[0,255,0]
                  width=5
            if (k == ord('e') or k==ord('E')):
                  TT=[0,0,0]
                  width=50

      cv2.destroyAllWindows()
      cap.release()

def RedCanvas():
      canvas = None
      x1,y1=0,0
      
      TT=[0,0,255]
      width=5

      while True:
            _,cam = cap.read()
            cam = cv2.flip( cam, 1 )
      
            if canvas is None:
                  canvas = np.zeros_like(cam)

            cam=cv2.GaussianBlur(cam,(7,7),1)
            hsv = cv2.cvtColor(cam, cv2.COLOR_BGR2HSV)
            lower  = np.array([26,80,147])
            upper = np.array([81,255,255])
            mask = cv2.inRange(hsv, lower, upper)

            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours and cv2.contourArea(max(contours, key = cv2.contourArea)) >800:
                  c = max(contours, key = cv2.contourArea)
                  x2,y2,w,h = cv2.boundingRect(c)

                  if x1 == 0 and y1 == 0:
                        x1,y1= x2,y2

                  else:
                        canvas = cv2.line(canvas, (x1,y1),(x2,y2), TT, width)
                  x1,y1= x2,y2
            else:
                  x1,y1 =0,0

            cam = cv2.add(cam,canvas)
            #stacked = np.hstack((canvas,cam))
            cv2.imshow('Canvas',canvas)
            cv2.imshow('Camera',cam)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                  win.destroy()
                  break    
            if (k == ord('c') or k==ord('C')):
                  canvas = None
            if (k == ord('b') or k==ord('B')):
                  TT=[0,0,0]
                  width=1
            if (k == ord('v') or k==ord('V')):
                  TT=[0,0,255]
                  width=5
            if (k == ord('e') or k==ord('E')):
                  TT=[0,0,0]
                  width=50

      cv2.destroyAllWindows()
      cap.release()


def YellowCanvas():
      canvas = None
      x1,y1=0,0
      
      TT=[0,255,255]
      width=5

      while True:
            _,cam = cap.read()
            cam = cv2.flip( cam, 1 )
      
            if canvas is None:
                  canvas = np.zeros_like(cam)

            cam=cv2.GaussianBlur(cam,(7,7),1)
            hsv = cv2.cvtColor(cam, cv2.COLOR_BGR2HSV)
            lower  = np.array([26,80,147])
            upper = np.array([81,255,255])
            mask = cv2.inRange(hsv, lower, upper)

            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours and cv2.contourArea(max(contours, key = cv2.contourArea)) >800:
                  c = max(contours, key = cv2.contourArea)
                  x2,y2,w,h = cv2.boundingRect(c)

                  if x1 == 0 and y1 == 0:
                        x1,y1= x2,y2

                  else:
                        canvas = cv2.line(canvas, (x1,y1),(x2,y2), TT, width)
                  x1,y1= x2,y2
            else:
                  x1,y1 =0,0

            cam = cv2.add(cam,canvas)
            #stacked = np.hstack((canvas,cam))
            cv2.imshow('Canvas',canvas)
            cv2.imshow('Camera',cam)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                  win.destroy()
                  break    
            if (k == ord('c') or k==ord('C')):
                  canvas = None
            if (k == ord('b') or k==ord('B')):
                  TT=[0,0,0]
                  width=1
            if (k == ord('v') or k==ord('V')):
                  TT=[0,255,255]
                  width=5
            if (k == ord('e') or k==ord('E')):
                  TT=[0,0,0]
                  width=50

      cv2.destroyAllWindows()
      cap.release()


def Canvas():
      sideimg=PhotoImage(file="C:/Users/GAURISHA/Desktop/Folders folder/Air Canvas Project/Air Canvas Github/canvas_man.png")
      sidelbl=Label(win, background = "lemon chiffon",)
      sidelbl.pack(padx=(15,0),pady=(50,30),side=LEFT)
      sidelbl.configure(image=sideimg)
      sidelbl.image = sideimg

      CanIntrolbl= Label(win, text ='~~Canvas~~',font = ("Amsterdam",32,'bold','italic'),background = "lemon chiffon",foreground='firebrick1')
      CanIntrolbl.pack()

      '''Collbl= Label(win, text ='Colors:' ,font = ("Georgia",14,'bold'),background = "lemon chiffon",
                    foreground="black")
      Collbl.pack(pady=(0,30))'''

      Colchoicelbl= Label(win, text ='Use a Green Colored Object as a Pen for better use.\n\nChoose the color you would like to use for the pen:' ,font = ("Georgia",14,'bold'),background = "lemon chiffon",
                    foreground="black")
      Colchoicelbl.pack()

      BlueBut= Button(win, text ='Blue' ,font=("Georgia",14,),width=30, relief='raised', border=5,background = "cyan2",
                    foreground="black",command=BlueCanvas)
      BlueBut.pack(pady=(20,0))
      GreenBut= Button(win, text ='Green' ,font=("Georgia",14,),width=30, relief='raised', border=5,background = "green2",
                    foreground="black",command=GreenCanvas)
      GreenBut.pack(pady=(20,0))
      YellowBut= Button(win, text ='Yellow' ,font=("Georgia",14,),width=30, relief='raised', border=5,background = "yellow",
                    foreground="black",command=YellowCanvas)
      YellowBut.pack(pady=(20,0))
      RedBut= Button(win, text ='Red' ,font=("Georgia",14,),width=30, relief='raised', border=5,background = "firebrick1",
                    foreground="black",command=RedCanvas)
      RedBut.pack(pady=(20,0))
      Clearlbl= Label(win, text ='To Clear the Screen, press "c"' ,font = ("Georgia",14,'bold'),background = "lemon chiffon",
                    foreground="black")
      Clearlbl.pack(pady=(30,0))
      Eraselbl= Label(win, text ='To Use the Eraser, press "e"' ,font = ("Georgia",14,'bold'),background = "lemon chiffon",
                    foreground="black")
      Eraselbl.pack(pady=(30,0))
      FlowBrlbl= Label(win, text ='To Break the flow of line, press "b"' ,font = ("Georgia",14,'bold'),background = "lemon chiffon",
                    foreground="black")
      FlowBrlbl.pack(pady=(30,0))
      FlowCntlbl= Label(win, text ='To Continue the Flow of Line, press "v"' ,font = ("Georgia",14,'bold'),background = "lemon chiffon",
                    foreground="black")
      FlowCntlbl.pack(pady=(30,0))
      Exitlbl= Label(win, text ="To Exit, press 'Esc'" ,font = ("Georgia",14,'bold'),background = "lemon chiffon",
                    foreground="black")
      Exitlbl.pack(pady=(10,0))
      
def screen2():
      headlbl.destroy()
      introlbl.destroy()
      menulbl.destroy()
      menubut1.destroy()
      menubut2.destroy()
      Canvas()
      

win=Tk()
win.title('Air Canvas')
win.geometry('950x625')
win.config(background="lemon chiffon")
win.resizable(0,0)


headimg=PhotoImage(file="C:/Users/GAURISHA/Desktop/Folders folder/Air Canvas Project/Air Canvas Github/air_canvas_logo.png")
headlbl=Label(win, image=headimg, background = "lemon chiffon",)
headlbl.pack()

introlbl= Label(win, text = "Air Canvas is a program that enables the user to draw in the Air which acts as a Canvas.\nIt is a Virtual Notepad, which can be used anywhere, its applications are limitless.\nUse it as virtual Black Board or virtual Meeting Pad.",
                font = ("Gabriola",20,'bold'),background = "lemon chiffon",foreground="black")
introlbl.pack(pady=(0,30))

menulbl=Label(win, text="Menu",font=("Amsterdam",18,'bold'),background="lemon chiffon",foreground="black",)
menulbl.pack(padx=(0,20))

menubut1=Button(win, text='Start Canvas',font=("Georgia",14,),
                width=25, relief='raised', border=5, background="SpringGreen",foreground="black", command= screen2 )
menubut1.pack()

menubut2=Button(win, text='Adjust the Pen and Use the Canvas',font=("Georgia",14,),
                width=30, relief='raised', border=5, background="SpringGreen",foreground="black", command= screen3 )
menubut2.pack(pady=(20,0))

win.mainloop()
