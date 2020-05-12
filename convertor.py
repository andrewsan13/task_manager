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
    temp = convert_to_dict(Project(name))
    database.addproject(temp)
def addprojecttask():
    pass
def addcalendartask():
    pass
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
    temp = []
    for each in data:
        proj = convert_to_obj(each['project'])
        temp.append(proj)
    return temp
def getprojecttask():
    pass
def getcalendartask():
    pass
