import re

names_book = open('names.txt', encoding='utf-8')
data = names_book.read()
names_book.close()


print(re.match(r'Love', data))
print(re.search(r'Tim', data))
