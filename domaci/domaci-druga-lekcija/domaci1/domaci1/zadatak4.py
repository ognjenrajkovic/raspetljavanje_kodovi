broj = int(input())

zadnja = broj % 10
sredisnja = broj % 100 // 10
prva = broj % 1000 // 100

zbir = zadnja + sredisnja + prva

print(zbir)