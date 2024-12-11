broj = int(input())

zadnja = broj % 10
treca = broj % 100 // 10
druga = broj % 1000 // 100
prva = broj % 10000 // 1000

print(zadnja, treca, druga, prva, sep="")