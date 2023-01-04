def PrintSunday():
    print('You chose Suunday!\n')
def PrintMonday():
    print('You chose Monday!\n')
def PrintTuesday():
    print('You chose Tuesday!\n')
def PrintWednesday():
    print('You chose Wednesday!\n')
def PrintThrusday():
    print('You chose Thrusday!\n')
def PrintFriday():
    print('You chose Friday!\n')
def PrintSaturday():
    print('You chose Saturday!\n')
def Chose():
    print("e.d number betwwwn 0-7")
##    print("0:Sunday")
##    print("1:Monday")
##    print("2:Tuesday")
##    print("3:Wednesday")
##    print("4:Thrusday")
##    print("5:Friday")
##    print("6:Saturday")
##    print("7:Quit")
##    return
rohith={0:PrintSunday, 1:PrintMonday, 2:PrintTuesday, 3:PrintWednesday, 4:PrintThrusday, 5:PrintFriday, 6:PrintSaturday, }
selection=0
while True:
    if (selection>=7):break
    if selection<0:break
    Chose()
    selection=int(input("select a Day Option:"))
    if(selection>=0)and(selection<7):
        rohith[selection]()
