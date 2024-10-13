import os
import sys
from getkey import getkey, keys # https://github.com/TheIceBergBot/getkey
from bus import Bus

#|____________________MENY/NAVIGATIONSLOGIK___________________|#

def display_menu(menu: list, title: str): 
    menu_selection = 0 # Initierar variabel för valt index

    while True:
        os.system('clear') #Rensar terminalskärmen. OBS: 'clear' i bash/zsh - ändra argument till 'cls' i Windows. 
        print("\x1b[?25l") # Gömmer pekaren i CLI output.
        print(title)

        # enumerate() = Itererar genom lista med dubbla variabler - listans index samt respektive element däri.
        for index, choice in enumerate(menu):
            if index == menu_selection:
                print(f"{choice}←") # Skriver ut nuvarande position i menyn med visuell markering.
            else:
                print(choice)
        
        key_press = getkey() # Registrerar nedtryckt tangent.

        # Logik för att navigera menyn.
        if key_press == keys.DOWN and menu_selection + 1 != len(menu):
            menu_selection += 1
        elif key_press == keys.UP and not (menu_selection == 0):
            menu_selection -= 1
        elif key_press == keys.ENTER:
            return menu_selection # returnerar uppdaterat menyval(index) till programloopen.

#|______________________PROGRAMLOOP_________________________|#

def run():
    my_bus = Bus() # initierat objekt för klassen Bus.

    main_menu = ["1. Påstigning\t\t", "2. Avstigning\t\t", "3. Statistik\t\t", "4. Peta på någon\t", "5. DEV: random_list\t", "6. Avsluta\t\t"]
    sub_menu1 = ["3.1 Alla passagerare\t\t", "3.2 Sortera passagerare\t\t", "3.3 Beräkningar\t\t\t", "3.4 Könsfördelning\t\t", "3.5 Huvudmeny\t\t\t"]
    sub_menu2 = ["3.3.1 Total ålder\t", "3.3.2 Medelålder\t", "3.3.3 Äldst i bussen\t", "3.3.4 Hitta ålder\t", "3.3.5 Bakåt\t\t"]

    while True:
        os.system('clear')
        selection = display_menu(main_menu, "-- Välkommen till Buss-simulatorn --\n") # Anropar menyfunktion med menylista samt menytitel.

        if selection == 0: # PÅSTIGNING
            os.system('clear')
            print(my_bus.add_passenger())
            print("--------------------------------")
            input("Tryck ENTER för att fortsätta...")
            
        elif selection == 1: # AVSTIGNING
            os.system('clear')
            my_bus.get_off()
            print("--------------------------------")
            input("Tryck ENTER för att fortsätta...")

        elif selection == 2: # STATISTIK --> UNDERMENY 1

            while True:
                os.system('clear')
                sub_selection = display_menu(sub_menu1, "-- Resenärsdata --\n")

                if sub_selection == 0: # ALLA PASSAGERARE
                    os.system('clear')
                    print("Nuvarande passagerare på bussen:\n")
                    print(my_bus.print_bus())
                    print("--------------------------------")
                    input("Tryck ENTER för att fortsätta...")

                elif sub_selection == 1: # SORTERAD PASSAGERARLISTA
                    os.system('clear')
                    print(f"Nuvarande passagerare sorterade i stigande ålder:\n\n{my_bus.sort_bus()}")
                    print("--------------------------------")
                    input("Tryck ENTER för att fortsätta...")

                elif sub_selection == 2: # BERÄKNINGAR --> UNDERMENY 2

                    while True:
                        sub_selection2 = display_menu(sub_menu2, "-- Beräkningar --\n")

                        if sub_selection2 == 0: # Total ålder
                            os.system('clear')
                            print(f"Passagerarnas totala ålder är {my_bus.calc_total_age()} år.")
                            print("--------------------------------")
                            input("Tryck ENTER för att fortsätta...")

                        elif sub_selection2 == 1: # Medelålder
                            os.system('clear')
                            average_age = my_bus.calc_average_age()
                            if average_age == None:
                                print("Bussen har inga passagerare.")
                            else:
                                print(f"Passagerarnas medelålder är {average_age} år.")
                            print("--------------------------------")
                            input("Tryck ENTER för att fortsätta...")

                        elif sub_selection2 == 2: # Äldst i bussen
                            os.system('clear')
                            print(f"Den äldsta passageraren i bussen är {my_bus.max_age()} år gammal.")
                            print("--------------------------------")
                            input("Tryck ENTER för att fortsätta...")
                        
                        elif sub_selection2 == 3: # Hitta ålder
                            os.system('clear')
                            print(f'{my_bus.find_age()}\n')
                            print("--------------------------------")
                            input("Tryck ENTER för att fortsätta...")                            

                        elif sub_selection2 == 4: # Bakåt i menyn
                            break

                elif sub_selection == 3: # KÖNSFÖRDELNING
                    os.system('clear')
                    my_bus.print_gender()
                    print("--------------------------------")
                    input("Tryck ENTER för att fortsätta...")        

                elif sub_selection == 4: # HUVUDMENY
                    break

        elif selection == 3: # PETA PÅ NÅGON
            os.system('clear')
            my_bus.poke()
            input()

        elif selection == 4: # TESTLISTA - genererar listor med passagerares ålder/kön.
            my_bus._random_passengers()

        elif selection == 5: # AVSLUTA PROGRAM
            sys.exit()
        print("\x1b[?25h") # visar pekaren igen (CLI)

# Startar programmet genom att anropa run().
def main():
    os.system('clear')
    print("\x1b[?25l")
    print("\t\t\tTor-Tor Touring")
    print("=========================================================================")
    print("== Alltid på fel plats, vid fel tillfälle och med helt fel utrustning! ==")
    input("\n# Programmerat av: Alexander Skoog 2024 för kursen Programmering 1 Hermods.")
    run()

if __name__ == "__main__": # Kontrollerar att koden körs ur denna fil, och inte försöker köras som en modul någon annanstans ifrån.
    main() # Om sant börjar programmet här.
