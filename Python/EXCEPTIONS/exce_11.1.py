zahl1 = float(input("Zahl 1: "))
zahl2 = float(input("Zahl 2: "))
ergebnis = 0.0
operator = input("Operator: ")

try:
    if operator == "+":
        try:
            ergebnis = zahl1 + zahl2,
        except:
            print("Fehler bei der Addition")

    if operator == "-":
        try:
            ergebnis = zahl1 - zahl2,
        except:
            print("Fehler bei der Subtraktion")

    if operator == "*":
        try:
            ergebnis = zahl1 * zahl2,
        except:
            print("Fehler bei der Multiplikation")

    if operator == "/":
        try:
            ergebnis = zahl1 / zahl2,
        except:
            print("Fehler bei der Division")
except:
    print("Fehler!")