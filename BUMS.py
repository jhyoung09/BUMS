##################################################
#
#   James Hunter Young
#   2020
#
#   BUMS - Back Up My Shtuff
#
#
#
##################################################

#   imports

#   global variables
report = int()
dir1 = int()
dir2 = int()
action = int()


def ask(report, dir1, dir2, action):
    print('### STARTING ASK ###')
    
    #   the REPORT
    print('What kind of report would you like?')
    reportAsk = input("Enter 1 for .TXT and 2 to print to the screen:\n")
    report = int(reportAsk)

    if report == 1:
        print('You chose a TEXT report')
    elif report == 2:
        print('you chose to print the report to the screen')
    else:
        print('You did not select a proper choice. Terminating')

    #   the DIRECTORIES
    print('What directories would you like to scan?')    
    dir1Ask = input('Enter Directory 1:')
    dir1 = str(dir1Ask)
    dir2Ask = input('Enter Directory 2:')
    dir2 = str(dir2Ask)
    print('You chose\n {} as Directory 1\n and\n {} as Directory 2'.format(dir1, dir2))

    #   the ASK
    print('What action would you like to perform?')
    actionAsk = input('Enter 1 for PUSH, 2 for PULL, and 3 for BOTH:')
    action = int(actionAsk)

    if action == 1:
        print('You chose to PUSH data.')
    elif action == 2:
        print('You chose to PULL data.')
    elif action == 3:
        print('You chose to PUSH & PULL data.')
    else:
        print('You did not select a proper choice. Terminating.')
    
    return report
    return dir1
    return dir2
    return action



def main():
    print('### STARTING MAIN ###')
    ask(report, dir1, dir2, action)
    print('### BACK IN MAIN ###')


main()