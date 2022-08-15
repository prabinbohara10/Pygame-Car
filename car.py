import imp
from pickle import FALSE, TRUE
import numpy as np
import cv2


import pygame


class Car:
    def __init__(self,width,height,car_width,car_height,track_canny_opencv,car_canny_opencv):
        self.velocity = 4
        self.x = 50
        self.y = 80
        self.angle=0
        self.width=width
        self.height= height
        self.car_width=car_width
        self.car_height=car_height
        self.track_canny_opencv=track_canny_opencv
        self.car_canny_opencv= car_canny_opencv
        
    
    def move(self, x,y):
        self.x += x
        self.y += y

    def rotate(self,angle):
        self.angle+=angle

    def collision_check(self):
        
        x=int(self.x)
        y=int(self.y)
        print(y,x,self.car_height,self.car_width)

        car_array = np.zeros(shape=(self.width, self.height))
        for i in range(x, x+self.car_width):
            for j in range (y, y+self.car_height ):
                #print(i-y,"  ", j-x,"\n")
                car_array[i][j] = self.car_canny_opencv[i-x][j-y]

        for i in range(0, self.width ):
            for j in range (0, self.height):
                if(car_array[i][j]!=0):
                    if(self.track_canny_opencv[i][j] !=0):
                        return True

        return False

        
