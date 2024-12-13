S = int(input())
d = int(input())

d2 = d**2
broj_plocica = S / d2

if S % d2 == 0:
    print("Da, potrebno je", broj_plocica,"pločica.")
else:
    print("Ne, potrebno je", broj_plocica,"pločica.")