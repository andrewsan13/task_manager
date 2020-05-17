import models
import pymongo

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mongoclient = pymongo.MongoClient(
    # f"mongodb+srv://{USER}:{PASSWORD}@cluster0-idlrk.azure.mongodb.net/test?retryWrites=true&w=majority", connect=False)

database = mongoclient["taskmanager"]
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
    if dbproj[last]:
        del dbproj[last]  # удаляем таски старого имени


def deleteproject(name):  # delete
    wbd = {"name": name}
    dbproj.delete_one(wbd)
    if dbproj[name]:
        del dbproj[name]  # Удаляем таски этого проэкта dbproj[name]['tasks']


def getprojects():  # find
    return dbproj.find()


def findoneproject(name):
    return dbproj.find_one({'name': name})


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
