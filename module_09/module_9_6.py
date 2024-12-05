def all_var(text):
    
    for i in range(len(text)):
        len_substring = i + 1  # длина подпоследовательности
        pointer = 0
        while len(text) - pointer > 0:
            if len(text[pointer: pointer + len_substring]) == len_substring:
                yield text[pointer: pointer + len_substring]
            else:
                break
            pointer += 1



if __name__ == "__main__":
    a = all_var("abc")
    for i in a:
        print(i)
