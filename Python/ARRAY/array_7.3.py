array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

eingabe = input("Bitte geben Sie eine Zahl von 0-9 ein: ")

if int(eingabe) in array:
    print("Die Zahl ist in der Liste an der", array.index(int(eingabe))+1, ". Stelle.")
else:
    print("Die Zahl ist nicht in der Liste.")