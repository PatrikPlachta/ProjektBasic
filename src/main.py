from spravapojistenych import SpravaPojistenych

# Přejmenování SpravaPojistenych pro lepší použití
sprava = SpravaPojistenych()

# Hlavní uživatelské rozhraní
while True:
    print("\n--- Správa pojištěných osob ---\n")
    print("1. Přidat pojištěnce")
    print("2. Zobrazit všechny pojištěnce")
    print("3. Vyhledat pojištěnce")
    print("4. Ukončit program\n")
    akce = input("Vyberte akci: ")

# přidání pojištěnce s validací prázdného jména

    if akce == "1":
        while True:
            jmeno = input("Zadejte jméno: ").strip()
            if not jmeno:
                print("Jméno nesmí být prázdné. Zkuste to znovu.")
            else:
                break

        while True:
            prijmeni = input("Zadejte příjmení: ").strip()
            if not prijmeni:
                print("Příjmení nesmí být prázdné. Zkuste to znovu.")
            else:
                break

        vek = input("Zadejte věk: ")
        telefon = input("Zadejte telefonní číslo: ")
        sprava.pridat_pojistence(jmeno, prijmeni, vek, telefon)

# Zobrazení seznamu pojištěných

    elif akce == "2":
        sprava.zobrazit_pojistence()

# Vyhledání pojištěného podle jména a příjmení

    elif akce == "3":
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        sprava.vyhledat_pojistence(jmeno, prijmeni)

# Ukončení programu

    elif akce == "4":
        print("Ukončuji program.")
        break
    else:
        print("Neplatná volba, zkuste to znovu.")