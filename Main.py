import time
from datetime import datetime
import random

Parkhaus_Parkplätze = 10
parkzeit_start = []
Parkschein = []

def freier_platz():
    while True:
        nummer = random.randint(1, 10)
        if nummer not in Parkschein:
            return nummer

def status_parkhaus():
    if Parkhaus_Parkplätze >= 10:
        print("Alle Parkplätze verfügbar")
    if Parkhaus_Parkplätze <= 0:
        print("Keine Parkplätze verfügbar")
    else:
        print("Es sind noch ",(Parkhaus_Parkplätze)," Parkplätze verfügbar")

def format_zeit(sekunden):
    """Rundet auf nächste volle Stunde, wenn angebrochen"""
    minuten_gesamt = sekunden / 60
    # Wenn auch nur 1 Sekunde angebrochen → nächste Stunde!
    stunden = int(minuten_gesamt) // 60 + 1 if minuten_gesamt % 60 > 0 else int(minuten_gesamt) // 60
    minuten = 0  # Immer auf volle Stunde → 00 Minuten
    return f"{stunden:02d}:{minuten:02d}"

def Einfahrt():
    global Parkhaus_Parkplätze
    Parkhaus_Parkplätze -= 1

def Ausfahrt():
    global Parkhaus_Parkplätze
    Parkhaus_Parkplätze += 1

def main():
    choice = "on"
    while choice != "off":
        print("\n=== Parkhaus ===")
        print("Wählen sie die gewünschte Aktion aus\n\n- Parkhaus getreten (enter)\n- Parkhaus verlassen (exit)\n- Status Parkhaus (status)\n- Wartungsmodus (maintenance)\n- System herunterfahren(off)")
        choice = input("\nBereich auswählen:")
        if choice == "enter":
            if 10 >= Parkhaus_Parkplätze > 0:
                Schein = freier_platz()
                Parkschein.append(Schein)
                parkzeit_start.append(time.time())
                print("Ihre Parknummer lautet ",Schein,"")
                print("Beginn der Parkzeit um ",(time.strftime("%H:%M")),"")
                time.sleep(4)
                print("Tor öffnet sich")
                time.sleep(1)
                print("Fahrzeug fährt ins Parkhaus")
                Einfahrt()
                time.sleep(1)
                print("Tor schließt sich")
                time.sleep(1)
                continue
            else:
                print("Keine Parkplätze verfügbar")
                time.sleep(1)
                continue
        elif choice == "exit":
            if Parkhaus_Parkplätze >= 10:
                print("Parkhaus ist Leer")
                time.sleep(2)
            else:
                parknummer = int(input("Bitte geben sie ihre Parknummer ein: "))
                if parknummer not in Parkschein:
                    print("Parknummer exestiert nicht.")
                    time.sleep(2)
                    continue
                platz = Parkschein.index(parknummer)
                differenz = time.time() - parkzeit_start[platz]
                print("Sie haben für",(format_zeit(differenz)),"h geparkt.")
                time.sleep(4)
                print("Tor öffnet sich")
                time.sleep(1)
                print("Fahrzeug fährt aus Parkhaus heraus")
                Ausfahrt()
                time.sleep(1)
                print("Tor schließt sich")
                time.sleep(1)
            continue
        elif choice == "status":
            status_parkhaus()
            time.sleep(4)
            continue
        elif choice == "maintenance":
            continue
        elif choice == "off":
            frage = input("Sind sie sicher das sie das System beenden wollen? (y/n)").lower()
            if frage == "y":
                print("System wird heruntergefahren")
            elif frage == "n":
                choice = "on"
            else:
                print("\nEingabe fehlerhaft! Vorgang wird abgebrochen.\n")
                time.sleep(2)
                choice = "on"
            
        else:
            print("\nUngültige eingabe! Bitte korrigieren!\n")
            time.sleep(2)
            choice = "on"

if __name__ == "__main__":
    main()