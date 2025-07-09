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

def load_memory_dict(address):
    '''
    attempts to load existing memory as dict if existing memory file does
    not exist returns an empty dict
    :args: address: string
    :inputs: None
    :return: memory: Dictionary object
    '''
    memory = getJson(address)
    if memory != FileNotFoundError and isinstance(memory, dict):
        return memory
    else:
        return {}  
    
def load_memory_list(address):
    '''
    attempts to load existing memory as list if existing memory file does
    not exist returns an empty list
    :args: address: string
    :inputs: None
    :return: memory: list
    '''
    memory = getJson(address)
    if memory != FileNotFoundError and isinstance(memory, list):
        return memory
    else:
        return []