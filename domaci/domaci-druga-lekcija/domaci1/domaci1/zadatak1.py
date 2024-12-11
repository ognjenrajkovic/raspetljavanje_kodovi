cena_pice = 250
cena_hrana = 500
torta = 1500

broj_gostiju = int(input()) + 1

ukupna_cena = broj_gostiju * (cena_pice + cena_hrana) + torta

print("Ukupan iznos je:", ukupna_cena)