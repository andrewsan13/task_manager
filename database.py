from settings import *
import models
import pymongo
from bson.objectid import ObjectId

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
# f"mongodb+srv://{USER}:{PASSWORD}@cluster0-idlrk.azure.mongodb.net/test?retryWrites=true&w=majority"
database = mongoclient["mydatabase"]
dbproj = database["projects"]
dbcale = database["calendar"]


# PROJECTS
def addproject(name, project):  # new project
    new = {'name': name, 'project': project, 'tasks': {}}
    dbproj.insert_one(new)
def editproject(last, newname, project):  # update
    old = {"name": last}
    # tasks = findoneproject(last)['tasks']
    new = {"$set": {'name': newname, "project": project}}
    dbproj.update_one(old, new)
def deleteproject(project):  # delete
    wbd = {"project": project}
    dbproj.delete_one(wbd)
def getprojects():  # find
    return dbproj.find()
def findoneproject(name):
    return dbproj.find_one({'name': name})

# PROJECT TASKS
def addptask(proj, task):  # new
    name = findoneproject(proj)
    name['tasks'].update({'_id': ObjectId(), 'task': task})
    new = {"$set": {'name': name['name'], 'project': name['project'], 'tasks': name['tasks']}}
    dbproj.update_one({'name': name['name']}, new)
    # dbproj[name]['tasks'].insert_one(new)
def editptask(proj, task, newtask):  # update
    old = {"task": task}
    new = {"$set": {"task": newtask}}
    dbproj[proj]['tasks'].update_one(old, new)
def deleteptask(proj, task):  # delete
    wbd = {"task": task}
    dbproj[proj]['tasks'].delete_one(wbd)
def getptask(proj):  # find
    obj = findoneproject(proj)
    tmp = []
    for i in obj['tasks']:
        tmp.append(i[1])
    return tmp

# CALENDAR TASKS
def addctask(date, task):  # new calendar task
    new = {'task': task}
    dbcale[date]['tasks'].insert_one(new)
def editctask(date, task, newtask):  # update
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

    _clearDatabase()

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
