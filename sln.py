import re
import math
def getContent(fileURL):
    '''
    Getting the content of the URL. To not overwhelm the Advent of code server, I have saved
    the file locally as a text file. There shouldn't be the need for these exceptions as I have included the
    text file in the repo, but it is meant to be good coding practices
    '''
    try:
        with open(fileURL, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{fileUrl}' not found")
        return None
    except Exception as e:
        print(f"Error Occurred: {e}")
        return None
    
def proveTrue(text):
    colorDict = {"blue":14, "green": 13, "red":12}
    pattern = re.compile(r'(\d+) ([a-zA-Z)]+)')
    retVal = True
    for match in pattern.findall(text):
        number, color = match
        if int(number) > colorDict[color]:
            retVal = False
    return retVal

def partTwo(text):
    colorDict = {"blue":0, "green": 0, "red":0}
    pattern = re.compile(r'(\d+) ([a-zA-Z)]+)')
    for match in pattern.findall(text):
        number, color = match
        if int(number) > int(colorDict[color]):
            colorDict[color] = number
    mul = 1
    return math.prod([mul*int(x) for x in colorDict.values()])

if __name__ == "__main__":
    textStr = getContent("input.txt")
    textSplit = textStr.splitlines()
    totSum = 0
    for i in range(len(textSplit)):
        if proveTrue(textSplit[i]):
            totSum += (i+1)
    print(totSum)
    totSum2 = 0
    for texts in textSplit:
        totSum2 += partTwo(texts)
    print(totSum2)