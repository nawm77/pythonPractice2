from service import role_service
from service import actor_service
from service import audience_service
from service import performance_service

msg = "Введите номер действия для продолжения работы"


# Отображаем первоначальное меню ввода для пользователя
def menu():
    print("Menu:")
    print("1) меню действия с актерами")
    print("2) меню действия с аудиторией")
    print("3) меню действия с выступлениями")
    print("4) меню действия с ролями")
    print("5) Завершение работы")


# Отображаем меню для работы с конкретной сущностью
def entity_menu(entity):
    print(f"1) Получить все объекты сущности {entity}")
    print(f"2) Получить объект сущности {entity} по его ID")
    print(f"3) Удалить объект сущности {entity} по его ID")
    print(f"4) Создать новый объект сущности {entity}")
    print(f"5) Редактировать объект сущности {entity} по его ID")


# Валидируем то, что написал нам пользователь (цифра это, или строка)
def validate_user_input(message, type):
    while True:
        print(message)
        user_input = input()
        if type == "number" and user_input.isdigit():
            return int(user_input)
        elif type == "string":
            return user_input
        else:
            print("Неверный формат входжных данных. Введите повторно корректные данные")


# возвращаем для работы определенный сервис, для того, чтобы избежать проблему дублирования одного и того же кода
# В лучшем случае можно вообще выдавать ошибку, что нет корректного сервиса,
# но в нашем случае это не нужно, тк мы сами эти сервисы в коде вызываем, а не пользователь вызывает
def on_action_with_entity(entity):
    if entity == "actor":
        return actor_service
    elif entity == "role":
        return role_service
    elif entity == "audience":
        return audience_service
    elif entity == "performance":
        return performance_service
    return None


# Производим одно из действий, которое у всех одинаковое (получение всех, получение одного, судаление одного)
def do_action(action_service, action):
    if action == 1:
        print(action_service.get_all())
    elif action == 2:
        id = validate_user_input("Введите ID", "number")
        print(action_service.get_one_by_id(id))
    elif action == 3:
        id = validate_user_input("Введите ID", "number")
        print(action_service.delete_one_by_id(id))
    print("--------------------------")

# main метод для запуска программы
def main():
    while True:
        # отображаем меню с первоначальным вводом
        menu()
        user_choice = validate_user_input(msg, "number")
        if user_choice == 5:
            print("Завершаем работу")
            break
        #     Для актера
        elif user_choice == 1:
            # подменяем реализацию сервиса
            current_service = on_action_with_entity("actor")
            # отображаем меню для действий к актеру
            entity_menu("actor")
            # определяем экшн (дейтсиве), которое будем делать (создание, удаление, поиск, обновление)
            action = validate_user_input(msg, "number")
            # если же мы работаем с созданием, или обновлением, то пока что можно написать так, тк у всех сущностей разное кол-во полей
            if action == 4:
                name = validate_user_input("Введите имя актера", "string")
                age = validate_user_input("Введите возраст актера", "number")
                social_network = validate_user_input("Введите соц.сеть актера", "string")
                actor = {"name": name, "age": age, "social network": social_network}
                current_service.create_one(actor)
            elif action == 5:
                id = validate_user_input("Введите ID", "number")
                name = validate_user_input("Введите имя актера", "string")
                age = validate_user_input("Введите возраст актера", "number")
                social_network = validate_user_input("Введите соц.сеть актера", "string")
                actor = {"name": name, "age": age, "social network": social_network}
                current_service.update_one_by_id(id, actor)
            else:
                do_action(current_service, action)
        #         TODO доделать реализацию для всех сущностей + сделать вывод итога для создания, удаления и обновления сущности, как делали это в конце занятия в сервисе. То есть печатать удалось ли сделать или нет
        elif user_choice == 2:
            current_service = on_action_with_entity("audience")
            entity_menu("audience")
            action = validate_user_input(msg, "number")
            do_action(current_service, action)


if __name__ == "__main__":
    main()
