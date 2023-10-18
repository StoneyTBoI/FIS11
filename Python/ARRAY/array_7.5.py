zahlenarray = [["#" for x in range(3)] for y in range(5)]

eingabe = input("Bitte geben Sie eine Zahl von 0-9 ein: ")

if eingabe == "0":
    for i in range(1, 4):
        zahlenarray[i][1] = " "
elif eingabe == "1":
    for i in range(5):
        zahlenarray[i][0] = " "
    for i in range(5):
        zahlenarray[i][1] = " "
elif eingabe == "2":
    zahlenarray[1][1] = " "
    zahlenarray[2][1] = " "
    zahlenarray[0][2] = " "
    zahlenarray[1][2] = " "
elif eingabe == "5":
    zahlenarray[1][1] = " "
    zahlenarray[1][2] = " "
    zahlenarray[3][0] = " "
    zahlenarray[3][1] = " "
    

for print_array in zahlenarray:
    print(" ".join(print_array))