n = int(input())

# deljivost15 = False
# deljivost5 = False
# deljivost3 = False
if n % 3 == 0:
    #deljivost3 = True
    print("- Deljiv je sa 3")
if n % 5 == 0:
    #deljivost5 = True
    print("- Deljiv je sa 5")
if n % 15 == 0:
    #deljivost15 = True
    print("- Deljiv je sa 15")
if n % 3 != 0 and n % 5 != 0 and n % 15 != 0:
    print("- Nije deljiv ni sa 3, ni sa 5")

# if deljivost3 and deljivost5 and deljivost15:
#     print("- Deljiv je sa 3 - Deljiv je sa 5 - Deljiv je sa 15 ")