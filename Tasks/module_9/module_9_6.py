def all_var(text):

    strings = ''
    for i in text:
        strings += i
        yield strings

a = all_var("ABC")
for i in a:
    print(i)
