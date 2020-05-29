cipher = "19 17 17 19 14 20 23 18 19 X8 12 16 19 X8 X3 21 X8 25 18 14 18 X6 X3 18 X8 15 18 22 18 11"

i=0
while 8 < len(cipher[:len(cipher)-i]):
    print(i*" "+cipher[:-i])
    i+=3
