
import string

letters = string.ascii_letters
cipher = "19 17 17 19 14 20 23 18 19 8 12 16 19 8 3 21 8 25 18 14 18 6 3 18 8 15 18 22 18 11"
key = 'pearl'
letter_dict = {}
letters=letters[:26]
t=1
for l in letters:
    letter_dict[t] = letters[t-1]
    t+=1
    if t > 26:
        break
print(letter_dict)
invert_letter_dict = {v: k for k, v in letter_dict.items()}
print(invert_letter_dict)
cipher_dict = {}

for ch in cipher.split(' '):
    cipher_dict[int(ch)] = letter_dict[int(ch)]

print(cipher_dict)
j=1
str=""
broken=""
broken_chr=""
for ch in cipher.split(' '):
    str+=letter_dict[int(ch)]
    broken+=" {}".format(int(ch)-1 - invert_letter_dict[key[j-1]])
    broken_chr+=" {}".format(letters[int(ch)-1 - invert_letter_dict[key[j-1]]])
    if j == 5:
        str+='\n'
        j=0

    j+=1
print(str)
print(broken)
print(broken_chr)
