import utils.db_service as json_service

entity_name = "performances"


def get_all():
    db = json_service.get_database()
    return db[entity_name]


def get_one_by_id(id):
    db = json_service.get_database()
    for element in db[entity_name]:
        if element["id"] == id:
            return element
    return {"message": f"Элемент с id {id} не найден"}


def update_one_by_id(id, performance):
    db = json_service.get_database()
    for i, elem in enumerate(db[entity_name]):
        if elem["id"] == id:
            elem["name"] = performance["name"]
            elem["time"] = performance["time"]
            elem["date"] = performance["date"]
            elem["ticket price"] = performance["ticket price"]
            json_service.save_into_database(db)
            return elem
    return {"message": f"Элемент с id {id} не найден"}


def create_one(performance):
    db = json_service.get_database()
    if len(get_all()) > 0:
        last_id = get_all()[-1]["id"]
    else:
        last_id = 0
    db[entity_name].append({"id": last_id + 1, **performance})
    json_service.save_into_database(db)


def delete_one_by_id(id):
    db = json_service.get_database()
    for i, elem in enumerate(db[entity_name]):
        if elem["id"] == id:
            obj = db[entity_name].pop(i)
            json_service.save_into_database(db)
            return obj
    return {"message": f"Элемент с id {id} не найден"}

# def get_all_with_name():
# db = json_service.get_database()
# for i, elem in enumerate(db["performance"]):
# for j, element in enumerate(elem["category"]):
# print(element)
