import random

peopleDict = {}
peopleDict["Sophia"] = "https://cdn.discordapp.com/attachments/953827200019361802/953886865876992030/152825.jpeg"
peopleDict["Andrew"] = "https://cdn.discordapp.com/attachments/953827200019361802/953886881869881424/169880.jpeg"
peopleDict["Justin"] = "https://cdn.discordapp.com/attachments/953827200019361802/953888804572381245/059627.jpeg"

def randPic():
  return random.choice(list(peopleDict))

def getPic(name):
  return peopleDict[name]
