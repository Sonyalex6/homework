import re
class WordsFinder():
    def __init__(self, *text_files):
        list_files_txt = []
        extension = ".txt"
        for txt_file in text_files:
            if txt_file.endswith(extension):
                list_files_txt.append(txt_file)
            else:
                print("Файл {} не имеет правильного формата".format(txt_file))
        if len(list_files_txt) > 0:
            self.file_names = list_files_txt
        else:
            print('Во веденном списке отсутствуют файлы типа txt')
    def get_all_words(self):
        all_words = {}
        delimiters = r"[',', '.', '=', '!', '?', ';', ':', ' - ', '\n']"
        for file_ in self.file_names:
            with open(file_, mode='r', encoding='utf-8') as file:
                string_whole_file = file.read().lower()
                list_from_file = re.split(delimiters, string_whole_file)
                all_words[file_] = list_from_file
        return all_words
    def find(self, word):
        dict_word_in_files = {}
        word_lower = word.lower()
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if words[i] == word_lower:
                    dict_word_in_files[name] = i + 1
                    break
        if len(dict_word_in_files) == 0:
            print('Искомое слово отсутствует в текстовых файлах')
            return
        else:
            return dict_word_in_files
    def count(self, word):
        word_lower = word.lower()
        dict_count_word_in_files = {}
        for name, words in self.get_all_words().items():
            count = 0
            for i in range(len(words)):
                if words[i] == word_lower:
                    count += 1
            if count > 0:
                dict_count_word_in_files[name] = count
        if len(dict_count_word_in_files) == 0:
            print('Искомое слово отсутствует в текстовых файлах')
            return
        else:
            return dict_count_word_in_files
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
