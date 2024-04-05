# 👉 List comprehension Elegant way to create Lists
# ▶️ List comprehension is an elegant way to define and create lists based on existing lists.
# ▶️ List comprehension is generally more compact and faster than normal functions and loops for creating list.

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# l = []
# for a in range(1,20):
#       l.append(a)


# print(l)  # 🎉 output:- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠


# n = [m for m in range(1,20)]
# print(n)  # 🎉 output:-  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# n = [m for m in range(1,20) if m%2==0 ]
# print(n)      # 🎉 output:-  [2, 4, 6, 8, 10, 12, 14, 16, 18]


# s = "hello"
# d=[g for g in s]
# print(d) 