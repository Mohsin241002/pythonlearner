a = "good afternoon, "
b = input("enter your name : ")
c = a + b
print(c)


letter = '''Dear |name|
    you are selected!
    |date|'''
a = input("enter your name : ")
b = input("todays date : ")

letter = letter.replace("|name|", a)
letter = letter.replace("|date|", b)
print(letter)


string = "hello  how  are  u?"
print(string)
print(string.count("  "))
print(string.replace("  ", " "))
