def custom_write(file_name, strings):
    # Словарь для хранения позиций и текста строк
    strings_positions = {}

    # Открываем файл для записи с кодировкой utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        # Проходимся по строкам и записываем их в файл
        for line_num, line in enumerate(strings, start=1):
            # Определяем начальную позицию в байтах перед записью строки
            byte_position = file.tell()
            # Записываем строку в файл и добавляем переход на новую строку
            file.write(line + '\n')
            # Добавляем данные в словарь с номером строки и позицией байта
            strings_positions[(line_num, byte_position)] = line

    # Возвращаем словарь с позициями строк
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
