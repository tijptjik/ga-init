import re
import re
from termcolor import colored
import getpass

def text_prompt(msg):
    try: input = raw_input
    except NameError: pass
    prompt = '\n' + msg + '\n\n > '
    text = input(prompt)
    return text

def password_prompt(msg):
    prompt = '\n' + msg + '\n\n > '
    password = getpass.getpass(prompt)
    return password

def opt_prompt(msg, options):
    try: input = raw_input
    except NameError: pass
    regex = re.compile("\((\S)\)",re.MULTILINE)
    valid_options = regex.findall("".join(options))
    prompt = '\n' + msg + '\n\n' + parse_opts(options) + '\n\n > '
    option = input(prompt)
    while option not in valid_options:
        warning_msg = 'Be sure to type the letter between brackets to select the option of your choice.'
        warning = print_warning(warning_msg)
        option = input('\n' + warning + '\n\n' + prompt)
    return find_substring_index(options, lambda x: '('+ option +')' in x )

def parse_opts(options):
    options = ", ".join(options).split('(')
    options.pop(0) if options[0] == "" else True
    for i, opt in enumerate(options):
        options[i] = '(' + print_opts(opt[0]) + opt[1:]
    return "".join(options)

def find_substring_index(lst, predicate):
     return (i for i, j in enumerate(lst) if predicate(j)).next()
    
print_opts = lambda x: colored(x, 'green', attrs=['bold'])
print_warning = lambda x: colored(x, 'red', attrs=['bold'])