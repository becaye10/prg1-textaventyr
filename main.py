# Här skriver du ditt 
import time
SpelarensNamn = input("vad vill du bli kallad? ")
time.sleep(1)
print("hej " + SpelarensNamn + " välkommen till ditt textäventyr")
time.sleep(1)
print("Du har precis krashat på en okänd planet och ditt skepp är paj!")
GåUt = input("Vill du gå ut eller stanna i skeppet och kolla runt? ")
if GåUt == "gå ut":
    print("Du märker att det inte går att andas och tvingas gå in i skeppet och hämta din mask ändå")
