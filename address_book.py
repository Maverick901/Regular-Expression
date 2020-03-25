import re

names_book = open('names.txt', encoding='utf-8')
data = names_book.read()
names_book.close()


# print(re.match(r'Love', data))
# print(re.search(r'Tim', data))

# print(re.search(r'\(\d{3}\) \d{3}-\d{4}', data))
# print(re.findall(r'\w*, \w+', data))
# print(re.findall(r'[-\w\d.]+@[-\w.]+', data))
# print(re.findall(r'[trehous]{9}', data, re.I))
# print(re.findall(r'''
#   \b@[-.\w\d]*
#    [^gov\t]
#    \b
# ''', data, re.VERBOSE | re.I))
# print(re.findall(r'''
#    \b[\w]*,
#    \s
#    [\w]+
#    [^\t\n]
# ''', data, re.X))

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w]+))\t
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})\t?
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?
    (?P<twitterHandle>@[\w\d]+)?$
''', re.X | re.M)
print(line.search(data).groupdict())

for match in line.finditer(data):
    print('{first} {last} {email}'.format(**match.groupdict()))
