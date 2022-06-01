# userGUY.py


import socket
import threading


####################  SOCKET  ###################
serverip = 'yourip'
portUser = xxxx // change xxxx to int initialize port

server = socket.socket()            # สร้างตัวเชื่อม
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) 
server.connect((serverip, portUser))    # ฝั่ง server เป็น bind() 

# server.send('CONN|USERCLIENT|<<<<<<TEST FROM USERCLIENT>>>>>>'.encode('utf-8'))
# data_server = server.recv(1024).decode('utf-8')
# print('Status: ', data_server)


####################   GUI   ####################

from tkinter import *        

listButton = []
listX = [97, 275, 453, 97, 275, 453, 97, 275, 453]
listY = [66, 66, 66, 244, 244, 244, 422, 422, 422]

table = ["", "", "", "", "", "", "", "", ""]
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
listNumButton = [one, two, three, four, five, six, seven, eight, nine]

window = Tk()
window.title('Don\'t Win')

window.geometry("720x700+400+100")
window.configure(bg = "#4d6dde")


channelpng = PhotoImage(file = f"channel.png")

normalOpng = PhotoImage(file = f"normalO.png")
normalXpng = PhotoImage(file = f"normalX.png")

greenOpng = PhotoImage(file = f"greenO.png")
greenXpng = PhotoImage(file = f"greenX.png")

winHorizonpng = PhotoImage(file = f"winHorizon.png")
winVerticalpng = PhotoImage(file = f"winVertical.png")

newGamepng = PhotoImage(file = f"newGame.png")
newBG = PhotoImage(file = f"newbg720631.png")

def changeButtonToX(n):
    listButton[n-1].place(
    x = listX[n-1], y = listY[n-1],
    width = 0,
    height = 0)

    newX = Button(
        image = normalXpng)

    newX.place(
        x = listX[n-1], y = listY[n-1],
        width = 160,
        height = 160)

def changeButtonToO(n):
    listButton[n-1].place(
    x = listX[n-1], y = listY[n-1],
    width = 0,
    height = 0)

    newO = Button(
        image = normalOpng)

    newO.place(
        x = listX[n-1], y = listY[n-1],
        width = 160,
        height = 160)

def checkButtonToO(n):
    if n != 0:
        i = 1
        for r in listNumButton:
            if r != n:
                i = i + 1
            elif r == n:
                changeButtonToO(i)
                table[i-1] = "O"



def sendToServer(n):
    server.send(str(n).encode('utf-8'))
    dataBot = receiveDataBotFromServer()
    return int(dataBot)

def receiveDataBotFromServer():
    dataBotFromServer = server.recv(1024).decode('utf-8')
    return dataBotFromServer

def btnOnClicked(n):
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global listNumButton

    print(f"data {n}")

    if "X" in table:
        dataBot = sendToServer(n)
        checkButtonToO(dataBot)

    else:
        if n == 1 or n == 2 or n == 5:
            listNumButton = [one, two, three, four, five, six, seven, eight, nine]
            print(one)
            dataBot = sendToServer(n)
            checkButtonToO(dataBot)

        elif n == 3 or n == 6:
            one = 7
            two = 4
            three = 1
            four = 8
            five = 5
            six = 2
            seven = 9
            eight = 6
            nine = 3
            listNumButton = [one, two, three, four, five, six, seven, eight, nine]
            print(one)
            if n == 3:
                dataBot = sendToServer(1)
                checkButtonToO(dataBot)
                
            elif n == 6:
                dataBot = sendToServer(2)
                checkButtonToO(dataBot)
                

        elif n == 9 or n == 8:
            one = 9
            two = 8
            three = 7
            four = 6
            five = 5
            six = 4
            seven = 3
            eight = 2
            nine = 1
            listNumButton = [one, two, three, four, five, six, seven, eight, nine]
            print(one)
            if n == 9:
                dataBot = sendToServer(1)
                checkButtonToO(dataBot)
                
            elif n == 8:
                dataBot = sendToServer(2)
                checkButtonToO(dataBot)
                

        elif n == 7 or n == 4:
            one = 3
            two = 6
            three = 9
            four = 2
            five = 5
            six = 8
            seven = 1
            eight = 4
            nine = 7
            listNumButton = [one, two, three, four, five, six, seven, eight, nine]
            print(one)
            if n == 7:
                dataBot = sendToServer(1)
                checkButtonToO(dataBot)
                
            elif n == 4:
                dataBot = sendToServer(2)
                checkButtonToO(dataBot)
                

def btn1_clicked():   
    print("Button 1 Clicked")   
    changeButtonToX(1)
    btnOnClicked(one)
    table[0] = "X"
    checkWin()

