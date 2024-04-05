# 👉 Python String Function
# 🎏 Function:- lower(), upper(),title(),capitalize(),find(),index(),isalpha(),isdigit(),isalnum(),chr(),ord(),format()

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# w="Welcome to SuberIQ"
# n=w.lower(); #🎉 Output:- welcome to suberiq
# print(n)

# u=w.upper(); #🎉 Output:- WELCOME TO SUBERIQ
# print(u)

# t=w.title(); # 🎉 Output:- Welcome To Suberiq
# print(t)

# c=w.capitalize(); # 🎉 Output:- Welcome to suberiq
# print(c)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# ❓ find() :- find character of index and if not matching character give -1.

# w="Welcome"
# print(w.find('e')) # 🎉 output:- index: 1
# print(w.find('el')) # 🎉 output:- index: 1
# print(w.find('e',2)) # 🎉 output:- index: 6
# print(w.find('z')) # 🎉 output:- index: -1 (not found)

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# ❓ index() :- find character with index and if not matching character give error.


# w="Welcome"
# print(w.index('e')) # 🎉 output:- index: 1
# print(w.index('c')) # 🎉 output:- index: 3
# print(w.index('o',2)) # 🎉 output:- index: 4
# print(w.index('z')) # 🎉 output:- index: ValueError substring not found 


# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# ❓ isalpha() : only characters

# w="Welcome"
# print(w.isalpha()) # 🎉 output:- True
# w="Wel come"
# print(w.isalpha()) # 🎉 output:- False
# w="Welcome123"
# print(w.isalpha()) # 🎉 output:- False

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# ❓ isdigit() : only number

# w="Welcome"
# print(w.isdigit()) # 🎉 output:- False
# w="Welcome123"
# print(w.isdigit()) # 🎉 output:- False
# w="1341424"
# print(w.isdigit()) # 🎉 output:- True
# w="1341 424"
# print(w.isdigit()) # 🎉 output:- False

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# ❓ isalnum() :- only apicable for number and character

# w="Welcome"
# print(w.isalnum()) # 🎉 output:- True
# w="Welcome123"
# print(w.isalnum()) # 🎉 output:- True
# w="1343"
# print(w.isalnum()) # 🎉 output:- True
# w="Welcome 1234"
# print(w.isalnum()) # 🎉 output:- False
# w="Welcome@1234"
# print(w.isalnum()) # 🎉 output:- False

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# ❓ chr() :- This takes in an interger i and converts it to a character c, so it returns a character string.
           #💧Convert integer 65 to ASCII Character ('A')

# print(chr(65))
# print(chr(97))
# print(97-65)
# print(chr(65+32))

# a = 65;
# print(chr(a)) #🎉 Output:- A
# y = chr(97);
# print(type(y),y) #🎉 Output:- (<class 'str'>) a


# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# ❓ ord() :- This takes a single Unicode character (string of length 1) and returns an integer,so the format is:
           #💧Convert ASCII Unicode Character 'A' to 65
             

# y = ord('A')
# print(type(y),y) #🎉 Output:- <class 'int'> 65

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# ❓ format() :- The format() method formats the specified value(s) and insert them inside the string's placeholder. The Placeholder is defined using curly brackets:{}. Read more about the placeholders in the Placeholder section below.

# 👉 named indexes:

# txt1 = "Welcome to {fname} {lname}".format(fname="Sumit", lname="Kumar")

# print(txt1)
# # 👉 numbered indexes:

# txt2 = "Welcome to {0} {1}".format("Plaza", "World")

# print(txt2)

# txt = "Welcome to {1} {0}".format("IQ","Suber")
# print(txt)

# # 👉 empty indexes:

# txt3 = "Welcome to {} {}".format("New", "Home")

# print(txt3)


# 🎉 output:- Welcome to Sumit Kumar (txt1)
            # Welcome to Plaza World (txt2)
             # Welcome to New Home  (txt3)


# w = "Welcome {b:10} to {a} SuberIQ".format(a=30,b=40)
# w = "Welcome {b:^10} to {a} SuberIQ".format(a=30,b=40)
# w = "Welcome {b:<10} to {a} SuberIQ".format(a=30,b=40)
# w = "Welcome {b:>10} to {a:^10} SuberIQ".format(a=30,b=40)

# print(w)

