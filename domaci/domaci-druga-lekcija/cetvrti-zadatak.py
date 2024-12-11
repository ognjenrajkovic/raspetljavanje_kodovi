broj_karata = input("Unesite broj karata:")
student = input("Unesi te da li ste student (DA/NA):").lower()
vip_paket = input("Da li je VIP paket?(DA/NE):").lower()

karta = 1500

if broj_karata.isdigit():
    broj_karata = int(broj_karata)
    if student == "da" or student == "ne":
        if vip_paket  == "da" or vip_paket == "ne":
            if vip_paket == "da":
                karta = karta + 500
            if student == "da":
                karta = karta - karta * 0.10
            if broj_karata > 4:
                karata = karta - karta * 0.05
            ukupna_cena = int(karta * broj_karata)
            print("Cena karata je:", ukupna_cena)
        else:
            print("Odgovor na pitanje da li je VIP paket mora da bude DA ili NE.")
    else:
        print("Odgovor na pitanje da li je student mora da bude DA ili NE.")
else:
    print("Broj karata mora da bude ceo broj.")