import pickle
import json

# Исходный словарь стран и столиц
countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим"
}

def save_to_pickle(data, filename="data.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
    print(f"Данные сохранены в {filename}")

def load_from_pickle(filename="data.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("Файл не найден, загружены пустые данные.")
        return {}

def save_to_json(data, filename="data.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Данные сохранены в {filename}")

def load_from_json(filename="data.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не найден, загружены пустые данные.")
        return {}

def add_country(countries, country, capital):
    countries[country] = capital
    print(f"Добавлена страна: {country} со столицей {capital}")

def remove_country(countries, country):
    if country in countries:
        del countries[country]
        print(f"Страна {country} удалена")
    else:
        print(f"Страна {country} не найдена")

def find_capital(countries, country):
    return countries.get(country, "Страна не найдена")

def edit_capital(countries, country, new_capital):
    if country in countries:
        countries[country] = new_capital
        print(f"Столица страны {country} изменена на {new_capital}")
    else:
        print(f"Страна {country} не найдена")

if __name__ == "__main__":
    print("Исходные данные:", countries)

    # Добавление данных
    add_country(countries, "Испания", "Мадрид")

    # Удаление данных
    remove_country(countries, "Германия")

    # Поиск данных
    print("Столица Франции:", find_capital(countries, "Франция"))

    # Редактирование данных
    edit_capital(countries, "Россия", "Санкт-Петербург")

    # Сохранение и загрузка в pickle
    save_to_pickle(countries)
    loaded_data_pickle = load_from_pickle()
    print("Данные после загрузки из pickle:", loaded_data_pickle)

    # Сохранение и загрузка в JSON
    save_to_json(countries)
    loaded_data_json = load_from_json()
    print("Данные после загрузки из JSON:", loaded_data_json)
