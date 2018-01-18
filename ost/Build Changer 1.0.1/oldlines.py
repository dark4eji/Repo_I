import os
import datetime

year = datetime.date.today().year

sysdrive = os.environ['systemdrive']

programFilesPath = sysdrive+'\ProgramData\Builds_SmartPTT'

source = '\\orpo-tfs-buildbot.elcom.local\Artifact share\Binaries (NOT ENCRYPTED, FAST BUILD)'
target = 'C:\Program Files (x86)\SmartPTT'
wrongAnswer = 'Wrong answer. Please try again'
buildPath = "D:\Repo_I"

def intro():
    #os.system('cls')
    print('''
Before using the program for build installing, make sure that you have the needed build in your local repository.

In case there is no needed build, copy it using the program downloader and then use the build for further work.

- To begin to work with SPTT Version 9.1, enter 1

- To begin to work with SPTT Version 9.2, enter 2

- To open the local repository folder, enter "RF"
''')

    sptt_config_version = input('Enter your answer here: ')

    return sptt_config_version

intro = intro()

def start(x):
    spttVerList = {'1', '2', 'RF', 'rf'}

    while True:

        if x == '1':
            return(float(9.1))
            break
        elif x == '2':
            return(float(9.2))
            break

        if x in spttVerList:
            if x == 'RF' or 'rf':
                print(os.startfile('D:\Python develop'))
                return start(spttConfig.intro())

        if x not in spttVerList:
            print(wrongAnswer)
            return start(spttConfig.intro())


checkType = start(spttConfig.intro())

buildTypeOutput = buildType.buildTypeLetter(checkType)

def selectingBuildType(x):
    configList = {'e', 'p', 'DD', 'dd'}

    while True:

        if x == 'e':
            return('enterprise_' + str(year))
            break
        elif x == 'p':
            return('PLUS_' + str(year))
            break
        elif x == 'DD' or 'dd':
            if x in configList:
                return float(1.0)
        elif x not in configList:
            print(wrongAnswer)
            return selectingBuildType(buildTypeOutput)

selectedBuild = type(selectingBuildType(buildTypeOutput))

