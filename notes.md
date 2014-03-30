sudo apt-get install ssh to make sure you have it installed (even if you think you do). Then do sudo service ssh start|stop|restart

I propose to write a setup script which would prepare student's Macbooks for any of the technical classes GA is offering. A lot of time and momentum is wasted in the first class trying to get everyone setup. About half the students run into 'inexplicable' errors or have trouble following along with the install instructions (regardless of whether it's written down / presented by the instructor). The instructor also often can't exactly demo the procedures since they are already setup. So, instead of each of GA's students worldwide spending at least an hour to setup, why not have a script which configures the machine for a particular class?  

The script would be written in python which
* Is customisable for City, Course and Batch.
* Suit all technical courses. as it knows the requirements for FEWD and DS (which I know) and BEWD and WDI (which I can get the requirements for.
* Would be built for OSX, I can build in support for Ubuntu / Fedora if there's interest, but someone would have to tweak the script for Windows. It should be straight-forwarded, except I haven't used windows since the 90s. 
* It will - depending on the course -check for or install SublimeText 3, Chrome, OSX Mavericks, XCode, Command Line Tools, Git Binary, Github GUI, Homebrew, ZSH, NodeJS, Grunt, Yo, Bower, Ruby, RVM, Rails, Python Anaconda. Anything I missed can be added.
* It will prompt the student for their github credentials, if they don't have one, it will create an account for them.
* Create or use their SSH Keys.
* Sync SSH keys with GitHub.
* Fork the Student Repo from ga-students.
* Clone the Student Repo.
* Create a sane Git config file

For the Instructor, after all the students have run the script, it will have a function to locally checkout all the student forks on local branches so it's easy for them to review code and suggest fixes. 


Options:

Course : (F)EWD, (B)EWD, (D)S
Geography : 

(B)OSTON, (H)ONG KONG, (L)ONDON, LOS (A)NGELES, (N)EW YORK CITY, (S)AN FRANCISCO, S(Y)DNEY, (W)ASHINGTON D.C.

BO
HK
LDN
LA
NYC
SF
SY

Batch : 1 ... 100

SublimeText 3, Chrome, OSX Mavericks, XCode, Command Line Tools, Git Binary, Github GUI, Homebrew, ZSH, NodeJS, Grunt, Yo, Bower, Ruby, RVM, Rails, Python Anaconda

SublimeText3
Chrome
OSX
XCode
XCode_CLT
Git
GitHub
Homebrew
ZSH
NodeJS
Grunt
Yo
Bower
Ruby
RVM
Rails
Python
Anaconda
GitHub

* It will prompt the student for their github credentials, if they don't have one, it will create an account for them.

