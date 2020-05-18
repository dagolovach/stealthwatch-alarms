#!/usr/bin/env python

from argparse import ArgumentParser
import pprint
import json
import shutil
from colorama import Fore, Back, Style
import sys

def search_pattern(alarms, searchFor):
    """Helper function to search pattern in the Alarm Names.

    Arguments:
        alarms {dict} -- dictionary with all SMC alarms
        searchFor {str} -- search pattern entered by user

    Returns:
        [list] -- List with all matched Alarms if successm None if not found
    """
    alarm_list = []
    for key in alarms.keys():
        if searchFor in key:
            alarm_list.append(alarms[key])
    if alarm_list:
        return alarm_list
    else:
        return None


def print_alarm_info(alarm_definitions=None, alarm=None):
    """Helper function to print results

    Keyword Arguments:
        alarm_definitions {dict} -- Dictionary with all Alarms Definitions (default: {None})
        alarm {str} -- initial requested Alarm (default: {None})
    """
    columns = shutil.get_terminal_size().columns
    if not alarm_definitions:
        print(Fore.RED + f"{alarm}".center(columns, '#'))
        print(Style.RESET_ALL)
        print(f"Not Found")
        return
    for alarm_definition in alarm_definitions:
        print(Fore.RED + f"{alarm_definition['name']}".center(columns, '#'))
        print(Style.RESET_ALL)
        print(Fore.GREEN + "======= Mitigation ======".center(columns))
        print(Style.RESET_ALL)
        print(f"{alarm_definition['mitigation']}")
        print(Style.RESET_ALL)
        print(Fore.GREEN + "======= What does it mean when it triggers? ======".center(columns))
        print(Style.RESET_ALL)
        print(f"{alarm_definition['meaning']}")
        print(Style.RESET_ALL)
        print(Fore.GREEN + "======= What are next steps? ======".center(columns))
        print(Style.RESET_ALL)
        print(f"{alarm_definition['steps']}")
        print(Style.RESET_ALL)

def get_alarm_list():
    """Function to get the list of all possible Alarms. Used in "define_alarm.py --list" command
    """
    with open('alarms.json', 'r') as f:
        content = json.loads(f.read())
        for k in content.keys():
            print(k.replace(' ', '-'))

# Main Function 
def get_alarm_info(alarm=None):
    """Main function to get Alarm Information based on the user input

    Keyword Arguments:
        alarm {str} -- requested Alarm (default: {None})

    Returns:
        [list] -- List with all Alarms found
    """
    requested_list = []
    with open('alarms.json', 'r') as f:
        content = json.loads(f.read())
        requested = content.get(alarm, None)
        if not requested:
            requested_list = search_pattern(content, alarm.lower())
        else:
            requested_list.append(requested)
    return requested_list


def define_alarm(user_input):
    """Main Function to check user input. Possible options:
        - python define_alarm.py udp
        - python define_alarm.py udp-flood
        - python define_alarm.py 'UDP Flodd"

    Arguments:
        user_input {str} -- alarm name or some search
    """
    if user_input == '--list':
        get_alarm_list()
        return
    if '-' in user_input:
        alarm = user_input.replace('-', ' ')
    else:
        alarm = user_input
    alarm_definitions = get_alarm_info(alarm)
    print_alarm_info(alarm_definitions, alarm)


# Run main function
if __name__ == "__main__":
    if len(sys.argv) == 2:
        define_alarm(sys.argv[1])
    else:
        raise SyntaxError("Insufficient arguments.")
