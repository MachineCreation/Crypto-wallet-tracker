def printInputError(error):
    '''
    prints an error to the user
    :args: None
    :input: None
    :return: None
    '''

    print(error)

def printDelineator():
    '''
    prints 79 character delineator line
    :args: None
    :input: None
    :return: None
    '''
    print('------------------------------------------------------------------------------\n')
def welcomeMessage(appName, optDescription = None):
    '''
    prints welcome message with optional app description
    :args: appName: string, optDescription: string default = None
    :input: None
    :return: None
    '''
    print(f'Welcome to the {appName} app')

    if optDescription:
        print(f'{optDescription}')
    
    print()
    

def print_menu_options(opt, prompt = "Enter what you would like to do from the choices below"):
    '''
    prompts user to choose from menu options.\n
    :args: opt: string List, prompt:\n 
        string default = Enter what you would like to do from the choices below
    :input: None\n
    :return: None
    '''
    
    print(prompt)
    for o in opt:
        print(f'-{o}')

def printConfirmation(action, prompt = 'continue? y/n\n'):
    '''
    prompts the user to confirm a choice with y/n
    :args: action: string, prompt: string default continue?
    :inputs: confirm: string
    :return: confirm: boolean
    '''
    print(action)
    while True:
        uInput = input(prompt).lower()
        if uInput != 'n' and uInput != 'y':
            printInputError('invalid entry')
        else:
            return uInput == 'y'

def exitMessage():
    '''
    prints exit message
    :args: None
    :input: None
    :return: None
    '''
    print('\nHave a wonderful day!')