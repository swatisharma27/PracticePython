file = input("Enter filename: ")
fhand = open(file, 'r')
fread = fhand.read()
words = fread.split()

counts = dict()
for line in fhand:
     words = line.decode().split()
     for word in words:
         counts[word] = counts.get(word, 0) + 1

print(counts)