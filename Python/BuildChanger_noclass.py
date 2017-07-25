import os
import sys
import subprocess

def introFunc():

    def inputInfo():
        
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

    def operatingVersion(x):

        possibleVariants = ('1', '2', 'E', 'D', 'RF', 'DD', 'M', 'P', 'B')
               
        inputVersion = x

        if inputVersion == possibleVariants[0]:

            versionVariable = "9.1"

        if inputVersion ==  possibleVariants[1]:

            versionVariable = "9.2"

        if inputVersion ==  possibleVariants[4]:

            print(subprocess.Popen('explorer "/usr/home/desktop/"'))

            #screen cleaning is needed here

        if inputVersion not in possibleVariants:

            def tryAgain():

                os.system('clear')
                print "Please try again"
                return introFunc()

            return(tryAgain())
        
    return operatingVersion(inputInfo())

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
print(introFunc())

"""

       


"""