def btn2_clicked():   
    print("Button 2 Clicked")
    changeButtonToX(2)   
    btnOnClicked(two)
    table[1] = "X"
    checkWin()

def btn3_clicked():   
    print("Button 3 Clicked")
    changeButtonToX(3)
    btnOnClicked(three)
    table[2] = "X"
    checkWin()

def btn4_clicked():   
    print("Button 4 Clicked")
    changeButtonToX(4)
    btnOnClicked(four)
    table[3] = "X"
    checkWin()

def btn5_clicked():   
    print("Button 5 Clicked")
    changeButtonToX(5)
    btnOnClicked(five)
    table[4] = "X"
    checkWin()

def btn6_clicked():   
    print("Button 6 Clicked")
    changeButtonToX(6)
    btnOnClicked(six)
    table[5] = "X"
    checkWin()

def btn7_clicked():   
    print("Button 7 Clicked")
    changeButtonToX(7)
    btnOnClicked(seven)
    table[6] = "X"
    checkWin()

def btn8_clicked():   
    print("Button 8 Clicked")
    changeButtonToX(8)
    btnOnClicked(eight)
    table[7] = "X"
    checkWin()

def btn9_clicked():   
    print("Button 9 Clicked")
    changeButtonToX(9)
    btnOnClicked(nine)
    table[8] = "X"
    checkWin()
    
def newGame():
    restart_program()
    
