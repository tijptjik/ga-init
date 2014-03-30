import webbrowser
from utils import *


def createGitHubAccount():
	url = 'https://github.com/join'
	webbrowser.open(url)
	print print_warning('\nThe GitHub signup page just opened in your browser.\
		\n\nPlease complete the process before continuing here.')

def promptExistingAccount():
	msg = 'Do you already have a GitHub account?'
	options = ['(Y)es','(N)o']
	existingAccount = opt_prompt(msg, options)
	return True if existingAccount == 'Y' else False

def promptAccountDetails():
	msg = 'What is your GitHub Username?'
	username = text_prompt(msg)
	msg = 'Please enter your GitHub Password. It will not be stored.'
	password = password_prompt(msg)
	return username, password

# Sign up for account
# Fork the ga-student/XXX_HK_1 repo
# Clone the username/XXX_HK_1 repo to ~/XXX_HK_1
# Create personal directories in /final/NAME/
# Add a README.md with the course details/
# Add everything, commit, push to Github