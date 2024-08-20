from pojistenec import Pojistenec


# Vytvoření prázdného seznamu pojištěnců

class SpravaPojistenych:
    def __init__(self):
        self.pojistenci = []

# metoda pro přidání pojištěnce
    def pridat_pojistence(self, jmeno, prijmeni, vek, telefon):
        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.pojistenci.append(novy_pojistenec)
        print(f"Pojištěnec {jmeno} {prijmeni}, {vek} let, tel: {telefon} byl úspěšně přidán.")

# metoda pro zobrazení seznamu
    def zobrazit_pojistence(self):
        if not self.pojistenci:
            print("Seznam pojištěnců je prázdný.")
        else:
            print("Seznam všech pojištěnců:")
            for pojistenec in self.pojistenci:
                print(pojistenec)

# metoda pro vyhledání pojištěnce podle jména a příjmení
    def vyhledat_pojistence(self, jmeno, prijmeni):
        nalezeno = False
        for pojistenec in self.pojistenci:
            if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
                print("Nalezený pojištěnec:")
                print(pojistenec)
                nalezeno = True
                break
        if not nalezeno:
            print(f"Pojistenec {jmeno} {prijmeni} nebyl nalezen.")