import sys
str = " ".join(sys.argv[1:])
words = str.split()
words.sort()
print("The sorted words are:")
for word in words:
   print(word)
