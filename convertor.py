import json
from collections import namedtuple
from json import JSONEncoder

from models import *
import database

# JSON
#  from json to obj
def objectDecoder(objdict):
    return namedtuple('X', objdict.keys())(*objdict.values())


#  convert to json
class objectEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def convert_to_dict(obj):
    return json.dumps(obj, indent=4, cls=objectEncoder)


def convert_to_obj(values):
    return json.loads(values, object_hook=objectDecoder)


# DATA
def addproject(name):
    proj = convert_to_dict(Project(name))
    database.addproject(name, proj)
def addprojecttask(proj, name, priority):
    new = Task(name, priority)
    task = convert_to_dict(new)
    database.addptask(proj, name, task)
def addcalendartask(date, name, priority):
    new = Task(name, priority)
    task = convert_to_dict(new)
    database.addctask(date, name, task)

def editproject(oldname, newname):
    proj = Project(newname)
    updated = convert_to_dict(proj)
    database.editproject(oldname, newname, updated)
def editprojecttask(project, oldname, newname, priority, status):
    task = Task(newname, priority, status)
    new = convert_to_dict(task)
    database.editptask(project, oldname, newname, new)
def editcalendartask(date, oldname, newname, priority, status):
    task = Task(newname, priority, status)
    new = convert_to_dict(task)
    database.editctask(date, oldname, newname, new)

def deleteproject(name):
    database.deleteproject(name)
def deleteprojecttask(proj, taskname):
    database.deleteptask(proj, taskname)
def deletecalendartask(date, name):
    database.deletectask(date, name)

def getprojects():
    data = database.getprojects()
    tmp = []
    for each in data:
        proj = convert_to_obj(each['project'])
        tmp.append(proj)
    return tmp
def getprojecttask(proj):
    data = database.getptask(proj)
    tmp = []
    for each in data:
        task = convert_to_obj(each['task'])
        tmp.append(task)
    return tmp
def getcalendartask(date):
    data = database.getctask(date)
    tmp = []
    for each in data:
        task = convert_to_obj(each['task'])
        tmp.append(task)
    return tmp

def get_all():
    tmp = []
    ps = database.getprojects()
    ds = database.getdates()
    for i in ps:
        tasks = getprojecttask(i['name'])
        tmp.extend(tasks)
    for i in ds:
        tasks = getcalendartask(i)
        tmp.extend(tasks)
    print(tmp)

