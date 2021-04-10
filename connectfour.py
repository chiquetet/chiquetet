"""
Project #1: A Simple Game
CONNECT FOUR
"""


import os
from colorama import init
from termcolor import colored, cprint
init()
list = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
#print(lista)

player = 1
def drawField(field):

    for row in range(11): #0,1,2,3,4,5,6,7,8,9
        if row%2 == 0:
            practicalRow = int(row/2)
            #print(practicalRow)
            for column in range(13):
                
                if column%2 == 0:

                    practicalColumn = int(column/2)
                    
                    if column != 12:
                        print(field[practicalColumn][practicalRow], end = "")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end = "")
        else:
            print("-------------")

drawField(list)

def whosWin(list,piece):
    #horizontal check    
        for c in range(4):#0,1,2,3,4
            for i in range(5,-1,-1):#5,4,3,2,1,0
                if not list[c][i] == " ":
                    if list[c][i] == list[c+1][i] and list[c][i] == list[c+2][i] and list[c][i] == list[c+3][i]:
                        return True
        #vertical check
        for c in range(7):#0,1,2,3,4,5,6
            for i in range(5,2,-1):#5,4,3
                if not list[c][i] == " ":
                    if list[c][i] == list[c][i-1] and list[c][i] == list[c][i-2] and list[c][i] == list[c][i-3]:
                        return True
                
        #Diagona up Check
        for c in range(4): #0,1,2,3
            for i in range(5,2,-1):
                if not list[c][i] == " ":
                    if list[c][i] == list[c+1][i-1] and list[c][i] == list[c+2][i-2] and list[c][i] == list[c+3][i-3]:
                        return True

        #Diagonal Down Check
        for c in range(3,-1,-1):#3,2,1,0
            for i in range(5,2,-1):#5,4,3
                if not list[c][i] == " ":
                    if list[c][i] == list[c-1][i-1] and list[c][i] == list[c-2][i-2] and list[c][i] == list[c-3][i-3]:
                        return True
def isValidMove(column_no):
    if column_no >=1 and column_no <=7:
        return True
    else:
        return False



while(True):
    if player== 1:
        piece = colored("X",'red')
        print("-- PLAYER",player,"TURN --")
        chooseColumn = int(input("choose your turn using the numbers between 1 and 7 : "))
        while isValidMove(chooseColumn) == False:
            chooseColumn = int(input("choose your turn using the numbers between 1 and 7 : "))
            isValidMove(chooseColumn)
        for i in range(5,-1,-1):
            if list[chooseColumn-1][i] == " ":
                
                list[chooseColumn-1][i] = piece
                break
        #os.system("cls")       
        drawField(list)

        if whosWin(list,piece):
            print("THE WINNER IS ",player)
            break
            
        player = 2
    
    else:
        piece = colored("O",'blue')
        print("-- PLAYER",player,"TURN --")
        chooseColumn = int(input("choose your turn using the numbers between 1 and 7 : "))
        while isValidMove(chooseColumn) == False:
            chooseColumn = int(input("choose your turn using the numbers between 1 and 7 : "))
            isValidMove(chooseColumn)
        for i in range(5,-1,-1):
            if list[chooseColumn-1][i] == " ":
                list[chooseColumn-1][i] = piece
                break
            
        #os.system("cls")       
        drawField(list)
        if whosWin(list,piece):

            print("THE WINNER IS ",player)
            break
            
        player = 1
    