canvas = Canvas(
    window,
    bg = "#4d6dde",
    height = 700,
    width = 720,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
##########################

b1 = Button(
    image = channelpng,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn1_clicked,   
    relief = "flat")

b1.place(
    x = listX[0], y = listY[0],
    width = 160,
    height = 160)

listButton.append(b1)
##########################
b2 = Button(
    image = channelpng,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn2_clicked,
    relief = "flat")

b2.place(
    x = listX[1], y = listY[1],
    width = 160,
    height = 160)

listButton.append(b2)
##########################
b3 = Button(
    image = channelpng,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn3_clicked,
    relief = "flat")

b3.place(
    x = listX[2], y = listY[2],
    width = 160,
    height = 160)

listButton.append(b3)
##########################
b4 = Button(
    image = channelpng,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn4_clicked,
    relief = "flat")

b4.place(
    x = listX[3], y = listY[3],
    width = 160,
    height = 160)

listButton.append(b4)
##########################
b5 = Button(
    image = channelpng,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn5_clicked,
    relief = "flat")

b5.place(
    x = listX[4], y = listY[4],
    width = 160,
    height = 160)

listButton.append(b5)
##########################
b6 = Button(
    image = channelpng,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn6_clicked,
    relief = "flat")

b6.place(
    x = listX[5], y = listY[5],
    width = 160,
    height = 160)

listButton.append(b6)
##########################
b7 = Button(
    image = channelpng,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn7_clicked,
    relief = "flat")

b7.place(
    x = listX[6], y = listY[6],
    width = 160,
    height = 160)

listButton.append(b7)
##########################
b8 = Button(
    image = channelpng,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn8_clicked,
    relief = "flat")
    
b8.place(
    x = listX[7], y = listY[7],
    width = 160,
    height = 160)

listButton.append(b8)
##########################
b9 = Button(
    image = channelpng,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn9_clicked,
    relief = "flat")

b9.place(
    x = listX[8], y = listY[8],
    width = 160,
    height = 160)
    
listButton.append(b9)
##########################
# newGamepng = PhotoImage(file = f"newGame.png")
ngButton = Button(
    image = newGamepng,
    borderwidth = 0,
    highlightthickness = 0,
    command = newGame,
    relief = "flat")

ngButton.place(
    x = 206, y = 631,
    width = 285,
    height = 46)

##################  THREAD CHECKING  ##################
def changeToGreenO(pX, pY):
    newGreenO = Button(
        image = greenOpng)

    newGreenO.place(
        x = pX, y = pY,
        width = 160,
        height = 160)

def changeToGreenX(pX, pY):
    newGreenX = Button(
        image = greenXpng)

    newGreenX.place(
        x = pX, y = pY,
        width = 160,
        height = 160)

def lineHorizon(pX, pY):
    winH = Button(
        image = winHorizonpng)

    winH.place(
        x = pX, y = pY,
        width = 600,
        height = 25)

def lineVertical(pX, pY):
    winV = Button(
        image = winVerticalpng)

    winV.place(
        x = pX, y = pY,
        width = 25,
        height = 600)

def checkWinHorizon1():
    if table[0] == table[1] and table[0] == table[2] and table[0] != "":
        lineHorizon(55, 133)

def checkWinHorizon2():
    if table[3] == table[4] and table[3] == table[5] and table[3] != "":
        lineHorizon(55, 312)
        
def checkWinHorizon3():
    if table[6] == table[7] and table[6] == table[8] and table[6] != "":
        lineHorizon(55, 489)

def checkWinVertical1():
    if table[0] == table[3] and table[0] == table[6] and table[0] != "":
        lineVertical(164, 23)

def checkWinVertical2():
    if table[1] == table[4] and table[1] == table[7] and table[1] != "":
        lineVertical(344, 23)

def checkWinVertical3():
    if table[2] == table[5] and table[2] == table[8] and table[2] != "":
        lineVertical(520, 23)

def checkWinSlant():
    if table[0] == table[4] and table[0] == table[8] and table[0] != "":
        if table[0] == "X":
            changeToGreenX(listX[0], listY[0])
            changeToGreenX(listX[4], listY[4])
            changeToGreenX(listX[8], listY[8])
        elif table[0] == "O":
            changeToGreenO(listX[0], listY[0])
            changeToGreenO(listX[4], listY[4])
            changeToGreenO(listX[8], listY[8])

def checkWinBackSlant():
    if table[2] == table[4] and table[2] == table[6] and table[2] != "":
        if table[2] == "X":
            changeToGreenX(listX[2], listY[2])
            changeToGreenX(listX[4], listY[4])
            changeToGreenX(listX[6], listY[6])
        elif table[2] == "O":
            changeToGreenO(listX[2], listY[2])
            changeToGreenO(listX[4], listY[4])
            changeToGreenO(listX[6], listY[6])

##### Multitasking

def checkWin():
    task1 = threading.Thread(target=checkWinHorizon1)   
    task2 = threading.Thread(target=checkWinHorizon2)   
    task3 = threading.Thread(target=checkWinHorizon3)   
    task4 = threading.Thread(target=checkWinVertical1)   
    task5 = threading.Thread(target=checkWinVertical2)   
    task6 = threading.Thread(target=checkWinVertical3)   
    task7 = threading.Thread(target=checkWinSlant)   
    task8 = threading.Thread(target=checkWinBackSlant)  

    task1.start()
    task2.start()
    task3.start()
    task4.start()
    task5.start()
    task6.start()
    task7.start()
    task8.start()   

def restart_program():
    dataBot = sendToServer(0)
    if dataBot == 0:
        print("Bot Reset Complete")
        
    global listButton
    global table
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global listNumButton
    
    listButton = []

    table = ["", "", "", "", "", "", "", "", ""]
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    listNumButton = [one, two, three, four, five, six, seven, eight, nine]

    newBackground= Button(
        image = newBG)

    newBackground.place(
        x = 0, y = 0,
        width = 720,
        height = 631)
    ##########################

    b1 = Button(
        image = channelpng,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn1_clicked,   
        relief = "flat")

    b1.place(
        x = listX[0], y = listY[0],
        width = 160,
        height = 160)

    listButton.append(b1)
    ##########################
    b2 = Button(
        image = channelpng,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn2_clicked,
        relief = "flat")

    b2.place(
        x = listX[1], y = listY[1],
        width = 160,
        height = 160)

    listButton.append(b2)
    ##########################
    b3 = Button(
        image = channelpng,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn3_clicked,
        relief = "flat")

    b3.place(
        x = listX[2], y = listY[2],
        width = 160,
        height = 160)

    listButton.append(b3)
    ##########################
    b4 = Button(
        image = channelpng,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn4_clicked,
        relief = "flat")

    b4.place(
        x = listX[3], y = listY[3],
        width = 160,
        height = 160)

    listButton.append(b4)
    ##########################
    b5 = Button(
        image = channelpng,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn5_clicked,
        relief = "flat")

    b5.place(
        x = listX[4], y = listY[4],
        width = 160,
        height = 160)

    listButton.append(b5)
    ##########################
    b6 = Button(
        image = channelpng,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn6_clicked,
        relief = "flat")

    b6.place(
        x = listX[5], y = listY[5],
        width = 160,
        height = 160)

    listButton.append(b6)
    ##########################
    b7 = Button(
        image = channelpng,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn7_clicked,
        relief = "flat")

    b7.place(
        x = listX[6], y = listY[6],
        width = 160,
        height = 160)

    listButton.append(b7)
    ##########################
    b8 = Button(
        image = channelpng,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn8_clicked,
        relief = "flat")
        
    b8.place(
        x = listX[7], y = listY[7],
        width = 160,
        height = 160)

    listButton.append(b8)
    ##########################
    b9 = Button(
        image = channelpng,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn9_clicked,
        relief = "flat")

    b9.place(
        x = listX[8], y = listY[8],
        width = 160,
        height = 160)
        
    listButton.append(b9)


window.resizable(False, False)
window.mainloop()













