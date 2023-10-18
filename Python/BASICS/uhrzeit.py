start_stunden = int(input("Bitte Startpunkt eingeben (Stunden): \n"))
start_minuten = int(input("Bitte Startpunk eingeben (Minuten): \n"))
event_dauer = int(input("Bitte Eventdauer eingeben (in Minuten): \n"))

start_minuten += event_dauer
tage = 0
while (start_minuten >= 60):
    start_stunden += 1
    start_minuten -= 60
if (start_stunden >= 24):
    tage += 1
    start_stunden -= 24

print("Ende: ", tage, ":", start_stunden, ":", start_minuten)