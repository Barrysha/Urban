class WordFinder:

    def __init__(self, *files):
        self.file_name = files

    def get_all_words(self):
        all_words = {}
        stop_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_name:
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.read().lower()
                for i in stop_list: # Целый час маялся, чтобы не прописывать replace для каждого символа. Как в анекдоте про оптимизацию.
                    lines = lines.replace(i, '')
                words = lines.split()
                all_words[file] = words
        return all_words

    def find(self, word):
        found_dict = {}
        for file, words in self.get_all_words().items():
            try:
                pos = words.index(word.lower()) + 1
                found_dict[file] = pos
            except ValueError:
                pass
        return found_dict

    def count(self, word):
        count_dict = {}
        for file, words in self.get_all_words().items():
            count_dict[file] = words.count(word.lower())
        return count_dict

finder1 = WordFinder('test_file.txt', 'test_file1.txt')
print(finder1.get_all_words())
print(finder1.find('бРуСника'))
print(finder1.count("ОсЕНь"), '\n')

print(finder1.find('ЖдаТь'))
print(finder1.count('ждАть'))
