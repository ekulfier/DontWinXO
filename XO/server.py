# server.py

import socket

serverip = '192.168.1.165'
portUser = 2082
portBot = 2496


serverUser = socket.socket()            # สร้าง socket
serverUser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)       # เปิด socket 1 == ON
                                # method  ที่ REUSE Port
serverUser.bind((serverip, portUser))   # ผูก ip กับ port ให้ชนกัน 
serverUser.listen(1)    # ฟัง เพื่อกำหนดจำนวน client

serverBot = socket.socket()            # สร้างตัวเชื่อม
serverBot.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)       # เปิด socket 1 == ON

serverBot.bind((serverip, portBot))   # ผูก ip กับ port ให้ชนกัน 
serverBot.listen(1)    # ฟัง เพื่อกำหนดจำนวน client

clientUser, addrUser = serverUser.accept()  # รับการเชื่อมต่อจากฝั่ง client
print('Connected from user: ', addrUser)

clientBot, addrBot = serverBot.accept()  # รับการเชื่อมต่อจากฝั่ง client
print('Connected from bot: ', addrBot)

while True:
    print("Waiting for User") 
    # ***** recv รับได้แค่ ครั้งเดียว จบเลย ******
    dataUser = clientUser.recv(1024).decode('utf-8')    # buffer server size 1024 per step 
    #######                                             #   .decode('utf-8') ==> แปลง Byte เป็น String 
    print("DataUser is : ", dataUser)
    clientBot.send(dataUser.encode('utf-8'))

    print("Waiting for Bot")

    dataBot = clientBot.recv(1024).decode('utf-8')
    print("DataBot is : ", dataBot)

    clientUser.send(dataBot.encode('utf-8'))       #   .encode('utf-8') ==> แปลง String เป็น Byte   # send text to client to bot