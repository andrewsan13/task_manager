from settings import *
import models
import pymongo
from bson.objectid import ObjectId

# mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongoclient = pymongo.MongoClient(
    f"mongodb+srv://{USER}:{PASSWORD}@cluster0-idlrk.azure.mongodb.net/test?retryWrites=true&w=majority", connect=False)

# db = mongoclient.test
database = mongoclient[f"{USER}_taskmanager"]
dbproj = database["projects"]
dbcale = database["calendar"]


# PROJECTS
def addproject(name, project):  # new project
    new = {'name': name, 'project': project}
    dbproj.insert_one(new)


def editproject(last, newname, project):  # update
    old = {"name": last}
    new = {"$set": {'name': newname, "project": project}}
    dbproj[newname]['tasks'] = dbproj[last]['tasks']  # таски со старого имени кидаем в новое
    dbproj.update_one(old, new)
    if dbproj[last]['tasks']:
        database.drop_collection(f'projects.{last}.tasks')  # удаляем таски старого имени


def deleteproject(name):  # delete
    wbd = {"name": name}
    dbproj.delete_many(wbd)
    if dbproj[name]['tasks']:
        database.drop_collection(f'projects.{name}.tasks') # Удаляем таски этого проэкта dbproj[name]['tasks']
    tmp = []
    for i in getprojects():
        tmp.append(i)
    if not tmp:
        database.drop_collection('projects')


def getprojects():  # find
    return dbproj.find()


def findoneproject(name):
    return dbproj.find_one({'name': name})

def getdates():
    return dbcale.find()


# PROJECT TASKS
def addptask(proj, taskname, task):  # new
    new = {'name': taskname, 'task': task}
    dbproj[proj]['tasks'].insert_one(new)


def editptask(proj, oldname, newname, task):  # update
    old = {"name": oldname}
    new = {"$set": {'name': newname, "task": task}}
    dbproj[proj]['tasks'].update_one(old, new)


def deleteptask(proj, name):  # delete
    wbd = {"name": name}
    dbproj[proj]['tasks'].delete_one(wbd)
    

def getptask(proj):  # find
    return dbproj[proj]['tasks'].find()


# CALENDAR TASKS
def addctask(date, name, task):  # new calendar task
    new = {'name': name, 'task': task}
    dbcale[date]['tasks'].insert_one(new)


def editctask(date, oldname, newname, task):  # update
    old = {'name': oldname}
    new = {"$set": {'name': newname, 'task': task}}
    dbcale[date].update_one(old, new)


def deletectask(date, name):  # delete
    wbd = {'name': name}
    dbcale[date]['tasks'].delete_one(wbd)
    tmp = []
    for each in dbcale[date]['tasks'].find():
        tmp.append(each)
    if not tmp:
        database.drop_collection(f'calendar.PyQt5.QtCore.QDate({date.year()}, {date.month()}, {date.day()}).tasks')


def getctask(date):  # find
    return dbcale[date]['tasks'].find()


# DATABASE
def _clearDatabase():
    for one in database.list_collection_names():
        database.drop_collection(one)



def _showDatabase():
    for col in database.list_collection_names():
        print("Collection name :", col)


def main():
    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # dblist = myclient.list_database_names()

    # mydb = myclient["mydatabase"]
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
