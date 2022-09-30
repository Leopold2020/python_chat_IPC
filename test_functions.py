# Oskar Svelund
# TEINF-20
# 2022-09-30
# a playground fot trying out functions


def toBinary(word):
  letters,binery=[],[]
  for i in word:
    letters.append(ord(i))
  for i in letters:
    binery.append(int(bin(i)[2:]))
  return binery

test1 = toBinary(input(""))

for r in test1:
    print(r, end=" ")