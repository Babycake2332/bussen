import os
import random
from passenger import Passenger

class Bus:
    passengers: int = [] # Initiering av passagerarlista
    passenger_gender: str = [] # Initiering av passagerares kön, motsvarar index i listan passengers.
    max_passengers: int = 22 # HÄR ÄNDRAR DU MAX ANTAL PASSAGERARE PÅ BUSSEN

#|_________PASSAGERARE AV/PÅ__________|#

    def add_passenger(self):
        new_passenger = 0 # Initiering av variabel för att ta emot användarinmatning.

        if len(self.passengers) >= self.max_passengers:
            os.system('clear')
            return "Bussen är fullsatt. Vänligen invänta avstigande passagerare.\n"

        while True:
            try: # Felhantering av inmatad datatyp samt fördefinierad avgränsning.
                os.system('clear')
                new_passenger = int(input("Passagerare, hur gammal är du? > "))
                if new_passenger < 0 or new_passenger > 110: # Kontrollerar att användarinmatning är inom en realistisk avgränsning.
                    print("\nÄr du en vampyr? Vänligen befinn dig i en rimlig ålder.")
                    input("\nFortsätt...")
                    continue
            except ValueError: # Om new_passenger inte är ett heltal.
                print("\nVänligen ange ett giltigt nummer.")
                input("\nFortsätt...")
                continue
            break

        while True:    
            os.system('clear')
            new_passenger_gender = str(input("Vilken är din könstillhörighet? (man/kvinna): ")).lower().strip() #Inmatning, små bokstäver utan eventuell whitespace.
            if new_passenger_gender not in ['man', 'kvinna']:
                print("\nVänligen fyll i din könstillhörighet.")
                input("\nFortsätt...")
                continue
            break
        
        self.passengers.append(new_passenger) # Lägger till värde i slutet på ålderslistan.
        self.passenger_gender.append(new_passenger_gender) # Lägger till värde i slutet på könstillhörighetslistan.
        return "\nVälkommen ombord!"

    def get_off(self): # Tar slumpmässigt bort passagerare från bussen.
        try:
            index = random.randint(0, len(self.passengers) - 1) # Slumpar indextal för avstigning.
            print(f"En {self.passengers[index]}-årig {self.passenger_gender[index]} klev av bussen vid hållplatsen.")
            del self.passengers[index] # tar bort element vid index ur listorna passengers och passenger_gender.
            del self.passenger_gender[index]
        except ValueError:
            print("Inga passagerare finns kvar på bussen.")
  

#|___________BERÄKNINGAR___________|#


    def calc_total_age(self): # Beräknar passagerarnas totala ålder.
        total_age = 0
        for _, age in enumerate(self.passengers):
            total_age += age
        return total_age


    def calc_average_age(self): # Beräknar passagerarnas medelålder.
        try:
            return round((self.calc_total_age() / len(self.passengers)), 2) # Returnerar kvot av metod och lista, avrundat till 2 decimaler.
        except ZeroDivisionError:
            return 'Inga passagerare finns på bussen.'

    def max_age(self): # Hittar den äldsta passageraren.
        current_oldest = 0
        for age in self.passengers:
            if age > current_oldest:
                current_oldest = age
        return current_oldest

    def find_age(self): # Hitta passagerares ålder inom ett åldersspann.
        filtered_list = [] # Initierar lista för att hålla resultat av iteration i passagerarlista.
        age_range = 0 # Initierad variabel för användarinmatning

        while True:
            os.system('clear')
            try:
                # Forcerad datatyp för att minimera valmöjligheter hos användaren.
                age_range = int(input("Följande resenärskategorier finns att söka:\n"
                            "1. Barn - 2. Ungdom - 3. Vuxen - 4. Senior\n\n"
                            "Vänligen skriv in numret på den kategori passagerare du önskar visa:  "))
                if age_range not in [1, 2, 3, 4]:
                    raise ValueError # Lyfter nedan felhantering tillbaka till anropare om ovan kontroll är FALSE.
            except ValueError:
                os.system('clear')
                print("Vänligen skriv in en giltig siffra (1 - 4).\n")
                input("Tryck ENTER för att fortsätta...")
                continue
            break
        # Kontrollerar användarens val och hämtar rätt åldrar ur passagerarlistan och tilldelar dessa till ny lista.
        if age_range == 1:
            for i in self.passengers:
                if i <= 6:
                    filtered_list.append(i)
        elif age_range == 2:
            for i in self.passengers:
                if i > 6 and i < 20:
                    filtered_list.append(i)
        elif age_range == 3:
            for i in self.passengers:
                if i >= 20 and i < 70:
                    filtered_list.append(i)
        elif age_range == 4:
            for i in self.passengers:
                if i >= 70:
                    filtered_list.append(i)

        return sorted(filtered_list) # Sorterar listan som returneras.

#|__________MANIPULERING AV LISTOR___________|#

    def print_bus(self): # Skriver ut listan med passagerare.
            return self.passengers


    def sort_bus(self):
        sorted_list = self.passengers[:] # sparar en lokal kopia av listan med slicing ([start:end:step])
    
    # Bubble sort - jämför och flyttar element i listan om de är på fel plats enligt kontrollsatsen.
        for i in range(len(sorted_list)):
            for j in range(0, len(sorted_list) - i - 1):
                if sorted_list[j] > sorted_list[j + 1]:
                    # temporär variabel för att skifta värden i listan
                    temp = sorted_list[j]
                    sorted_list[j] = sorted_list[j+1]
                    sorted_list[j+1] = temp
        return sorted_list


    def print_gender(self): # Skriver ut lista med passagerares plats i bussen (index), ålder samt kön (lista[index]).
        passenger_index = 1
        while True:
            for i, age in enumerate(self.passengers):
                print(f"Passagerare på sittplats {passenger_index} är en {age} årig {self.passenger_gender[i]}.")
                passenger_index += 1
            break    


    def poke(self): # Petar på en passagerare, anropar klass Passenger.
        try:
            random_index: int = random.randint(0, len(self.passengers) - 1) # Genererar ett slumpat index mellan 0 och nuvarande längd på lista (-1 då index börjar från 0).
            age_gender: tuple = (self.passengers[random_index], self.passenger_gender[random_index])
            reaction = Passenger(*age_gender) # Tilldelning av klassattribut till objekt. Packar upp argument ålder och kön i klass Passenger.
            return reaction.get_reaction()
        except ValueError:
            print("Inga passagerare finns på bussen.")

#|__________DEV_TOOLS________|#

    # Testmetod för att fylla passagerarlistor med ålder och kön.
    def _random_passengers(self):
        for _ in range(self.max_passengers): # Generar nummer till ålderslista. Maxlängd bestäms i max_passengers-variabeln.
            age = random.randint(0, 110)
            self.passengers.append(age)
        
        genders = ['man', 'kvinna']

        for _ in range(len(self.passengers)): # Avgränsar och definierar längden på gender-lista till längden på passagerarlistan.
            rand_gender = random.choice(genders)
            self.passenger_gender.append(rand_gender)
        