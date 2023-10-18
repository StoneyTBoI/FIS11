eingabe = input("Gib ein Wort ein: ")
eingabe = eingabe.lower()
eingabe = eingabe.replace(" ", "")
palindrom = ""

for buchstabe in eingabe:
    palindrom = buchstabe + palindrom

if eingabe == palindrom:
    print("Das eingegebene Wort ist ein Palindrom.")
else:
    print("Das eingegebene Wort ist kein Palindrom.")
