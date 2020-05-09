from settings import *
import pymongo

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
# f"mongodb+srv://{USER}:{PASSWORD}@cluster0-idlrk.azure.mongodb.net/test?retryWrites=true&w=majority"
database = mongoclient["mydatabase"]
dbproj = database["projects"]
dbcale = database["calendar"]


# PROJECTS
def nproject(project):  # new project
    new = {"project": project, "tasks": {}}
    dbproj.insert_one(new)


def uproject(project, new_data):  # update
    old = {"project": project}
    new = {"$set": {"project": new_data}}
    dbproj.update_one(old, new)


def dproject(project):  # delete
    wbd = {"project": project}
    dbproj.delete_one(wbd)


def fproject():  # find
    return dbproj.find({}, {"tasks": 0})


# PROJECT TASKS
def nptask(proj, task):  # new
    new = {'task': task}
    dbproj[proj].insert_one(new)


def uptask(proj, task, newtask):  # update
    old = {"task": task}
    new = {"$set": {"task": newtask}}
    dbproj[proj].update_one(old, new)


def dptask(proj, task):  # delete
    wbd = {"task": task}
    dbproj[proj].delete_one(wbd)


def fptask(proj):  # find
    return dbproj[proj]["tasks"].find({}, {"_id": 0})


# CALENDAR TASKS
def nctask(date, task):  # new calendar task
    new = {'task': task}
    dbcale[date].insert_one(new)


def uctask(date, task, newtask):  # update
    old = {'task': task}
    new = {"$set": {'task': task}}
    dbcale[date].update_one(old, new)


def dctask(date, task):  # delete
    wbd = {'task': task}
    dbcale[date].delete_one(wbd)


def fctask(date):  # find
    return dbcale[date].find({}, {"_id": 0})


def _clearDatabase():
    for col in database.collection_names()
        database.drop_collection(col)


def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # dblist = myclient.list_database_names()

    mydb = myclient["mydatabase"]
    # collist = mydb.list_collection_names()
    mycol = mydb["projects"]
    for x in mycol.find():
        print(x)
        print(type(x))
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
