# -*- coding: utf-8 -*-

class Hello:    # variable length arguments!!!
    def __init__(self, *args, **kwargs): pass
        self.name = name
        self.age = 10 #default or static value
        
hello = Hello()
hello = Hello('name', 'eh', 'ff', name = 'sjjds')
