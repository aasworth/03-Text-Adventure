import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def render():
    '''DISPLAY THE CURRENT LOCATION'''
    i = 1
    print("Location: ", game['rooms'][current]['name'])
    response = check_input()
    if response == str(3):
        for exit in game['rooms']['WHOUS']['exits']:
            print(i, exit.get('verb'))
            i = i + 1
    elif response == str(2):
        print("Description: ", game['rooms'][current]['desc'])
    elif response== str(1):
        print("Location: ", game['rooms'][current]['name'])
    return True

def update():
    ''' UPDATE OUR LOCATION IF POSSIBLE, ETC.'''

    return True

def check_input():
    '''GET USER INPUT'''
    response = input('What would you like to do? ')
    
    return response

#Put the zork.json information inside of a dictionary named game, so that I can pull the information out to use inside of the game
game = {}
with open('zork.json') as json_file:
    game = json.load(json_file)
current = 'WHOUS'       #Sets the current place in the world
option = 'exits'         #Sets the current option the player has chosen
def main():
    
    # Your game goes here!
        # Here will add code to make the game! give player options, choices, and things to do.

    quit = False

    while not quit:
        
        #Render
    
        response = check_input()

        render()
        #Check player input
    
        #Update the status of the world
        update()


    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()