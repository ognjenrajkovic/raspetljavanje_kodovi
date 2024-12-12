n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("Broj je deljiv i sa 3 i sa 5.")
elif n % 3 == 0 and n % 5 != 0:
    print("Broj je deljiv sa 3, ali nije deljiv sa 5.")
elif n % 3 != 0 and n % 5 == 0:
    print("Broj je deljiv sa 5, ali nije deljiv sa 3.")
