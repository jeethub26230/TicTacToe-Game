from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

ActivePlayer = 1
p1 = [] #P1 Selection
p2 = [] #P2 Selection
count = 0

def Game():
    #Global Variables

    box = Tk()
    box.title('TicTacToe! : Player 1')
    # Buttons
    def buc(id):
        global ActivePlayer
        global p1
        global p2
        global count
        if(ActivePlayer == 1):
            AfterClick(id,'X')
            p1.append(id)
            box.title('TicTacToe! : Player 2')
            ActivePlayer = 2
            print("P1:{}".format(p1))

        elif(ActivePlayer == 2):
            AfterClick(id, 'O')
            p2.append(id)
            box.title('TicTacToe! : Player 2')
            ActivePlayer = 1
            print("P2:{}".format(p2))
        Who_won()

    def AfterClick(id,PSymbol):
        fnt = Font(family = 'verdana',size = 20 )
        if(id ==  1):
            bu1.config(text=PSymbol,font = fnt, fg = 'blue')
            bu1["state"] = 'disabled'
        elif(id ==  2):
            bu2.config(text=PSymbol,font = fnt)
            bu2["state"] = 'disabled'
        elif (id == 3):
            bu3.config(text=PSymbol,font = fnt)
            bu3["state"] = 'disabled'
        elif (id == 4):
            bu4.config(text=PSymbol,font = fnt)
            bu4["state"] = 'disabled'
        elif (id == 5):
            bu5.config(text=PSymbol,font = fnt)
            bu5["state"] = 'disabled'
        elif (id == 6):
            bu6.config(text=PSymbol,font = fnt)
            bu6["state"] = 'disabled'
        elif (id == 7):
            bu7.config(text=PSymbol,font = fnt)
            bu7["state"] = 'disabled'
        elif (id == 8):
            bu8.config(text=PSymbol,font = fnt)
            bu8["state"] = 'disabled'
        elif (id == 9):
            bu9.config(text=PSymbol,font = fnt)
            bu9["state"] = 'disabled'

        print("ID:{}".format(id))

    def Who_won():
        # global p1
        # global p2
        global count
        sec11 = [1,2,3]
        sec12 = [4,5,6]
        sec13 = [7,8,9]
        sec21 = [1,4,7]
        sec22 = [2,5,8]
        sec23 = [3,6,9]
        sec31 = [1,5,9]
        sec32 = [3,5,7]
        sec0 = [sec11,sec12,sec13,sec21,sec22,sec23,sec31,sec32 ]
        count += 1

        for l in sec0:
            result1 = all(item in p1 for item in l)
            result2 = all(item in p2 for item in l)
            if(result1 is True):
                messagebox.showinfo('Game Over.!',"'Player1 Win!'")
                break
            elif(result2 is True):
                messagebox.showinfo('Game Over.!', "'Player2 Win!'")
                break
        if (count is 9):
            result = result1 or result2
            if (result is False):
                messagebox.showinfo("Game Over", 'Replay')
                box.destroy()
                Game()
        print("Count :{0}\nResult1 :{1}\nResult2:{2} ".format(count,result1,result2))

    bu1 = Button(box,text = " ",command = lambda : buc(1))
    bu1.grid(row = 0 , column = 0, ipadx = 40 , ipady = 40)

    bu2 = Button(box,text = " ",command = lambda : buc(2))
    bu2.grid(row = 0 , column = 1, ipadx = 40 , ipady = 40)

    bu3 = Button(box,text = " ",command = lambda : buc(3))
    bu3.grid(row = 0 , column = 2, ipadx = 40 , ipady = 40)

    bu4 = Button(box,text = " ",command = lambda : buc(4))
    bu4.grid(row = 1 , column = 0, ipadx = 40 , ipady = 40)

    bu5 = Button(box,text = " ",command = lambda : buc(5))
    bu5.grid(row = 1 , column = 1, ipadx = 40 , ipady = 40)

    bu6 = Button(box,text = " ",command = lambda : buc(6))
    bu6.grid(row = 1 , column = 2, ipadx = 40 , ipady = 40)

    bu7 = Button(box,text = " ",command = lambda : buc(7))
    bu7.grid(row = 2 , column = 0, ipadx = 40 , ipady = 40)

    bu8 = Button(box,text = " ",command = lambda : buc(8))
    bu8.grid(row = 2 , column = 1, ipadx = 40 , ipady = 40)

    bu9 = Button(box,text = " ",command = lambda : buc(9))
    bu9.grid(row = 2 , column = 2, ipadx = 40 , ipady = 40)

    box.mainloop()

Game()
