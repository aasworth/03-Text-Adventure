import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def render():
    '''DISPLAY THE CURRENT LOCATION'''
    print("\n",game['rooms'][current]['name'])
    if game['rooms'][current]['desc']:
        print(game['rooms'][current]['desc'])
    for exit in game['rooms'][current]['exits']:
        print(exit.get('verb')) 
    return True

def update():
    ''' UPDATE OUR LOCATION IF POSSIBLE, ETC.'''
    global current
    for exit in game['rooms'][current]['exits']:
        if response == exit.get('verb'):
            if exit.get('target') == 'NoExit':
                print("Sorry, That is not an option. Please select another option.")
            elif exit.get('target') != 'NoExit':
                current = exit.get('target')
    return current

def check_input():
    '''GET USER INPUT'''
    global quit
    global response
    response = input("Where would you like to go? ") 
    return response


game = {}
with open('zork.json') as json_file:        #Put the zork.json information inside of a dictionary named game, so that I can pull the information out to use inside of the game
    game = json.load(json_file)
current = 'WHOUS'    #Sets the current place in the world
option = 'exits'    #Sets the current option the player has chosen
response = ''
def main():
    
    
    # Your game goes here!
        # Here will add code to make the game! give player options, choices, and things to do.

    quit = False

    while not quit:
        
        #Render
        render()
        #Check player input
        check_input()
        #Update the status of the world
        update()


    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()


#TO-DO
# Implement a quit function
# Implement an inventory function