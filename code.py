def render():
    '''DISPLAY THE CURRENT LOCATION'''
    i = 1
    print("Location: ", game['rooms'][current]['name'])
    response = check_input()
    if response == str(3):
        for exit in game['rooms'][current]['exits']:
            print(i, exit.get('verb'))
            i = i + 1
    elif response == str(2):
        print("Description: ", game['rooms'][current]['desc'])
    elif response== str(1):
        print("Location: ", game['rooms'][current]['name'])
    return True