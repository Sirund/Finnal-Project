import cv2
import numpy as np

def box(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Merah
    red_low = np.array([141, 143, 21])
    red_up = np.array([174, 255, 255])

    #Hijau
    green_low = np.array([36, 10, 0])
    green_up = np.array([120, 255, 255])

    #Biru
    blue_low = np.array([100, 100, 100])
    blue_up = np.array([120, 255, 255])

    #Kuning
    yellow_low = np.array([20, 100, 100])
    yellow_up = np.array([40, 255, 255])

    red_mask = cv2.inRange(imgHSV, red_low, red_up)
    green_mask = cv2.inRange(imgHSV, green_low, green_up)
    blue_mask = cv2.inRange(imgHSV, blue_low, blue_up)
    yellow_mask = cv2.inRange(imgHSV, yellow_low, yellow_up)    


    #Merah
    contours_red, hierarchy = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_red:
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
        x, y, w, h = cv2.boundingRect(approx)
        if area > 100:
            cv2.rectangle(img,(x,y), (x+w,y+h), (0,0,255), 3)
            cv2.putText(img, 'RED BALL', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

    # Hijau
    contours_green, hierarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_green:
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt, True)
        print(f'{area}, {peri}')
        approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
        x, y, w, h = cv2.boundingRect(approx)
        if area > 100:
            print(f'{area}, {peri}')
            cv2.rectangle(img,(x,y), (x+w,y+h), (0,128, 0), 3)
            cv2.putText(img, 'GREEN BALL', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,128, 0), 2)
        
    return img

vid = cv2.VideoCapture('vidio.webm')

while True:
    success, frame = vid.read()

    if not success:
        continue

    bonding_box = box(frame)

    cv2.imshow('video', bonding_box)
    if cv2.waitKey(50) & 0xFF ==ord('q'):
        break
 