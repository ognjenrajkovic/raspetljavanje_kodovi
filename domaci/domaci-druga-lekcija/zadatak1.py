vrsta = input("Unesite tip pretplate (Basic/Premium):").lower
broj_meseci = input("Unesite broj meseci članarine:")
cena_clanarine = input("Unesite cenu članarine:")

clanarina = 0

if vrsta != "premium" or vrsta != "basic":
    print("Molim Vas unesite ponuđene tipove članarine u suprotnom program neće biti izvršen.")


else:
    if broj_meseci.isdigit:
        broj_meseci = int(broj_meseci)

        if cena_clanarine.isdigit:
            cena_clanarine = int(cena_clanarine)

            if vrsta == "premium":
                cena_clanarine *= 2
            if broj_meseci >= 6 and broj_meseci < 12:
                cena_clanarine = cena_clanarine - (cena_clanarine * 0.10)
            elif broj_meseci >= 12:
                cena_clanarine = cena_clanarine - (cena_clanarine * 0.20)

            clanarina = int(cena_clanarine * broj_meseci)
            print(clanarina)

        else:
            print("Možete uneti samo brojeve u odeljku za broj meseci i cenu članarine u suprotnom program neće biti izvršen.")
    else:
        print("Možete uneti samo brojeve u odeljku za broj meseci i cenu članarine u suprotnom program neće biti izvršen.")