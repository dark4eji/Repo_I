import fnmatch
import os

wrong_answer = 'Некорректный ответ, попробуйте снова'

enter_answer = 'Введите ваш ответ здесь: '

path = os.listdir(r'D:\Python task')

config_path_list = []

finalchoice = []

def check_and_find(ler):
    for files in path:

        if fnmatch.fnmatch(files, ler):

            config_path = os.path.join('D:\\', 'Python task', files)
            print(config_path)
            config_path_list.append(config_path)

    for dirs in config_path_list:

        last_edited_config = max(config_path_list, key=os.path.getctime)

        if os.path.exists(last_edited_config) is False:
            return 'Нету файлов вообще епта'
            # config_selecting_screen(general_intro_func())

        return os.path.exists(last_edited_config)

check_and_find('asd')

print(config_path_list)