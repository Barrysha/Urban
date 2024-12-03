first_strings = ["Elon", "Musk", "Programmer", "Monitors", "Variable"]
second_strings = ["Task", "Git", "Comprehension", "Java", "Computer", "Assembler"]

firs_result = [len(i) for i in first_strings if len(i) > 5] # 1 Пункт
second_result = [x + y for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {x: len(x) for x in [*first_strings, *second_strings]}
third_result = [i for i in third_result.items()]

print(firs_result, '\n')
print(second_result, '\n')
print(*third_result, sep='\n')
