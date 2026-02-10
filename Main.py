import time
from datetime import datetime

Parkhaus_Parkplätze = 10
parkzeit_start = []
Parkschein = []
    
def status_parkhaus():
    if Parkhaus_Parkplätze >= 10:
        print("Alle Parkplätze verfügbar")
    if Parkhaus_Parkplätze <= 0:
        print("Keine Parkplätze verfügbar")
    else:
        print("Es sind noch ",(Parkhaus_Parkplätze)," Parkplätze verfügbar")
        print(Parkschein)

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
                freier_platz = Parkhaus_Parkplätze
                Parkschein.append(Parkhaus_Parkplätze)
                parkzeit_start.append(time.time())
                print("Ihre Parknummer lautet ",freier_platz,"")
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
                input("Drücke ENTER zum fortfahren")
                continue
        elif choice == "exit":
            if Parkhaus_Parkplätze >= 10:
                print("Parkhaus ist Leer")
                input("Drücke ENTER zum fortfahren")
            else:
                parknummer = int(input("Bitte geben sie ihre Parknummer ein: "))
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
            input("Drücke ENTER zum fortfahren")
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
                input("Drücke ENTER um zum Menü zu gelangen")
                choice = "on"
            
        else:
            print("\nUngültige eingabe! Bitte korrigieren!\n")
            input("Drücke ENTER zum wiederholen")
            choice = "on"

if __name__ == "__main__":
    main()