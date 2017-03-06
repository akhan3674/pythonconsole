import sys

class PyShell:
    def __init__(self):
        # A dictionary mapping valid commands to functions
        self.__commands  = {}
        self.__variables = {}
        self.__PROMPT    = 'pyshell>'
    def __loadCommands(self):
        """ 
        This function intializes commands in a similar way as 
        does unittest module
        Default commands
        - help
        - run script
        - restart
        - exit
        - hist
        - set
        - unset
        """
        for name in dir(module):
            obj = getattr(module,name)
        self.__commands['help'] = self.__func
        self.__commands['exit'] = self.__printHelp
        pass

    def run(self):
        """ 
        This is the main function
        """
        self.__loadCommands()
        self.__setUp()
        try:
            self.__shellLoop()
        finally:
            self.__tearDown()

    def __commandProcessor(self,line):
        pass
        
    def __shellLoop(self):
        """
        This will execute the shell
        """
        RUN_SHELL = True
        while(RUN_SHELL):
            sys.stdout.write(self._PROMPT)
            userIn = sys.stdin.readline()
            RUN_SHELL = self.__commandProcessor(userIn)

    def __setUp(self):
        pass 

    def __tearDown(self):
        pass

    def __command_help(self):
        print "Usage"

    def __command_exit(self):
       pass 
