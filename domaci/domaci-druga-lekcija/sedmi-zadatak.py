godina = int(input())

if (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0:
    print("Godina", godina,"je prestupna.")
else:
    print("Godina", godina,"nije prestupna.")