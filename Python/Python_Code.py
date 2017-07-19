import os
import sys

def introFunc():

    inp = raw_input("This program allows you to install the needed SmartPTT build."
              "\n-- WARNING --"
              "\n Before using the program for build installing, make sure that you have the needed build in your local repository."
              "\n In case there is no needed build, copy it using the program downloader and then use the build for further work."
              "\n"
              "\n - To begin to work with SPTT Version 9.1, enter 1"
              "\n - To begin to work with SPTT Version 9.2, enter 2"
              "\n - To open the local repository folder, enter 'RF'"
              " \n Enter your answer here: ")
    return inp.upper()

class initGateway:

    def __init__(self, a):

        self.possibleVariants = ('1', '2', 'E', 'D', 'RF', 'DD', 'M', 'P', 'B')

        self.inputVersion = a

    def operatingVersion(self):

        if self.inputVersion == self.possibleVariants[0]:

            self.versionVariable = "9.1"

        elif self.possibleVariants[1]:

            self.versionVariable = "9.2"

        if self.inputVersion not in self.possibleVariants:

         def tryAgain():
                return "Please try again"
         print(tryAgain())
         return introFunc()

        else:
            return self.versionVariable

        # I should add a method for opening a repo folder
   # if sys.platform == 'win32': # Clear console screen
     #   os.system('cls')
        #else:
           # os.system('clear')

class secondGateway:

    def __init__(self, versionVariable):

        self.versionVariable = versionVariable

    def configSelecting(self):
        return self.versionVariable


        print("---- VERSION Action " #+ self.versionVariable + " Selection Window ----"
	"\n ---- Choose the needed action and enter your answer below ----"
    "\n- To install SmartPTT Enterprise build, enter 'E'."
    "\n- To install SmartPTT Plus build, enter 'P'."
    "\n- To install SmartPTT Basic build, enter 'B'."
    "\n- To install SmartPTT Monitoring build, enter 'M'."
    "\n- To install SmartPTT Radius-IP Enterprise build, enter 'RE'."
    "\n- To install SmartPTT Developer build, enter 'D'."
	"\n- To activate Downloader, enter 'DD'")
        confInp = raw_input("enter your answer here: ")


ig = initGateway(introFunc())
sg = secondGateway(ig.operatingVersion)
print(sg.configSelecting())