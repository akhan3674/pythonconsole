#!/usr/bin/python

def help_function():
    print " help - display list of commands"
    print " exit - quits the console"
    print " quit - same as exit"
    print " dum  - test function" 
def dummy_function():
    print "dummy function was called."

def console():
    stream=None;
    print " "
    print "<Untitled> Console v1.0"
    print "by Abdus Samad Khan"
    print "-------------------"
    while 1:
       stream=raw_input(">>> ")
       if stream=="exit" or stream=="quit":
		break;
       if stream == "help":
           help_function()
       elif stream == "dum":
           dummy_function()
       else:
	   print "",stream,"is unknown command."

console()
