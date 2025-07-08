# get files by type
import json

def getJson(fileName):
    '''
    tries to open and read .json file. if file does not exist returns
    FileNotFoundError class
    :args: fileName: string
    :inputs: None
    :return: f: raw file contents | FileNotFoundError
    '''
    try:
        with open(fileName + '.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return FileNotFoundError
    
# make file by type

def makeJson(data, fileName):
    '''
    overwrites or makes new json file in parent folder
    :args: data: any, fileName: string
    :inputs: None
    :return: None
    '''
    with open(fileName + '.json', 'w')as f:
        json.dump(data, f, indent=4)