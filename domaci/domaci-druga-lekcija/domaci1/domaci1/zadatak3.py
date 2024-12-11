plata_sat = 200

broj_radnih_sati = int(input())

if broj_radnih_sati > 40:
    broj_radnih_sati = 40

plata = broj_radnih_sati * plata_sat

print("Plata ranika je:", plata)