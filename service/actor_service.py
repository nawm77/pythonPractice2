import utils.db_service as json_service

entity_name = "actors"


def get_all():
    db = json_service.get_database()
    return db[entity_name]


def get_one_by_id(id):
    db = json_service.get_database()
    for element in db[entity_name]:
        if element["id"] == id:
            return element
    return {"message": f"Элемент с id {id} не найден"}


def update_one_by_id(id, actor):
    db = json_service.get_database()
    for i, elem in enumerate(db[entity_name]):
        if elem["id"] == id:
            elem["name"] = actor["name"]
            elem["age"] = actor["age"]
            elem["social network"] = actor["social network"]
            json_service.save_into_database(db)
            print(f"Актер {elem['name']} успешно обновлен")
            return elem
    return {"message": f"Элемент с id {id} не найден"}


def create_one(actor):
    db = json_service.get_database()
    if len(get_all()) > 0:
        last_id = get_all()[-1]["id"]
    else:
        last_id = 0
    db[entity_name].append({"id": last_id + 1, **actor})
    json_service.save_into_database(db)
    print(f"Актер с именем {actor['name']} успешно сохранен")


def delete_one_by_id(id):
    db = json_service.get_database()
    for i, elem in enumerate(db[entity_name]):
        if elem["id"] == id:
            obj = db[entity_name].pop(i)
            json_service.save_into_database(db)
            return obj
    return {"message": f"Элемент с id {id} не найден"}
