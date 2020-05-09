from settings import *
import pymongo

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
# f"mongodb+srv://{USER}:{PASSWORD}@cluster0-idlrk.azure.mongodb.net/test?retryWrites=true&w=majority"
database = mongoclient["mydatabase"]
dbproj = database["projects"]
dbcale = database["calendar"]


# PROJECTS
def nproject(name):  # new project
    new = {"name": name, "tasks": {}}
    dbproj.insert_one(new)


def uproject(name, new_name):  # update
    old = {"name": name}
    new = {"$set": {"name": new_name}}
    dbproj.update_one(old, new)


def dproject(name):  # delete
    wbd = {"name": name}
    dbproj.delete_one(wbd)


def fproject():  # find
    return dbproj.find({}, {"tasks": 0})


# PROJECT TASKS
def nptask(proj, name, status, priority):  # new
    new = {"name": name, "status": status, "priority": priority}
    dbproj[proj].insert_one(new)


def uptask(proj, name, new_name, status, priority):  # update
    old = {"name": name}
    new = {"$set": {"name": new_name, "status": status, "priority": priority}}
    dbproj[proj].update_one(old, new)


def dptask(proj, name):  # delete
    wbd = {"name": name}
    dbproj[proj].delete_one(wbd)


def fptask(proj):  # find
    return dbproj[proj]["tasks"].find({}, {"_id": 0})


# CALENDAR TASKS
def nctask(date, name, status, priority):  # new calendar task
    new = {"name": name, "status": status, "priority": priority}
    dbcale[date].insert_one(new)


def uctask(date, name, new_name, status, priority):  # update
    old = {"name": name}
    new = {"$set": {"name": new_name, "status": status, "priority": priority}}
    dbcale[date].update_one(old, new)


def dctask(date, name):  # delete
    wbd = {"name": name}
    dbcale[date].delete_one(wbd)


def fctask(date):  # find
    return dbcale[date].find({}, {"_id": 0})


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
