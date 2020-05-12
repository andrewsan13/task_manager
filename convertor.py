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
    tmp = convert_to_dict(Project(name))
    database.addproject(tmp)
def addprojecttask(proj, name, priority):
    new = Task(name, priority)
    tmp = convert_to_dict(new)
    database.addptask(proj, tmp)
def addcalendartask(date, name, priority):
    new = Task(name, priority)
    tmp = convert_to_dict(new)
    database.addctask(date, tmp)
def updateproject():
    pass
def updateprojecttask():
    pass
def updatecalendartask():
    pass
def deleteproject():
    pass
def deleteprojecttask():
    pass
def deletecalendartask():
    pass
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
