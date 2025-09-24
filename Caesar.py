def caesar_cipher(message: str, shift: int) -> str:
    encrypted_message = ""
    for char in message:
        if char == " ":
            encrypted_message += char
        else:
            char_code = ord(char)
            new_char_code = char_code + shift
            encrypted_message += chr(new_char_code)

    return encrypted_message


def main() -> None:
    try:
        message = input("Введите текст: ")
        shift = int(input("Введите сдвиг: "))
        result = caesar_cipher(message, shift)
        print("Результат:", result)
    except ValueError:
        print("Ошибка: сдвиг должен быть целым числом.")


if __name__ == "__main__":
    main()
