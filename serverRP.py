import socket
import random
#import cv2
#import base64
# Create a socket object


#video = cv2.VideoCapture(0)

s = socket.socket()

# Define the port on which you want to connect
port = 3000

# connect to the server on local computer
s.connect(('192.168.43.129', port))

# receive data from the server


#while(True):
'''ret, frame = video.read()
frame = cv2.resize(frame,(150,150),interpolation = cv2.INTER_CUBIC)
retval, buffer = cv2.imencode('.jpg', frame)
jpg_text = base64.b64encode(buffer)'''
    

gonderilcekData = '''
    {"sicaklik":''' + str(random.randint(10,80)) + ''',"basinc":''' + str(random.randint(10,80)) + ''',"basinc1":''' + str(random.randint(10,80)) +'''}'''
s.send(gonderilcekData.encode()) # veriyi gonderdi
print(gonderilcekData)
data = s.recv(1024) # cevap bekle
print(data.decode())

    #time.sleep(1) 


# close the connection
s.close()
'''
video.release()
cv2.destroyAllWindows()'''
