import json
def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

import os
def delete_save(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("Файл не найден.")

import csv
def write_to_csv(users, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Имя", "Данные"])  # Записываем заголовки
        for user in users:
            writer.writerow([user["name"], user["data"]])  # Записываем данные пользователя

def start_game():
    print("Добро пожаловать в игру 'Пленник Замка Тьмы'!")
    print("Вам необходимо выбирать пути и принимать решения для освобождения из замка.")
    chapter_1()

def chapter_1():
    print("\nГлава 1: Темная Комната")
    print("Вы пытаетесь освободиться из своей камеры, но кроме вас в комнате ничего нет.")
    print("Что вы будете делать?")
    print("1. Искать выход.")
    print("2. Кричать на помощь.")
    choice = input("Выберите вариант (1 или 2): ")
    if choice == "1":
        chapter_2()
    elif choice == "2":
        chapter_2()
    else:
        print("Пожалуйста, выберите допустимый вариант.")
        chapter_1()

def chapter_2():
    print("\nГлава 2: Темные Подземелья")
    print("Вы нашли маленькую дверь в углу комнаты, которая ведет в подземелья.")
    print("1. Пройти через дверь.")
    print("2. Исследовать комнату дальше.")
    choice = input("Выберите вариант (1 или 2): ")
    if choice == "1":
        chapter_3()
    elif choice == "2":
        chapter_3()
    else:
        print("Пожалуйста, выберите допустимый вариант.")
        chapter_2()

def chapter_3():
    print("\nГлава 3: Битва с Чудовищем")
    print("Вы вошли в подземелья и встретили огромное чудовище!")
    print("1. Сражаться с чудовищем.")
    print("2. Вернуться и пройти через дверь.")
    choice = input("Выберите вариант (1 или 2): ")
    if choice == "1":
        chapter_4()
    elif choice == "2":
        chapter_4()
    else:
        print("Пожалуйста, выберите допустимый вариант.")
        chapter_3()


def chapter_4():
    print("\nГлава 4: Решение")
    print("Вы сражаетесь с чудовищем и побеждаете! Ваше смелое действие привлекло внимание стражников.")
    print("1. Спрятаться.")
    print("2. Сопротивляться.")
    choice = input("Выберите вариант (1 или 2): ")
    if choice == "1":
        chapter_5()
    elif choice == "2":
        chapter_5()
    else:
        print("Пожалуйста, выберите допустимый вариант.")
        chapter_4()
def chapter_5():
    print("\nГлава 5: Побег")
    print("Вы сумели спрятаться и ожидаете подходящего момента для побега.")
    print("1. Наблюдать за стражниками и выбирать момент побега.")
    print("2. Попытаться обмануть стражников и покинуть замок.")
    choice = input("Выберите вариант (1 или 2): ")
    if choice == "1":
        chapter_6()
    elif choice == "2":
        chapter_6()
    else:
        print("Пожалуйста, выберите допустимый вариант.")
        chapter_5()
def chapter_6():
    print("\nГлава 6: Замковый Двор")
    print("Вы выбрали момент и смогли убежать от стражников. Теперь вы находитесь в замковом дворе.")
    print("1. Искать спрятанный выход из замка.")
    print("2. Попытаться проникнуть во внутреннюю часть замка.")
    choice = input("Выберите вариант (1 или 2): ")
    if choice == "1":
        chapter_7()
    elif choice == "2":
        chapter_8()
    else:
        print("Пожалуйста, выберите допустимый вариант.")
        chapter_6()
def chapter_7():
    print("\nГлава 7: Тайные Туннели")
    print("Вы нашли секретный проход, который ведет в тайные туннели под замком.")
    print("1. Пройти по туннелям.")
    print("2. Вернуться в замковый двор.")
    choice = input("Выберите вариант (1 или 2): ")
    if choice == "1":
        chapter_9()
    elif choice == "2":
        chapter_6()
    else:
        print("Пожалуйста, выберите допустимый вариант.")
        chapter_7()

def chapter_8():
    print("\nГлава 8: Зал Магии")
    print("Вы прошли во внутреннюю часть замка и нашли себя в зале магии.")
    print("1. Исследовать зал магии.")
    print("2. Выйти из зала и искать другой выход.")
    choice = input("Выберите вариант (1 или 2): ")
    if choice == "1":
        chapter_10()
    elif choice == "2":
        chapter_6()
    else:
        print("Пожалуйста, выберите допустимый вариант.")
        chapter_8()

def chapter_9():
    print("\nГлава 9: Выход")
    print("Вы прошли по тайным туннелям и нашли выход из замка.")
    print("1. Выбросить дичь на свободу.")
    print("2. Вернуться в замок и разоблачить злодея.")
    choice = input("Выберите вариант (1 или 2): ")
    if choice == "1":
        print("Поздравляю! Вы успешно освободились из замка и помогли дичи найти свободу. Игра окончена.")
    elif choice == "2":
        chapter_11()
    else:
        print("Пожалуйста, выберите допустимый вариант.")
        chapter_9()

def chapter_10():
    print("\nГлава 10: Проклятие")
    print("Пока вы исследуете зал магии, вас захватывает проклятие и вы становитесь пленником замка вновь.")
    print("1. Попытаться снять проклятие.")
    print("2. Найти другой выход.")
    choice = input("Выберите вариант (1 или 2): ")
    if choice == "1":
        chapter_12()
    elif choice == "2":
        chapter_6()
    else:
        print("Пожалуйста, выберите допустимый вариант.")
        chapter_10()

def chapter_11():
    print("\nГлава 11: Битва")
    print("Вы возвращаетесь в замок, готовые разоблачить злодея и сразиться с ним в битве.")
    print("1. Подготовиться к битве.")
    print("2. Попытаться убежать.")
    choice = input("Выберите вариант (1 или 2): ")

    if choice == "1":
        chapter_12()
    elif choice == "2":
        chapter_6()
    else:
        print("Пожалуйста, выберите допустимый вариант.")
        chapter_11()
def chapter_12():
            print("\nГлава 12: Свобода")
            print("Вы успешно покинули замок и восстановили свободу!")
            print("Спасибо за игру!")


def save_game_data(data):
    save_data(data, "game_data.json")
    write_to_csv(data["users"], "game_data.csv")
    print("Данные сохранены и записаны в файлы.")



if __name__ == "__main__":
    start_game()
    data = {
        "users": [
            {
                "name": "Ramil",
                "data": "25.10.2023"
            },

        ]
    }
    save_game_data(data)
#только что заметил, что отправил не тот код,код показывал другу, что мы делаем на вашем прекрасном уроке)
