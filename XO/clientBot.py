# clientBot.py


import socket


####################  SOCKET  ###################
serverip = '192.168.1.165'
portBot = 2496

server = socket.socket()            # สร้างตัวเชื่อม
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) 
server.connect((serverip, portBot))    # ฝั่ง server เป็น bind() 

def getDataFromUser():
    data_server = server.recv(1024).decode('utf-8')
    print(data_server)
    return int(data_server)



while True:
    data1 = getDataFromUser()
    if data1 == 1:
        server.send('5'.encode('utf-8'))
        data2 = getDataFromUser()
        if data2 == 2:
            server.send('3'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 4 or data3 == 6 or data3 == 8 or data3 == 9:
                server.send('7'.encode('utf-8'))
                continue

            elif data3 == 7:
                server.send('4'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 8 or data4 == 9:
                    server.send('6'.encode('utf-8'))
                    continue

                elif data4 == 6:
                    server.send('8'.encode('utf-8'))
                    continue
                    

                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 3:
            server.send('2'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 4 or data3 == 6 or data3 == 7 or data3 == 9:
                server.send('8'.encode('utf-8'))
                continue

            elif data3 == 8:
                server.send('7'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 4 or data4 == 9:
                    server.send('6'.encode('utf-8'))
                    continue

                elif data4 == 6:
                    server.send('9'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 4:
            server.send('7'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 2 or data3 == 6 or data3 == 8 or data3 == 9:
                server.send('3'.encode('utf-8'))
                continue

            elif data3 == 3:
                server.send('2'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 6 or data4 == 9:
                    server.send('8'.encode('utf-8'))
                    continue

                elif data4 == 8:
                    server.send('6'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 6:
            server.send('3'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 2 or data3 == 4 or data3 == 8 or data3 == 9:
                server.send('7'.encode('utf-8'))
                continue

            elif data3 == 7:
                server.send('4'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 2 or data4 == 9:
                    server.send('8'.encode('utf-8'))
                    continue

                elif data4 == 8:
                    server.send('9'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 7:
            server.send('4'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 2 or data3 == 3 or data3 == 8 or data3 == 9:
                server.send('6'.encode('utf-8'))
                continue    

            elif data3 == 6:
                server.send('8'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 3 or data4 == 9:
                    server.send('2'.encode('utf-8'))
                    continue

                elif data4 == 2:
                    server.send('3'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 8:
            server.send('7'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 2 or data3 == 4 or data3 == 6 or data3 == 9:
                server.send('3'.encode('utf-8'))
                continue

            elif data3 == 3:
                server.send('2'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 4 or data4 == 9:
                    server.send('6'.encode('utf-8'))
                    continue

                elif data4 == 6:
                    server.send('9'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 9:
            server.send('2'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 3 or data3 == 4 or data3 == 6 or data3 == 7:
                server.send('8'.encode('utf-8'))
                continue

            elif data3 == 8:
                server.send('7'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 4 or data4 == 6:
                    server.send('3'.encode('utf-8'))
                    continue

                elif data4 == 3:
                    server.send('6'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue

        elif data2 == 0:
            server.send('0'.encode('utf-8'))
            continue

#####################################################
    elif data1 == 2:
        server.send('5'.encode('utf-8'))
        data2 = getDataFromUser()
        if data2 == 1:
            server.send('3'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 4 or data3 == 6 or data3 == 8 or data3 == 9:
                server.send('7'.encode('utf-8'))
                continue

            elif data3 == 7:
                server.send('4'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 8 or data4 == 9:
                    server.send('6'.encode('utf-8'))
                    continue

                elif data4 == 6:
                    server.send('8'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 3:
            server.send('1'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 4 or data3 == 6 or data3 == 7 or data3 == 8:
                server.send('9'.encode('utf-8'))
                continue

            elif data3 == 9:
                server.send('6'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 7 or data4 == 8:
                    server.send('4'.encode('utf-8'))
                    continue

                elif data4 == 4:
                    server.send('8'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 4:
            server.send('1'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 3 or data3 == 6 or data3 == 7 or data3 == 8:
                server.send('9'.encode('utf-8'))
                continue

            elif data3 == 9:
                server.send('3'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 6 or data4 == 8:
                    server.send('7'.encode('utf-8'))
                    continue

                elif data4 == 7:
                    server.send('8'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 6:
            server.send('3'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 1 or data3 == 4 or data3 == 8 or data3 == 9:
                server.send('7'.encode('utf-8'))
                continue

            elif data3 == 7:
                server.send('1'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 4 or data4 == 8:
                    server.send('9'.encode('utf-8'))
                    continue

                elif data4 == 9:
                    server.send('8'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue

        
        elif data2 == 7:
            server.send('1'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 3 or data3 == 4 or data3 == 6 or data3 == 8:
                server.send('9'.encode('utf-8'))
                continue

            elif data3 == 9:
                server.send('8'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 3 or data4 == 4:
                    server.send('6'.encode('utf-8'))
                    continue

                elif data4 == 6:
                    server.send('3'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 8:
            server.send('1'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 3 or data3 == 4 or data3 == 6 or data3 == 7:
                server.send('9'.encode('utf-8'))
                continue

            elif data3 == 9:
                server.send('7'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 4 or data4 == 6:
                    server.send('3'.encode('utf-8'))
                    continue

                elif data4 == 3:
                    server.send('4'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 9:
            server.send('3'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 1 or data3 == 4 or data3 == 6 or data3 == 8:
                server.send('7'.encode('utf-8'))
                continue

            elif data3 == 7:
                server.send('8'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 1 or data4 == 6:
                    server.send('4'.encode('utf-8'))
                    continue

                elif data4 == 4:
                    server.send('1'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 0:
            server.send('0'.encode('utf-8'))
            continue


#####################################################
    elif data1 == 5:
        server.send('1'.encode('utf-8'))
        data2 = getDataFromUser()
        if data2 == 2:
            server.send('8'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 3:
                server.send('7'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 6 or data4 == 9:
                    server.send('4'.encode('utf-8'))
                    continue

                elif data4 == 4:
                    server.send('9'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue
                
            elif data3 == 4:
                server.send('6'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 7 or data4 == 9:
                    server.send('3'.encode('utf-8'))
                    continue

                elif data4 == 3:
                    server.send('7'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 6:
                server.send('4'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 3 or data4 == 9:
                    server.send('7'.encode('utf-8'))
                    continue

                elif data4 == 7:
                    server.send('3'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 7:
                server.send('3'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 4 or data4 == 9:
                    server.send('6'.encode('utf-8'))
                    continue

                elif data4 == 6:
                    server.send('4'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 9:
                server.send('7'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 3 or data4 == 6:
                    server.send('4'.encode('utf-8'))
                    continue

                elif data4 == 4:
                    server.send('6'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 3:
            server.send('7'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 2 or data3 == 6 or data3 == 8 or data3 == 9:
                server.send('4'.encode('utf-8'))
                continue

            elif data3 == 4:
                server.send('6'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 2 or data4 == 9:
                    server.send('8'.encode('utf-8'))
                    continue

                elif data4 == 8:
                    server.send('2'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 4:
            server.send('6'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 2:
                server.send('8'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 3 or data4 == 9:
                    server.send('7'.encode('utf-8'))
                    continue

                elif data4 == 7:
                    server.send('3'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue
                
            elif data3 == 3:
                server.send('7'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 2 or data4 == 9:
                    server.send('8'.encode('utf-8'))
                    continue

                elif data4 == 8:
                    server.send('2'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 7:
                server.send('3'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 2 or data4 == 8:
                    server.send('9'.encode('utf-8'))
                    continue

                elif data4 == 9:
                    server.send('8'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 8:
                server.send('2'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 7 or data4 == 9:
                    server.send('3'.encode('utf-8'))
                    continue

                elif data4 == 3:
                    server.send('7'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 9:
                server.send('3'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 7 or data4 == 8:
                    server.send('2'.encode('utf-8'))
                    continue

                elif data4 == 2:
                    server.send('8'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 6:
            server.send('4'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 2 or data3 == 3 or data3 == 8 or data3 == 9:
                server.send('7'.encode('utf-8'))
                continue

            elif data3 == 7:
                server.send('3'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 8 or data4 == 9:
                    server.send('2'.encode('utf-8'))
                    continue

                elif data4 == 2:
                    server.send('8'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 7:
            server.send('3'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 4 or data3 == 6 or data3 == 8 or data3 == 9:
                server.send('2'.encode('utf-8'))
                continue

            elif data3 == 2:
                server.send('8'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 4 or data4 == 9:
                    server.send('6'.encode('utf-8'))
                    continue

                elif data4 == 6:
                    server.send('4'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 8:
            server.send('2'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 4 or data3 == 6 or data3 == 7 or data3 == 9:
                server.send('3'.encode('utf-8'))
                continue

            elif data3 == 3:
                server.send('7'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 6 or data4 == 9:
                    server.send('4'.encode('utf-8'))
                    continue

                elif data4 == 4:
                    server.send('6'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue



        elif data2 == 9:
            server.send('3'.encode('utf-8'))
            data3 = getDataFromUser()
            if data3 == 4 or data3 == 6 or data3 == 7 or data3 == 8:
                server.send('2'.encode('utf-8'))
                continue

            elif data3 == 2:
                server.send('8'.encode('utf-8'))
                data4 = getDataFromUser()
                if data4 == 6 or data4 == 7:
                    server.send('4'.encode('utf-8'))
                    continue

                elif data4 == 4:
                    server.send('6'.encode('utf-8'))
                    continue
                    
                elif data4 == 0:
                    server.send('0'.encode('utf-8'))
                    continue

            elif data3 == 0:
                server.send('0'.encode('utf-8'))
                continue


        elif data2 == 0:
            server.send('0'.encode('utf-8'))
            continue


#####################################################
    elif data1 == 0:
        server.send('0'.encode('utf-8'))
        continue

    else:
        server.send('0'.encode('utf-8'))
        continue
    

