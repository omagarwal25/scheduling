import json
from treelib import Node, Tree
from HSClass import HSClass

masterList = {}

#opens up the json with classes and loads it up
with open("classes.json") as json_file:
    data = json.load(json_file)

#loads each class into a HSClass storing all of its properties
for i in data:
    a = data[i]
    masterList[a["name"]] = HSClass(a["name"], a["pre"], a["post"], a["credits"], a["gradeReq"], a["sem"], True, a["con"], a["prestige"])

def returnMasterList():
    return masterList

def returnPre(name):
    """
    returns the prereqests for a given class.
    """
    return masterList[name].returnAll()["pre"][0]

#starts of the generation of a tree for a given class
def initSearch(name):
    """
    starts the search for the tree
    """
    a = Tree()
    a.create_node(name, name)
    getAllPrimaryPre(name, a, name)
    return a

def getAllPrimaryPre(name, tree, parent_name):
    """
    tree search for the json
    """
    a = tree
    x = name
    for i in returnPre(x):
        if i != 0:
            if a.get_node(i) == 0:
                a.create_node(i, i, parent = parent_name)
                new_parent_name = i
            else:
                a.create_node(i, i + parent_name, parent = parent_name)
                new_parent_name = i + parent_name
            if returnPre(i)[0] != 0:
                getAllPrimaryPre(i, a, new_parent_name)

def turnTreeLeaves(l):
    """
    Turns a tree output into a set of arrays
    """
    b = l.paths_to_leaves()
    y = 0
    for i in b:
        z = 0
        for x in i:
            b[y][z] = l.get_node(x).tag
            z = z + 1
        y = y + 1
    return b

def findHighestPres(cleanedUpTree):
    """
    finds the most presideous route
    """
    highestOutputPres = 0
    highestOutput = 0
    lowestLen = 999
    lenMatched = []

    for i in cleanedUpTree:
        if len(i) < lowestLen:
            lowestLen = len(i)
        
    for i in cleanedUpTree:
        if len(i) == lowestLen:
            lenMatched.append(i)

    for i in lenMatched:
        currentPres = 0
        for x in i:
            currentPres = currentPres + masterList[x].returnAll()["prestige"]
        if currentPres > highestOutputPres:
            highestOutputPres = currentPres
            highestOutput = i
    return highestOutput
