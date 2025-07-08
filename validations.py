import messages as M

def get_Y_N(prompt = 'Would you like to continue? Y/N: '):
    '''
    prompts the user for 'y' or 'n' input (case-insensitive), with error handling for invalid entries
    :args: prompt: string (optional)
    :return: uInput: string ('y' or 'n')
    '''
    while True:
        uInput = input(prompt).lower()
        if uInput != 'n' and uInput != 'y':
            M.printInputError('invalid entry')
        else:
            return uInput
        
def validateString(prompt="Please enter a string: "):
    '''
    prompts the user for a non-empty string input, with error handling for empty entries
    :args: prompt: string
    :return: uString: string (non-empty)
    '''
    uString = input(prompt)
    while True:
        if uString != '':
            return uString
        else:
            M.printInputError('invalid empty input.')
            uString = input(prompt)

def validateInteger(string="Please enter an integer: "):
    '''
    prompts the user for a non-negative integer input, with error handling for invalid entries
    :args: string: string (prompt for input)
    :return: number: int (non-negative integer)
    '''
    while True:
        number = validateString(string)
        try:
            number = int(number)
            if number >= 0:
                return number
            else:
                raise ValueError
        except ValueError:
            M.printInputError('Invalid integer')
            
def get_real(prompt="Please enter a real number: "):
  """
  Function to prompt for and return a valid real number
  :param prompt: string Optional string to use as prompt
  :return: float Valid real number
  """
  num = 0.0
  while True:
      try:
          num = float(input(prompt))
          return num
      except ValueError:
          print("Invalid number.")

# TODO create dynamic validator for lists
def validateChoiceFromList(optionsList, prompt = None, case = 'lower'):
    '''
    validates user input is in list of options\n
    :args: optionsList: string List, prompt: string default = None, 
    case: string default = lower\n
    :inputs: choice: \n
    :return: choice: string
    '''
    while True:
        # check for case 
        if case == 'lower':
            choice = validateString('').lower()
        elif case == 'upper':
            choice = validateString('').upper()
        else:
            choice = validateString('').title()

        if choice in optionsList:
            return choice
        else:
            print('----Invalid entry----')
            if prompt:
                M.print_menu_options(optionsList, prompt)
            else:
                M.print_menu_options(optionsList)