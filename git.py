import webbrowser
from utils import *
from pygithub3 import Github

class GitHubWrapper(object):
	"""docstring for GitHub"""
	def __init__(self, username=None, password=None):
		super(GitHubWrapper, self).__init__()
		self.username = username
		self.password = password
		
	def newAccount(self):
		url = 'https://github.com/join'
		webbrowser.open(url)
		print print_warning('\nThe GitHub signup page just opened in your browser.\
			\n\nPlease complete the process before continuing here.')

	def promptExistingAccount(self):
		msg = 'Do you already have a GitHub account?'
		options = ['(N)o','(Y)es']
		existingAccount = opt_prompt(msg, options)
		return True if existingAccount else False

	def promptAccountDetails(self, username=None):
		if not username:
			msg = 'What is your GitHub Username?'
			username = text_prompt(msg)
		userhint = print_warning(username.capitalize())
		msg = 'Welcome ' + userhint + ', please enter your GitHub Password. It will not be stored.'
		password = password_prompt(msg)
		return [username, password]

	def auth(self, username, password, repo=None):
		GitHubClient = Github(login=username, user=username, password=password, repo=repo)
		return GitHubClient

	def studentRepo(self, course, location, batch):
		return "%s_%s_%s" % (course, location, batch)


# Sign up for account
# Fork the ga-student/XXX_HK_1 repo
# Clone the username/XXX_HK_1 repo to ~/XXX_HK_1
# Create personal directories in /final/NAME/
# Add a README.md with the course details/
# Add everything, commit, push to Github