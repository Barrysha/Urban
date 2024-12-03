def custom_write(file_name, strings):
    str_pos = {}
    with open(file_name, 'w', encoding='utf-8') as file_name:
        for idx, string in enumerate(strings, start=1):
            file_name.write(string + '\n')
            current_pos = file_name.tell()
            str_pos[(idx, current_pos)] = string
    return str_pos

info = [
    "Text for tell.",
    "Используйте кодировку utf-8.",
    "Because there are 2 languages!",
    "Спасибо!"
    ]

result = custom_write('file_name', info)
for key, value in result.items():
    print(key, value)
