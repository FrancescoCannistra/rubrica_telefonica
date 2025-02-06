rubrica = []

def mostra_menu():
    print("Menu Rubrica Telefonica:")
    print("1. Aggiungi contatto")
    print("2. Visualizza tutti i contatti")
    print("3. Esci")

def aggiungi_contatto():
    nome = input("Inserisci il nome del contatto: ")
    numero = input("Inserisci il numero di telefono: ")
    rubrica.append((nome, numero))
    print(f"Contatto {nome} aggiunto con successo!")

def visualizza_contatti():
    if not rubrica:
        print("La rubrica è vuota.")
    else:
        print("Contatti salvati:")
        for contatto in rubrica:
            print(f"{contatto[0]}: {contatto[1]}")

def main():
    while True:
        mostra_menu()
        scelta = input("Scegli un'opzione (1-3): ")
        
        if scelta == "1":
            aggiungi_contatto()
        elif scelta == "2":
            visualizza_contatti()
        elif scelta == "3":
            print("Arrivederci!")
           
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
