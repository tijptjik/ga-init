#!/usr/bin/env python
# 
# General Assembly Developer Environment Setup Script
# 
# By Mart van de Ven 
# 
# Email: m@type.hk
# Github: @tijptjik


# Requirments

# FEWD


# BEWD

# DS
"""GA Init

Developer Environment Setup for General Assembly.

Please provide a command to run the script. The default command 'install' 
takes three arguments, your course, your location and the iteration of 
thecourse you are part of, e.g.

    ga_init install FEWD HK 5

Usage:
  ga_init install [COURSE LOCATION BATCH] [options]
  ga_init advanced
  ga_init setup APPLICATION...
  ga_init (-h | --help)
  ga_init --version

Options:
  -h --help         Show this screen.
  --version         Show version.
  --advanced        Interactively set advanced settings
  -u=<username>     GitHub Username
  -p=<password>     GitHub Password

"""

import sys

import requests
from fabric.api import local
from docopt import docopt

from applications.OS import *
from utils import *
from git import GitHubWrapper

GA = {}

# Configuration Settings

def setup_os():
    OS = 'OSX'
    if OS == 'OSX':
        pass
    if OS == 'Ubuntu':
        pass
    if OS == 'Fedora':
        pass
    if OS == 'Windows':
        print print_warning('Windows not supported. Please ask your instructor for assistance.')

    return OS

def setup_course():
    courses = ['FEWD','BEWD','DS']
    if args['COURSE'] in courses:
        course = args['COURSE']
    else:
        course = select_course(courses)

    return course
    
def setup_location():
    locations = ['BO', 'HK', 'LDN', 'LA', 'NYC', 'SF', 'SY']
    if args['LOCATION'] in locations:
        location = args['LOCATION']
    else:
        location = select_location(locations)

    return location

def setup_batch():
    if args['BATCH'] and args['BATCH'].isdigit():
        batch = int(args['BATCH'])
    else:
        batch = select_batch()

    return batch

def setup_dependencies(course):
    common_deps = [
        SublimeText,
        Chrome,
        System,
        CLT,
        Git,
        GitHub,
        Package_Manager,
        ZSH]

    if course == 'FEWD':
        deps = common_deps + [NodeJS, Grunt, Yo, Bower]
    elif course == 'BEWD':
        deps = common_deps + [NodeJS, Grunt, Yo, Bower, Ruby, RVM, Rails]
    elif course == 'DS':
        deps = common_deps + [Python, Anaconda]

    return deps

def setup_github():
    GH = GitHubWrapper()
    hasAccount = True if args['-u'] else GH.promptExistingAccount()
    if not hasAccount:
        GH.newAccount()
    accountDetails = [args['-u'], args['-p']] \
        if args['-u'] and args['-p'] \
        else GH.promptAccountDetails(args['-u'])
    username, password = accountDetails[0], accountDetails[1]
    GA['REPO'] = GH.studentRepo(GA['COURSE'], GA['LOCATION'], GA['BATCH']);
    GitHubClient = GH.auth(username, password, GA['REPO'])
    oct_repo = GitHubClient.repos.get()
    print oct_repo
    # gastudents = GitHubClient.repos.get(user='ga-students')
    # print gastudents.repos.list()

def advanced_setup(deps):
    pass

def setup_application():
    pass

def select_course(courses):
    msg = 'Please select your course from the follow options:'
    options = ['(F)EWD','(B)EWD','(D)S']
    course = courses[opt_prompt(msg, options)]
    return course

def select_location(locations):
    msg = 'Please select the city where your course is being held:'
    options = ['(B)OSTON', '(H)ONG KONG', '(L)ONDON', 'LOS (A)NGELES', '(N)EW YORK CITY', '(S)AN FRANCISCO', 'S(Y)DNEY', '(W)ASHINGTON D.C.']
    location = locations[opt_prompt(msg, options)]
    return location

def select_batch():
    try: input = raw_input
    except NameError: pass
    prompt = 'Which iteration of the course are you joining? Ask the instructor if unclear!' + '\n\n > '
    option = input(prompt)
    while not option.isdigit():
        warning_msg = 'Please input a number. Ask your instructor for directions if this isn\'t clear'
        warning = print_warning(warning_msg)
        option = input('\n' + warning + '\n\n' + prompt)
    return int(option)

# Helpers

def start_sshd():
    local('sudo systemsetup -setremotelogin on')

# Initialise 

def main():
    GA['OS'] = setup_os()
    GA['COURSE'] = setup_course()
    GA['LOCATION'] = setup_location()
    GA['BATCH'] = setup_batch()
    GA['DEPENDENCIES'] = setup_dependencies(GA['COURSE'])
    
    if args['advanced']:
        GA['DEPENDENCIES'] = advanced_setup(GA['DEPENDENCIES'])
    [install() for install in GA['DEPENDENCIES']]
    
    GA['GITHUB'] = setup_github()

if __name__ == "__main__":
    args = docopt(__doc__, argv=None, help=False, version=None, options_first=False)
    print args
    if args['install']:
        main()
    elif args['advanced']:
        advanced_setup([])
    elif args['setup']:
        setup_application()
    else:
        print __doc__