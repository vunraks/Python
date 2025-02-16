#1
# def filter_long_words(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
#         for line in infile:
#             words = line.split()
#             long_words = [word for word in words if len(word) >= 7]
#             outfile.write(" ".join(long_words) + "\n")


# filter_long_words("newtest.txt", "test.txt")


#2
# with open("newtest.txt", "r", encoding="utf-8") as infile, open("test.txt", "w", encoding="utf-8") as outfile:
#     for line in infile:
#         outfile.write(line)


#3
# with open("test.txt", "r", encoding="utf-8") as infile:
#     lines = infile.readlines()

# with open("newtest.txt", "w", encoding="utf-8") as outfile:
#     outfile.writelines(reversed(lines))


#4
# with open("test.txt", "r", encoding="utf-8") as infile:
#     lines = infile.readlines()

# last_no_comma = -1
# for i, line in enumerate(lines):
#     if "," not in line:
#         last_no_comma = i

# if last_no_comma != -1:
#     lines.insert(last_no_comma + 1, "************\n")
# else:
#     lines.append("************\n")

# with open("newtest.txt", "w", encoding="utf-8") as outfile:
#     outfile.writelines(lines)


#5
# symbol = input("Введите символ: ").strip()

# with open("test.txt", "r", encoding="utf-8") as infile:
#     text = infile.read()

# words = text.split()
# count = sum(1 for word in words if word.startswith(symbol))

# print(f"Количество слов, начинающихся с '{symbol}': {count}")


#6
# with open("test.txt", "r", encoding="utf-8") as infile:
#     text = infile.read()

# text = text.replace("*", "#").replace("&", "*").replace("#", "&")

# with open("newtest.txt", "w", encoding="utf-8") as outfile:
#     outfile.write(text)


#7
# lines = ["Первая строка", "Вторая строка", "Третья строка"]

# with open("test.txt", "w", encoding="utf-8") as outfile:
#     outfile.writelines(line + "\n" for line in lines)


#9
# with open("test.txt", "r", encoding="utf-8") as infile:
#     text = infile.read()

# print(f"Количество символов в файле: {len(text)}")


#10
# with open("test.txt", "r", encoding="utf-8") as infile:
#     line_count = sum(1 for _ in infile)

# print(f"Количество строк в файле: {line_count}")



















#1
# with open("test.txt", "r", encoding="utf-8") as f1, open("newtest.txt", "r", encoding="utf-8") as f2:
#     lines1 = f1.readlines()
#     lines2 = f2.readlines()

# for i, (line1, line2) in enumerate(zip(lines1, lines2)):
#     if line1 != line2:
#         print(f"Строка {i + 1} не совпадает:")
#         print(f"test.txt: {line1.strip()}")
#         print(f"newtest.txt: {line2.strip()}")

# if len(lines1) > len(lines2):
#     print("Дополнительные строки в test.txt:")
#     print("".join(lines1[len(lines2):]))
# elif len(lines2) > len(lines1):
#     print("Дополнительные строки в newtest.txt:")
#     print("".join(lines2[len(lines1):]))


#2
# vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
# consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
# digits = "0123456789"

# with open("test.txt", "r", encoding="utf-8") as infile:
#     text = infile.read()

# num_chars = len(text)
# num_lines = text.count("\n") + 1
# num_vowels = sum(1 for char in text if char in vowels)
# num_consonants = sum(1 for char in text if char in consonants)
# num_digits = sum(1 for char in text if char in digits)

# stats = (
#     f"Количество символов: {num_chars}\n"
#     f"Количество строк: {num_lines}\n"
#     f"Количество гласных букв: {num_vowels}\n"
#     f"Количество согласных букв: {num_consonants}\n"
#     f"Количество цифр: {num_digits}\n"
# )

# with open("newtest.txt", "w", encoding="utf-8") as outfile:
#     outfile.write(stats)




#3
# with open("test.txt", "r", encoding="utf-8") as infile:
#     lines = infile.readlines()

# if lines:
#     lines.pop()  # Удаляем последнюю строку

# with open("newtest.txt", "w", encoding="utf-8") as outfile:
#     outfile.writelines(lines)



#4
# with open("test.txt", "r", encoding="utf-8") as infile:
#     max_length = max(len(line.rstrip()) for line in infile)

# print(f"Длина самой длинной строки: {max_length}")


#5
# word = input("Введите слово для поиска: ").strip().lower()

# with open("test.txt", "r", encoding="utf-8") as infile:
#     text = infile.read().lower()

# count = text.split().count(word)
# print(f"Слово '{word}' встречается {count} раз(а).")


#6
# search_word = input("Введите слово для поиска: ").strip()
# replace_word = input("Введите слово для замены: ").strip()

# with open("test.txt", "r", encoding="utf-8") as infile:
#     text = infile.read()

# new_text = text.replace(search_word, replace_word)

# with open("newtest.txt", "w", encoding="utf-8") as outfile:
#     outfile.write(new_text)

# print("Замена выполнена!")
