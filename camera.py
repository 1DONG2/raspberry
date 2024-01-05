import numpy as np
import cv2 # 카메라 라이브러리
from picamera2 import Picamera2 # 라즈베리파이 카메라 동기화
import pygame # 카메라 촬영음 효과를 위한 라이브러리

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + \
                                    'haarcascade_frontalface_default.xml') # 얼굴 정면 인식 데이터 불러오기

picam2 = Picamera2() # 라즈베리파이 카메라 동기화 작업
picam2.start() # 스타트

cap = cv2.VideoCapture(0) # cv 카메라 캡처 시작
cap.set(3,640) # set Width
cap.set(4,480) # set Height

pygame.init() # 파이게임 불러오기 
pygame.mixer.init()  # 파이게임 믹서음 불러오기
sound = pygame.mixer.Sound('/home/dongdong/Downloads/camera-shutter-pentax-k20d-38609.mp3') # HDD 안에 있는 카메라 촬영음 파일

while(True): # q가 눌릴 때까지 반복
    #ret, frame = cap.read()
    frame = picam2.capture_array() # 라즈베리파이 카메라를 통해 배열 생성
    frame = cv2.flip(frame, -1) # Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 흑백 캠으로 변환 
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(10,10)
    ) # 다양한 변수 조정, 카메라의 얼굴 등등 스케일

    for (x,y,w,h) in faces: # 얼굴을 인식했을때 나타나는 효과
        cv2.rectangle(gray,(x,y),(w+w,y+h),(255,0,0),2) # 얼굴 주변으로 사각형 그려주기
        sound.play() # 카메라 촬영음 내기

    cv2.imshow('gray', gray) # 카메라 켜기
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # press 'q' to quit
        break # 루프 종료

cap.release()
pygame.quit()
cv2.destroyAllWindows()
# 해당 리소스 정리