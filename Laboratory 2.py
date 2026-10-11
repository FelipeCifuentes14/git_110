import csv
import random
import xml.etree.ElementTree as ET

def process_csv(filename="books.csv"):
    books = []
    
    # Чтение файла. Часто используется кодировка windows-1251 для русских CSV.
    try:
        with open(filename, "r", encoding="windows-1251") as file:
            reader = csv.reader(file, delimiter=";")
            headers = next(reader)
            for row in reader:
                if len(row) > 3:
                    books.append(row)
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        return

    # ВАЖНО: Проверьте индексы столбцов в вашем файле и измените их, если нужно
    # Стандартная структура часто бывает: 0-ID, 1-Название, 2-Автор, 3-Год, 4-Издательство, 5-Популярность
    IDX_TITLE = 1
    IDX_AUTHOR = 2
    IDX_YEAR = 3
    IDX_PUBLISHER = 4
    IDX_POPULARITY = 5 # Или другой столбец, содержащий числа просмотров/скачиваний

    # 1. Вывести количество записей, у которых в поле Название строка длиннее 30 символов
    long_titles = sum(1 for book in books if len(book[IDX_TITLE]) > 30)
    print(f"1. Количество книг с названием длиннее 30 символов: {long_titles}")

    # 2. Поиск книги по автору с ограничением (Вариант 3: Только 2014, 2016 и 2017 года)
    search_author = input("2. Введите имя автора для поиска: ").strip().lower()
    allowed_years = {"2014", "2016", "2017"}
    
    search_results = [
        book for book in books 
        if search_author in book[IDX_AUTHOR].lower() and str(book[IDX_YEAR]) in allowed_years
    ]
    
    print(f"   Найдено книг автора в {allowed_years}: {len(search_results)}")
    for b in search_results:
        print(f"   - {b[IDX_TITLE]} ({b[IDX_YEAR]})")

    # 3. Генератор библиографических ссылок для 20 записей
    if len(books) >= 20:
        random_books = random.sample(books, 20)
        with open("references.txt", "w", encoding="utf-8") as f_out:
            for i, book in enumerate(random_books, 1):
                f_out.write(f"{i}. {book[IDX_AUTHOR]}. {book[IDX_TITLE]} - {book[IDX_YEAR]}\n")
        print("3. Сгенерирован файл 'references.txt' с 20 ссылками.")
    else:
        print("3. Недостаточно книг для генерации 20 ссылок.")

    # --- ДОПЗАДАНИЕ ---
    print("\n--- Дополнительное задание ---")
    
    # Вывести перечень всех издательств без повторений
    publishers = set()
    for book in books:
        if len(book) > IDX_PUBLISHER:
            publishers.add(book[IDX_PUBLISHER].strip())
    print(f"Количество уникальных издательств: {len(publishers)}")
    # print(publishers) # Раскомментируйте, чтобы вывести сам список

    # Самые популярные 20 книг
    try:
        sorted_books = sorted(books, key=lambda x: int(x[IDX_POPULARITY]) if x[IDX_POPULARITY].isdigit() else 0, reverse=True)
        print("Топ 20 самых популярных книг:")
        for i in range(min(20, len(sorted_books))):
            print(f"  {i+1}. {sorted_books[i][IDX_TITLE]} (Популярность: {sorted_books[i][IDX_POPULARITY]})")
    except IndexError:
        print("Не удалось определить популярность. Проверьте индекс IDX_POPULARITY.")

def process_xml(filename="currency.xml"):
    print("\n--- Обработка XML ---")
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Вариант 3: Список Name, но только для валют с Nominal=1
        print("Список валют (Nominal = 1):")
        found = False
        
        for valute in root.findall('Valute'):
            nominal = valute.find('Nominal')
            name = valute.find('Name')
            
            if nominal is not None and name is not None:
                if nominal.text.strip() == "1":
                    print(f"- {name.text}")
                    found = True
                    
        if not found:
            print("Валют с номиналом 1 не найдено.")
            
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
    except ET.ParseError:
        print(f"Ошибка: Файл {filename} имеет неверный формат XML.")

if __name__ == "__main__":
    process_csv("books.csv")
    process_xml("currency.xml")