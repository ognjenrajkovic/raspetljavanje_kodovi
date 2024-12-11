broj_ucenika = int(input())
broj_autobusa = broj_ucenika // 50
broj_preostalih_ucenika = broj_ucenika % 50

if broj_preostalih_ucenika > 0:
    broj_autobusa += 1

print("Potrebno je", broj_autobusa,"autobusa, a u poslednjem autobusu ima", broj_preostalih_ucenika)