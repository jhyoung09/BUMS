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
import logzero, os, filecmp
from logzero import logger, logfile



#   global variables


def ask():
    logger.debug('### STARTING ASK ###')
    
    #   the REPORT
    logger.debug('# STARTING REPORT #')
    print('What kind of report would you like?')
    reportAsk = input("Enter 1 for .TXT and 2 to print to the screen:\n")
    reportChoice = int(reportAsk)
    report = str()

    if reportChoice == 1:
        print('You chose a TEXT report')
        report = str('TEXT')
    elif reportChoice == 2:
        print('you chose to print the report to the screen')
        report = str('SCREEN')
    else:
        print('You did not select a proper choice. Terminating')
        report = str('REPORT ERROR')

    logger.info(report)

    #   the DIRECTORIES
    logger.debug('# STARTING DIRECTORIES #')
    print('What directories would you like to scan?')    
    dir1Ask = input('Enter Directory 1:')
    dir1 = str(dir1Ask)
    logger.info(dir1)
    dir2Ask = input('Enter Directory 2:')
    dir2 = str(dir2Ask)
    print('You chose\n {} as Directory 1\n and\n {} as Directory 2'.format(dir1, dir2))
    logger.info(dir2)

    #   the ACTION
    logger.debug('# STARTING ACTION #')
    print('What action would you like to perform?')
    actionAsk = input('Enter 1 for PUSH, 2 for PULL, and 3 for BOTH:')
    actionChoice = int(actionAsk)
    action = str()

    if actionChoice == 1:
        print('You chose to PUSH data.')
        action = str('PUSH')
    elif actionChoice == 2:
        print('You chose to PULL data.')
        action = str('PULL')
    elif actionChoice == 3:
        print('You chose to PUSH & PULL data.')
        action = str('BOTH')
    else:
        print('You did not select a proper choice. Terminating.')
        action = str('ACTION ERROR')
    logger.info(action)
    
    return report, dir1, dir2,  action

def reporting(report, dir1, dir2, action):
    logger.debug('### STARTING REPORTING ###')

    #   set log information
    logger.debug('# SETTING LOGGING INFO #')

    if 'TEXT' in report:
        logzero.loglevel(20)
        logzero.logfile('./logs/BUMS_REPORT.txt') #    need to add the date time function and pull that in here
        logger.info('User selected {} for their report.'.format(report))
        logger.info('User selected {} as dir1 and {} as dir2'.format(dir1,dir2))
        logger.info('User selected to {} between the folders'.format(action))
    else:
        logger.debug('User choose not to use a report.')

def date():
    date = datetime.datetime.now()
    return date.strftime('%d %m %Y')

def dir_compare(dir1, dir2, prefix1='.', prefix2='.'):
    logger.debug('### STARTING DIR_COMPARE ###')

    comparison = filecmp.dircmp(dir1, dir2)

    data = {
        "left": ["{}{}{}".format(prefix1, os.sep, i) for i in comparison.left_only],
        "right": ["{}{}{}".format(prefix2, os.sep, i) for i in comparison.right_only],
        "both": ["{}{}{}***{}{}{}".format(prefix1, os.sep, i, prefix2, os.sep, i) for i in comparison.common_files],
    }

    for datalist in data.values():
        datalist.sort()

    if comparison.common_dirs:
        for folder in comparison.common_dirs:
            # Update prefix to include new sub_folder
            prefix1 = os.path.normpath(os.path.join(folder1, folder))
            prefix2 = os.path.normpath(os.path.join(folder2, folder))
            # Compare common folder and add results to the report
            sub_folder1 = os.path.join(folder1, folder)
            sub_folder2 = os.path.join(folder2, folder)
            sub_report = _recursive_dircmp(sub_folder1, sub_folder2, prefix1, prefix2)

            for key, value in sub_report.items():
                data[key] += value

    return data

    print(data)
    





def main():
    logzero.loglevel(10)
    logzero.logfile('./logs/BUMS_LOG.txt')
    logger.debug('### STARTING MAIN ###')

    logger.debug('# SETTING report, dir1, dir2, action VARIABLES #')
    report, dir1, dir2, action = ask()

    dir_compare(dir1, dir2)

    #logger.debug('# SETTING data VARIABLE #')
    #data = dir_compare()

    reporting(report, dir1, dir2, action)

    logger.debug('### ENDING MAIN ###')


main()