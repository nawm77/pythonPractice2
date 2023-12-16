import json


#Метод который позволяет читать данные из файла .json
def get_database():
    with open("db.json", encoding="utf-8") as db_file:
        return json.load(db_file)


#метод для сохранения данных в формате JSON в .json файл
def save_into_database(data):
    with open("db.json", "w", encoding="utf-8", ) as db_file:
        json.dump(data, db_file, ensure_ascii=False)