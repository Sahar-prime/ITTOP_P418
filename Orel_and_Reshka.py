import random


def brosok_monetki(brosok: int) -> list[str]:
    variants = ['орел', 'решка']
    results: list[str] = []
    for _ in range(brosok):
        result = random.choice(variants)
        results.append(result)
    return results


def main():
    try:
        brosok = int(input("Введите количество бросков: "))
    except ValueError:
        print("Некорректный ввод.")
        return
    result_broskov = brosok_monetki(brosok)
    eagle_count = result_broskov.count('орел')
    tails_count = result_broskov.count('решка')
    print("Результаты бросков:")
    for i, result in enumerate(result_broskov):
        print(f"Бросок {i+1}: {result}")
    print(f"\nОрлов: {eagle_count}")
    print(f"Решек: {tails_count}")
    if eagle_count > tails_count:
        print("\nПобедил орел!")
    elif tails_count > eagle_count:
        print("\nПобедила решка!")
    else:
        print("\nНичья!")


if __name__ == "__main__":
    main()
