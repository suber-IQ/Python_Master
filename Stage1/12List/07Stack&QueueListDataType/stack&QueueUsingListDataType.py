# 👉  Implement a Stack and Queue Using a List Data Type

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Stack in Python :- linear data structure. And Store items in (LIFO) manner.

# l = []

# while True:
#       c = int(input('''
#             1. Push Elements
#             2. Pop Elements
#             3. Peek Elements
#             4. Display Elements
#             5. Exit
#            '''))
#       if c == 1:
#           n = input("Enter The Value:-")
#           l.append(n)
#           print(l)
#       elif c == 2:
#           if len(l) == 0:
#                print("Empty Stack")
#           else:
#                p = l.pop()
#                print(p)
#                print(l)
#       elif c == 3:
#           if len(l) == 0:
#                print("Empty Stack")
#           else:
#               print("Last Stack Value:",l[-1])
#       elif c == 4:
#               print("Display Stack:",l)     
#       elif c == 5:
#               break;
#       else:
#            print("Invalid Oper...")


# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Queue in Python :- linear data structure And (FIFO) manner


l = []

while True:
      c = int(input('''
            1. Push Elements
            2. Pop First Elements
            3. Front Elements
            4. Last Elements
            5. Display Queue
            6. Exit
           '''))
      if c == 1:
          n = input("Enter The Value:-")
          l.append(n)
          print(l)
      elif c == 2:
          if len(l) == 0:
               print("Empty Queue")
          else:
               del l[0]
               print(l)
      elif c == 3:
          if len(l) == 0:
               print("Empty Queue")
          else:
              print("First Queue Value:",l[0])
      elif c == 4:
          if len(l) == 0:
               print("Empty Queue")
          else:
              print("Last Queue Value:",l[-1])  
      elif c == 5:
              print("Display Queue",l)
      elif c == 6:
              break;
      else:
           print("Invalid Oper...")






