import random
import string


def load_cities(filename: str) -> set:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            cities = {city.strip().lower() for city in f}
        return cities
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return set()
    except Exception as e:
        print(f'Ошибка при чтении файла \'{filename}\': {e}')
        return set()


def find_bad_letters(cities_set: set) -> set:
    first_letters = {city[0] for city in cities_set}
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return alphabet - first_letters


def human_turn(previous_city: str, cities_set: set) -> str | None:
    if previous_city:
        last_letter = previous_city[-1].lower()
        print(f"\nВаш ход. Назовите город на букву '{last_letter.upper()}':")
    else:
        print("\nВаш первый ход. Назовите любой город:")

    city = input("> ").strip().lower()

    if not city:
        print("Нельзя вводить пустую строку.")
        return None

    if city not in cities_set:
        print("Такого города нет в списке или он уже был назван.")
        return None

    if previous_city:
        if city[0] != previous_city[-1].lower():
            print(f"Город должен начинаться на букву '{previous_city[-1].upper()}'.")
            return None

    cities_set.remove(city)
    return city


def computer_turn(previous_city: str, cities_set: set, bad_letters: set) -> (str | None):
    if not previous_city:
        print("Компьютер не может ходить первым. Ход переходит к человеку.")
        return None

    last_letter = previous_city[-1].lower()
    possible_cities = [
        city for city in cities_set
        if city[0] == last_letter and city[-1] not in bad_letters
    ]

    if not possible_cities:
        print("Компьютер не может найти подходящий город.")
        return None

    city = random.choice(possible_cities)
    cities_set.remove(city)
    print(f"Компьютер назвал город: {city.capitalize()}")
    return city


def main():
    filename = "cities.txt"
    cities = load_cities(filename)
    if not cities:
        print("Игра завершена из-за ошибки при загрузке городов.")
        return

    bad_letters = find_bad_letters(cities)
    previous_city = ""

    while True:
        city = human_turn(previous_city, cities)
        if city is None:
            print("Компьютер победил.")
            break

        previous_city = city

        city = computer_turn(previous_city, cities, bad_letters)
        if city is None:
            print("Компьютер проиграл.")
            break

        previous_city = city


main()
