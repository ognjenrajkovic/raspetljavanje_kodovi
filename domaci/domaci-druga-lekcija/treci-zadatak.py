kasnjenje = input("Unesite broj dana kašenja u vraćanju knjige:")
broj_dosadasnjih_kasnjena = input("Unesite broj prethodnih kašnjenja:")
clan_biblioteke = input("Unesite da li je član biblioteke (DA/NE):").lower()

kazna = 0

if kasnjenje.isdigit():
    kasnjenje = int(kasnjenje)
    if broj_dosadasnjih_kasnjena.isdigit():
        broj_dosadasnjih_kasnjena = int(broj_dosadasnjih_kasnjena)
        if clan_biblioteke == "da" or clan_biblioteke == "ne":
            if kasnjenje > 10 or broj_dosadasnjih_kasnjena > 3:
                kazna = 100 * kasnjenje
            if kasnjenje >= 1 and kasnjenje <= 10 and broj_dosadasnjih_kasnjena <= 3:
                kazna = 50 * kasnjenje
            if kasnjenje == 0:
                kazna = 0
            if clan_biblioteke == "da":
                kazna //= 2
            print("Kazna prema unetim informacijama iznosi:", kazna)
        else:
            print("Na pitanje da li je član biblioteke morate odgovoriti sa DA ILI NE.")
    else:
        print("Broj mora da bude ceo broj.")
else:
    print("Broj mora da bude ceo broj")
