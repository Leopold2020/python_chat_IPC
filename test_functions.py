# Oskar Svelund
# TEINF-20
# 2022-09-30
# a playground fot trying out functions

name = input("Write your username\n>> ")

print(name.lower())





if name.lower() == "tech priest":
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


if name.lower() == "catboy" or name.lower() == "catboy":
  test_cat = input("catchat\n>> ")
  test_cat += " ~ nyan"
  print(test_cat)


if name.lower() == "pepe":
  message = input("write a message\n>> ")
  i = 0
  for x in message:
      if i%2==0:
          print(x.lower(), end = "")
      else:
          print(x.upper(), end = "")
      i += 1


if name.lower() == "märta" or name.lower() == "pär":
  message = input("please write a message\n>> ")
  message = len(message.split(" "))
  final_message = "bullshit " * message
  print(final_message)

if name.lower == "niclas":
  pass

if name.lower == "":
  pass