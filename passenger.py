import os

class Passenger:

    def __init__(self, age: int, gender: str):
        self.age = age # klassattribut för passagerares ålder
        self.gender = gender # klassattribut för passagerares kön

#|__________METODER__________|#

    def get_reaction(self): # Metoden kontrollerar objektets(passagerarens) ålder och skriver ut en händelse till skärmen.
        os.system('clear')
        if self.age >= 0 and self.age <= 6:
            if self.gender == 'man':
                print('Den lilla pojken snärtar en snorkråka i ansiktet på dig.')
            elif self.gender == 'kvinna':
                print('Den lilla flickan stirrar nedlåtande djupt i din själ.')
        elif self.age > 6 and self.age < 20:
            if self.gender == 'man':
                print('Du trodde att din petning lyckades överraska, men när pojken försvunnit ur din syn igen upptäcker du att din plånbok är borta.')
            elif self.gender == 'woman':
                print('Flickan tittar bestört på ditt närmande finger och fäller långsamt ut fällkniven hon hade i sin väska...\n\n'
                      'Du väljer att avbryta petningen.')
        elif self.age >= 20 and self.age < 70:
            if self.gender == 'man':
                print('Du får en örfil som sänker dig i medvetslöshet...\n\n')
                input('Vakna...')
                os.system('clear')
                input('Vakna sa jag...')
                os.system('clear')
                input('Ett försök till...')
                os.system('clear')
            elif self.gender == 'kvinna':
                print('Med en kvick handrörelse har den rasande kvinnan ringt polisen, brandkåren och den lokala kommunfullmäktige för att anmäla ditt beteende.')
        elif self.age >= 70:
            print(f"En gammal {self.gender} faller plötsligt livlös till marken. Ingen såg det, va?")

    # Skriver ut klassattributen om print(Passenger) eller object.str() anropas.
    def __str__(self):
        return f"Passagerare(ålder:{self.age}, kön:{self.gender})"