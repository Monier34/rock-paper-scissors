import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Сделайте выбор - ({choices_str}): "))
    action = Action(selection)
    return action


def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


def determinate_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Оба пользователя выбрали {user_action.name}. Ничья!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")


while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Некорректный ввод. Введите значение из промежутка {range_str}")
        continue

    computer_action = get_computer_selection()
    determinate_winner(user_action, computer_action)

    play_again = input("Сыграем еще? (д/н): ")
    if play_again.lower() != "д":
        break
