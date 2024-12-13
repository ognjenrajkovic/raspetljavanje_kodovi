plata = 500
plata_prekovremeno = 250
bonus = 500

broj_radnih = int(input())
broj_prekovremenih = int(input())

mesecna_plata = plata * broj_radnih + plata_prekovremeno

if broj_prekovremenih > 10:
    mesecna_plata += bonus

print("Plata radnika je:", mesecna_plata)
