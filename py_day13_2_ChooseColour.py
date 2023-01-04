def PrintBlack():
    print('You chose Black!\n')
def PrintRed():
    print('You chose Red!\n')
def PrintGreen():
    print('You chose Green!\n')
def PrintPink():
    print('You chose Pink!\n')
def ChoseColour():
    print("0:Black")
    print("1:Red")
    print("2:Green")
    print("3:pink")
    print("Quit")
    return
rohith={0:PrintBlack, 1:PrintRed, 2:PrintGreen, 3:PrintPink }
selection=0
while True:
    if (selection>=5):break
    if selection<0:break
    ChoseColour()
    selection=int(input("select a colour option:"))
    if(selection>=0)and(selection<4):
        rohith[selection]()
