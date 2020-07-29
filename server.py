import socket
import random
import cv2
import base64
import threading
from time import sleep

# Create a socket object

#'./Bilgisayar gözüyle Istanbul (tensorflow).mp4'

def sendVideo(width,height,port):
    videoSocket = socket.socket()
    videoSocket.connect(('localhost', port))
    video = cv2.VideoCapture(0)
    while(video.isOpened()):
        ret, frame = video.read()
        frame = cv2.resize(frame, (500, 500), interpolation=cv2.INTER_CUBIC)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        retval, buffer = cv2.imencode('.jpg', frame, encode_param)
        jpg_text = base64.b64encode(buffer)
        jpg_text = str(jpg_text).split("'")[1]
        aleyna = '''
        {"resim":"''' + jpg_text +'''"}'''

        videoSocket.send(aleyna.encode())
        recv = videoSocket.recv(1024)
        print(recv)
        cv2.imshow('window', frame)
'''
    threading._start_new_thread(sendVideo,(150,150,3001))

    while(True):
        sleep(1)
'''

s = socket.socket()
port = 3001
s.connect(('localhost', port))
video = cv2.VideoCapture(0)
while (video.isOpened()):
    ret, frame = video.read()
    frame = cv2.resize(frame, (500, 500), interpolation=cv2.INTER_CUBIC)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    retval, buffer = cv2.imencode('.jpg', frame, encode_param)
    jpg_text = base64.b64encode(buffer)
    jpg_text = str(jpg_text).split("'")[1]
    gonderilcekData = '''
        {"sicaklik":''' + str(random.randint(10,80)) + ''',"resim":"''' + jpg_text + '''","basinc":''' + str(random.randint(10,80)) + ''',"basinc1":''' + str(random.randint(10,80)) +'''}'''
    #print(gonderilcekData)
    s.send(gonderilcekData.encode()) # veriyi gonderdi
    #print(gonderilcekData)
    data = s.recv(1024)# cevap bekle
    print(data)
    if(data.decode() == "-1"):
        break
    #time.sleep(1)
# close the connection
s.close()

video.release()
cv2.destroyAllWindows()
