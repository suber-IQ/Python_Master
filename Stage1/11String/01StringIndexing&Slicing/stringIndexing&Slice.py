# 👉 String Indexing & Slicing
#  🎏 Point:- 💧 A String is a Sequence of Characters.
            # 💧 Strings can be created by enclosing characters inside a single quote or double-quotes
           #💧 Triple quotes can be used represent multiline strings.
           #💧left to right indexing is start with 0.
           #💧right to left indexing is start with -1.

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# w = "Welcome to SuberIQ"
# print(w[6])
# print(w[-1])
# print(w[-12])

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

w = "Welcome to SuberIQ"

print(w[0:7]) # slice 0 to 6 char (Welcome)
print(w[0::2]) # 2 with increment (Wloet ueI)
print(w[-1:-10:-2]) # reverse order (QrbSo)