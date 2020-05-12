from settings import *
import models
import pymongo

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
# f"mongodb+srv://{USER}:{PASSWORD}@cluster0-idlrk.azure.mongodb.net/test?retryWrites=true&w=majority"
database = mongoclient["mydatabase"]
dbproj = database["projects"]
dbcale = database["calendar"]


# PROJECTS
def addproject(project):  # new project
    new = {'project': project}
    dbproj.insert_one(new)
def changeproject(name, project):  # update
    old = {"name": name}
    new = {"$set": {'name': project['name'], "project": project}}
    dbproj.update_one(old, new)
def deleteproject(project):  # delete
    wbd = {"project": project}
    dbproj.delete_one(wbd)
def getprojects():  # find
    return dbproj.find()

# PROJECT TASKS
def addptask(proj, task):  # new
    new = {'task': task}
    dbproj[proj]['tasks'].insert_one(new)
def changeptask(proj, task, newtask):  # update
    old = {"task": task}
    new = {"$set": {"task": newtask}}
    dbproj[proj]['tasks'].update_one(old, new)
def deleteptask(proj, task):  # delete
    wbd = {"task": task}
    dbproj[proj]['tasks'].delete_one(wbd)
def getptask(proj):  # find
    return dbproj[proj]["tasks"].find()

# CALENDAR TASKS
def addctask(date, task):  # new calendar task
    new = {'task': task}
    dbcale[date]['tasks'].insert_one(new)
def changectask(date, task, newtask):  # update
    old = {'task': task}
    new = {"$set": {'task': newtask}}
    dbcale[date].update_one(old, new)
def deletectask(date, task):  # delete
    wbd = {'task': task}
    dbcale[date].delete_one(wbd)
def getctask(date):  # find
    return dbcale[date]['tasks'].find()

# DATABASE
def _clearDatabase():
    for col in database.collection_names():
        database.drop_collection(col)
def _showDatabase():
    for col in database.collection_names():
        print("Collection name :", database[col])
        for i in database[col].find():
            print(i)


def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # dblist = myclient.list_database_names()

    mydb = myclient["mydatabase"]
    # collist = mydb.list_collection_names()

    _showDatabase()

    # for x in mycol.find({}, {"_id": 0}):
    #     print(x)

    # Добавить несколько
    # mylist = [{"name": "Amy", "address": "Apple st 652"},
    #           {"name": "Hannah", "address": "Mountain 21"},]
    # mycol.insert_many(mylist)

    # Найти find() или find_one()
    # myquery = { "address": { "$regex": "^S" } } поиск адреса который начинается с буквы S
    # mydoc = mycol.find(myquery)
    # mydoc = mycol.find().sort("name", 1) сортировать по возрастанию /(-1) по убыванию

    # Удалить много
    # myquery = { "address": {"$regex": "^S"} }
    # mycol.delete_many(myquery)
    # Удалить все mycol.delete_many( {} )

    # Обновить много
    # myquery = {"address": {"$regex": "^S"}}
    # newvalues = {"$set": {"name": "Minnie"}}
    # x = mycol.update_many(myquery, newvalues)

    # ограничить результат
    # mycol.find().limit( int ) принимает только один параметр, число (количество результатов)


if __name__ == '__main__':
    main()
