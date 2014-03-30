OS = 'OSX'

if OS == 'OSX':
    from OSX import (SublimeText, Chrome, System, CLT, Git, GitHub, 
        Package_Manager, ZSH, NodeJS, Grunt, Yo, Bower, Ruby, RVM, 
        Rails, Python, Anaconda)
if OS == 'Ubuntu':
    from Ubuntu import (SublimeText, Chrome, System, CLT, Git, GitHub, 
        Package_Manager, ZSH, NodeJS, Grunt, Yo, Bower, Ruby, RVM, 
        Rails, Python, Anaconda)
if OS == 'Fedora':
    from Fedora import (SublimeText, Chrome, System, CLT, Git, GitHub, 
        Package_Manager, ZSH, NodeJS, Grunt, Yo, Bower, Ruby, RVM, 
        Rails, Python, Anaconda)
if OS == 'Windows':
    pass

