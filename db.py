from settings import *
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# f"mongodb+srv://{USER}:{PASSWORD}@cluster0-idlrk.azure.mongodb.net/test?retryWrites=true&w=majority"
mydb = myclient["mydatabase"]


def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # dblist = myclient.list_database_names()

    mydb = myclient["mydatabase"]

    mycol = mydb["customers"]
    # collist = mydb.list_collection_names()

    # for x in mycol.find({}, {"_id": 0}):
    #     print(x)

    # Добавить
    # mydict = {"name": "John", "address": "Highway 37"}
    # x = mycol.insert_one(mydict)
    # Добавить несколько
    # mylist = [{"name": "Amy", "address": "Apple st 652"},
    #           {"name": "Hannah", "address": "Mountain 21"},]
    # mycol.insert_many(mylist)

    # Найти find() или find_one()
    # myquery = { "address": { "$regex": "^S" } } поиск адреса который начинается с буквы S
    # mydoc = mycol.find(myquery)
    # mydoc = mycol.find().sort("name", 1) сортировать по возрастанию /(-1) по убыванию

    # Удалить
    # myquery = { "address": "Mountain 21" }
    # mycol.delete_one(myquery)
    # myquery = { "address": {"$regex": "^S"} }
    # mycol.delete_many(myquery)
    # Удалить все mycol.delete_many( {} )

    # Удалить коллекцию или таблицу
    # mycol.drop()

    # Обновить
    # myquery = {"address": "Valley 345"}
    # newvalues = {"$set": {"address": "Canyon 123"}}
    # mycol.update_one(myquery, newvalues)
    # Обновить много
    # myquery = {"address": {"$regex": "^S"}}
    # newvalues = {"$set": {"name": "Minnie"}}
    # x = mycol.update_many(myquery, newvalues)

    # ограничить результат
    # mycol.find().limit( int ) принимает только один параметр, число (количество результатов)


if __name__ == '__main__':
    main()
