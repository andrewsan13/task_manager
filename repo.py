import json
from collections import namedtuple
from json import JSONEncoder

#  from json in obj
def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())


# Assume you received this JSON response
studentJsonData = '{"rollNumber": 1, "name": "Emma"}'

# Parse JSON into an object with attributes corresponding to dict keys.
student = json.loads(studentJsonData, object_hook=customStudentDecoder)

print("After Converting JSON Data into Custom Python Object")
print(student.rollNumber, student.name)

# After Converting JSON Data into Custom Python Object
# 1 Emma

#  convert into json
