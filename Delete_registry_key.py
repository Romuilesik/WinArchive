import winreg
import sys
import ctypes
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
import requests
from packaging.version import parse
import colorama
from colorama import Fore

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

colorama.init(autoreset=True)

pygame.init()

pygame.mixer.init()

program_version = "1.8"

# Проверяем, запущен ли скрипт от имени администратора
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Если скрипт не запущен от имени администратора, запрашиваем повышение привилегий
if not is_admin():
    # Повторный запуск скрипта от имени администратора
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Получаем путь к исполняемому файлу
executable_directory = os.path.dirname(sys.executable)

# Звуки для пайгейм
sound_file_error = os.path.join(script_directory, 'Sounds', 'Error.mp3')
sound_file_success = os.path.join(script_directory, 'Sounds', 'Success.mp3')
sound_file_goodbye = os.path.join(script_directory, 'Sounds', 'Goodbye.mp3')
sound_file_hello = os.path.join(script_directory, 'Sounds', 'Hello.mp3')
sound_file_test = os.path.join(script_directory, 'Sounds', 'Test.mp3')
sound_file_warning = os.path.join(script_directory, 'Sounds', 'Warning.mp3')

sound_error = pygame.mixer.Sound(sound_file_error)
sound_success = pygame.mixer.Sound(sound_file_success)
sound_hello = pygame.mixer.Sound(sound_file_hello)
sound_goodbye = pygame.mixer.Sound(sound_file_goodbye)
sound_test = pygame.mixer.Sound(sound_file_test)
sound_warning = pygame.mixer.Sound(sound_file_warning)

sound_error.set_volume(0.3)
sound_success.set_volume(0.3)
sound_hello.set_volume(0.3)
sound_goodbye.set_volume(0.3)
sound_test.set_volume(0.3)
sound_warning.set_volume(0.3)

def play_sound(sound):
    if not pygame.mixer.get_busy():
        sound.play()


play_sound(sound_hello)
# Reading language from Language_key.txt
try:
    with open("Language_key.txt", "r") as file:
        selected_language = file.read().strip()
        print(Fore.GREEN + f"Last selected language: {selected_language}")
        play_sound(sound_warning)
except FileNotFoundError:
    print(Fore.RED + "No language file found.")
    play_sound(sound_error)

    # Setting language based on user choice
    language = input("""Choose language!
1 - English - English
2 - Russian - Русский
3 - Ukrainian - Українська
: """)

    languages = {
        "1": "English",
        "2": "Russian",
        "3": "Ukrainian"
    }

    selected_language = languages.get(language)
    if selected_language:
        with open("Language_key.txt", "w") as file:
            file.write(selected_language)
            print(Fore.GREEN + f"Selected language '{selected_language}' has been written to Language_key.txt")
    else:
        print("Invalid choice of language")
        play_sound(sound_error)


# Логика на основе выбранного языка
if selected_language == "Russian":
    def check_version(current_version):
        url = "mine url)))))"
        response = requests.get(url)
        online_version = response.text.strip()

        if parse(online_version) > parse(current_version):
            print(Fore.YELLOW + f"Доступно обновление {online_version}! Для получения инструкций по установке обновления, пожалуйста, скачайте установщик с https://github.com/Romuilesik/WinArchiveInstaller или с https://sites.google.com/view/romuilesik-winarchive/main/download?authuser=0, перейдите в раздел “О программе” и выберите “Проверить наличие обновлений")
            play_sound(sound_warning)
        elif parse(online_version) < parse(current_version):
            print(Fore.YELLOW + "Вы участвуете в бета-тестировании программы!")
            play_sound(sound_warning)
        else:
            print(Fore.GREEN + "У вас последняя версия программы!")
            play_sound(sound_success)

    check_version(program_version)

    time.sleep(1)

    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(Fore.GREEN + "Добро пожаловать в Delete_registry_key! Эта программа была создана пользователем под ником RoмкаР.")
    print("")
    print(Fore.RED + f"ПРЕДУПРЕЖДЕНИЕ! ПРОГРАММА ДОЛЖНА БЫТЬ ЗАПУЩЕНА ОТ ИМЕНИ АДМИНИСТАРТОРА ДЛЯ УДАЛЕНИЯ КЛЮЧА РАСШИРЕНИЯ ФАЙЛА!")
    print("")
    while True:
        option = input("""Выберете опцию!
1 - Удалить ключ .wnz
2 - Удалить ключ .wnzt
3- Изменить язык
0 - Выход
: """)
        if option == "1":

            play_sound(sound_warning)
            print(Fore.RED + "Удалить ключ?")
            print("")
            delete = input("""1 - Да
2 - Нет
: """)

            if delete == "1":

                play_sound(sound_warning)
                confirm = input(Fore.YELLOW + """Вы уверены что хотите удалить ключ?
1 - Да
2 - Нет
: """)
                if confirm == "1":
                    def delete_default_icon(extension):
                        try:
                            parent_key = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
                            key_to_delete = winreg.OpenKey(parent_key, extension, 0, winreg.KEY_ALL_ACCESS)

                            winreg.DeleteKey(key_to_delete, 'DefaultIcon')
                            print(Fore.GREEN + f"Подключ 'DefaultIcon' успешно удален из ключа '{extension}' в реестре")

                            winreg.CloseKey(key_to_delete)

                            winreg.DeleteKey(parent_key, extension)
                            print(Fore.GREEN + f"Ключ расширения файла '{extension}' успешно удален из реестра")

                            play_sound(sound_success)
                            exit = input("Введите что угодно что бы ввыйти: ")
                            if exit == "1":
                                print(Fore.GREEN + "До свидания!")
                            else:
                                print(Fore.GREEN + "До свидания!")
                        except Exception as e:
                            print(Fore.RED + f"Ошибка при удалении ключа расширения файла: {e}")

                            play_sound(sound_error)

                            print(Fore.YELLOW + f"""Если у вас не получаеться удалить ключ реестра попробуйте сделать это вручную по этой инстуркции:
Нажмите Win + R, чтобы открыть диалоговое окно “Выполнить”.
Введите regedit и нажмите Enter, чтобы открыть редактор реестра.
В редакторе реестра перейдите к HKEY_CLASSES_ROOT.
Найдите и выберите ключ ‘.wnz’.
Нажмите правую кнопку мыши и выберите ‘Удалить’.
Подтвердите удаление ключа.
Пожалуйста, будьте осторожны при работе с реестром, так как неправильное использование может повредить вашу систему.""")
                            exit = input("Введите что угодно что бы ввыйти: ")
                            if exit == "1":
                                print(Fore.GREEN + "До свидания!")
                            else:
                                print(Fore.GREEN + "До свидания!")

                    delete_default_icon('.wnz')
                    play_sound(sound_goodbye)
                    time.sleep(2.3)
                    exit()

                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До свидания!")
                    time.sleep(2.3)

            else:
                if delete == "":
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До свидания!")
                    time.sleep(2.3)
                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До свидания!")
                    time.sleep(2.3)

        elif option == "2":

            play_sound(sound_warning)
            print(Fore.RED + "Удалить ключ?")
            print("")
            delete = input("""1 - Да
2 - Нет
: """)

            if delete == "1":

                play_sound(sound_warning)
                confirm = input(Fore.YELLOW + """Вы уверены что хотите удалить ключ?
1 - Да
2 - Нет
: """)
                if confirm == "1":
                    def delete_default_icon(extension):
                        try:
                            parent_key = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
                            key_to_delete = winreg.OpenKey(parent_key, extension, 0, winreg.KEY_ALL_ACCESS)

                            winreg.DeleteKey(key_to_delete, 'DefaultIcon')
                            print(
                                Fore.GREEN + f"Подключ 'DefaultIcon' успешно удален из ключа '{extension}' в реестре")

                            winreg.CloseKey(key_to_delete)

                            winreg.DeleteKey(parent_key, extension)
                            print(Fore.GREEN + f"Ключ расширения файла '{extension}' успешно удален из реестра")

                            play_sound(sound_success)
                            exit = input("Введите что угодно что бы ввыйти: ")
                            if exit == "1":
                                print(Fore.GREEN + "До свидания!")
                            else:
                                print(Fore.GREEN + "До свидания!")
                        except Exception as e:
                            print(Fore.RED + f"Ошибка при удалении ключа расширения файла: {e}")

                            play_sound(sound_error)

                            print(Fore.YELLOW + f"""Если у вас не получаеться удалить ключ реестра попробуйте сделать это вручную по этой инстуркции:
Нажмите Win + R, чтобы открыть диалоговое окно “Выполнить”.
Введите regedit и нажмите Enter, чтобы открыть редактор реестра.
В редакторе реестра перейдите к HKEY_CLASSES_ROOT.
Найдите и выберите ключ ‘.wnzt’.
Нажмите правую кнопку мыши и выберите ‘Удалить’.
Подтвердите удаление ключа.
Пожалуйста, будьте осторожны при работе с реестром, так как неправильное использование может повредить вашу систему.""")
                            exit = input("Введите что угодно что бы ввыйти: ")
                            if exit == "1":
                                print(Fore.GREEN + "До свидания!")
                            else:
                                print(Fore.GREEN + "До свидания!")


                    delete_default_icon('.wnzt')
                    play_sound(sound_goodbye)
                    time.sleep(2.3)
                    exit()

                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До свидания!")
                    time.sleep(2.3)

            else:
                if delete == "":
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До свидания!")
                    time.sleep(2.3)
                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До свидания!")
                    time.sleep(2.3)

        elif option == "3":
            # Установка языка на основе выбора пользователя
            while True:
                language = input("""Выберите язык!
1 - English
2 - Русский
3 - Украинский
0 - выход
: """)

                languages = {
                    "1": "English",
                    "2": "Russian",
                    "3": "Ukrainian"
                }

                if language in languages:
                    selected_language = languages.get(language)
                    with open("Language_key.txt", "w") as file:
                        file.write(selected_language)
                        print(
                            Fore.GREEN + f"Выбранный язык '{selected_language}' был записан в Language_key.txt")
                        play_sound(sound_success)
                        print(
                            Fore.RED + "Чтобы применить новые настройки языка, пожалуйста, перезапустите программу.")
                        time.sleep(2)
                        sys.exit()  # Закрыть программу

                elif language == "0":
                    print(Fore.GREEN + "Возвращение в главное меню")
                    break

                else:
                    print(Fore.RED + "Неверный выбор языка")
                    play_sound(sound_error)

        elif option == "0":
                play_sound(sound_goodbye)
                print(Fore.GREEN + "До свидания!")
                time.sleep(2.3)
                break

        else:
            print(Fore.RED + "Неверный выбор!")
            play_sound(sound_error)

# Logic based on the selected language
if selected_language == "English":

    def check_version(current_version):
        url = "mine url)))))"
        response = requests.get(url)
        online_version = response.text.strip()

        if parse(online_version) > parse(current_version):
            print(
                Fore.YELLOW + f"An update is available {online_version}! To get instructions on how to install the update, please download the installer from https://github.com/Romuilesik/WinArchiveInstaller or from https://sites.google.com/view/romuilesik-winarchive/main/download?authuser=0, go to the 'About' section, and select 'Check for Updates'.")
            play_sound(sound_warning)
        elif parse(online_version) < parse(current_version):
            print(Fore.YELLOW + "You are participating in the program's beta testing!")
            play_sound(sound_warning)
        else:
            print(Fore.GREEN + "You have the latest version of the program!")
            play_sound(sound_success)


    check_version(program_version)

    time.sleep(1)

    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(Fore.GREEN + "Welcome to Delete_registry_key! This program was created by the user under the nickname RoмкаР.")
    print("")
    print(Fore.RED + f"WARNING! THE PROGRAM MUST BE RUN AS ADMINISTRATOR TO DELETE THE FILE EXTENSION KEY!")
    print("")
    while True:
        option = input("""Choose an option!
1 - Delete key .wnz
2 - Delete key .wnzt
3 - Change language
0 - Exit
: """)
        if option == "1":

            play_sound(sound_warning)
            print(Fore.RED + "Delete key?")
            print("")
            delete = input("""1 - Yes
2 - No
: """)

            if delete == "1":

                play_sound(sound_warning)
                confirm = input(Fore.YELLOW + """Are you sure you want to delete the key?
1 - Yes
2 - No
: """)
                if confirm == "1":
                    def delete_default_icon(extension):
                        try:
                            parent_key = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
                            key_to_delete = winreg.OpenKey(parent_key, extension, 0, winreg.KEY_ALL_ACCESS)

                            winreg.DeleteKey(key_to_delete, 'DefaultIcon')
                            print(
                                Fore.GREEN + f"Subkey 'DefaultIcon' successfully deleted from key '{extension}' in the registry")

                            winreg.CloseKey(key_to_delete)

                            winreg.DeleteKey(parent_key, extension)
                            print(
                                Fore.GREEN + f"File extension key '{extension}' successfully deleted from the registry")

                            play_sound(sound_success)
                            exit = input("Enter anything to exit: ")
                            if exit == "1":
                                print(Fore.GREEN + "Goodbye!")
                            else:
                                print(Fore.GREEN + "Goodbye!")
                        except Exception as e:
                            print(Fore.RED + f"Error deleting file extension key: {e}")

                            play_sound(sound_error)

                            print(Fore.YELLOW + f"""If you can't delete the registry key, try doing it manually using this instruction:
Press Win + R to open the “Run” dialog box.
Enter regedit and press Enter to open the registry editor.
In the registry editor, go to HKEY_CLASSES_ROOT.
Find and select the ‘.wnz’ key.
Right-click and select ‘Delete’.
Confirm the deletion of the key.
Please be careful when working with the registry, as improper use can damage your system.""")
                            exit = input("Enter anything to exit: ")
                            if exit == "1":
                                print(Fore.GREEN + "Goodbye!")
                            else:
                                print(Fore.GREEN + "Goodbye!")


                    delete_default_icon('.wnz')
                    play_sound(sound_goodbye)
                    time.sleep(2.3)
                    exit()

                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "Goodbye!")
                    time.sleep(2.3)

            else:
                if delete == "":
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "Goodbye!")
                    time.sleep(2.3)
                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "Goodbye!")
                    time.sleep(2.3)

        elif option == "2":

            play_sound(sound_warning)
            print(Fore.RED + "Delete key?")
            print("")
            delete = input("""1 - Yes
2 - No
: """)

            if delete == "1":

                play_sound(sound_warning)
                confirm = input(Fore.YELLOW + """Are you sure you want to delete the key?
1 - Yes
2 - No
: """)
                if confirm == "1":
                    def delete_default_icon(extension):
                        try:
                            parent_key = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
                            key_to_delete = winreg.OpenKey(parent_key, extension, 0, winreg.KEY_ALL_ACCESS)

                            winreg.DeleteKey(key_to_delete, 'DefaultIcon')
                            print(
                                Fore.GREEN + f"Subkey 'DefaultIcon' successfully deleted from key '{extension}' in the registry")

                            winreg.CloseKey(key_to_delete)

                            winreg.DeleteKey(parent_key, extension)
                            print(
                                Fore.GREEN + f"File extension key '{extension}' successfully deleted from the registry")

                            play_sound(sound_success)
                            exit = input("Enter anything to exit: ")
                            if exit == "1":
                                print(Fore.GREEN + "Goodbye!")
                            else:
                                print(Fore.GREEN + "Goodbye!")
                        except Exception as e:
                            print(Fore.RED + f"Error deleting file extension key: {e}")

                            play_sound(sound_error)

                            print(Fore.YELLOW + f"""If you can't delete the registry key, try doing it manually using this instruction:
Press Win + R to open the “Run” dialog box.
Enter regedit and press Enter to open the registry editor.
In the registry editor, go to HKEY_CLASSES_ROOT.
Find and select the ‘.wnzt’ key.
Right-click and select ‘Delete’.
Confirm the deletion of the key.
Please be careful when working with the registry, as improper use can damage your system.""")
                            exit = input("Enter anything to exit: ")
                            if exit == "1":
                                print(Fore.GREEN + "Goodbye!")
                            else:
                                print(Fore.GREEN + "Goodbye!")


                    delete_default_icon('.wnzt')
                    play_sound(sound_goodbye)
                    time.sleep(2.3)
                    exit()

                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "Goodbye!")
                    time.sleep(2.3)

            else:
                if delete == "":
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "Goodbye!")
                    time.sleep(2.3)
                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "Goodbye!")
                    time.sleep(2.3)

        elif option == "3":
            # Setting the language based on user choice
            while True:
                language = input("""Choose a language!
1 - English
2 - Russian
3 - Ukrainian
0 - exit
: """)

                languages = {
                    "1": "English",
                    "2": "Russian",
                    "3": "Ukrainian"
                }

                if language in languages:
                    selected_language = languages.get(language)
                    with open("Language_key.txt", "w") as file:
                        file.write(selected_language)
                        print(
                            Fore.GREEN + f"Selected language '{selected_language}' has been written to Language_key.txt")
                        play_sound(sound_success)
                        print(
                            Fore.RED + "To apply new language settings, please restart the program.")
                        time.sleep(2)
                        sys.exit()  # Close the program

                elif language == "0":
                    print(Fore.GREEN + "Returning to the main menu")
                    break

                else:
                    print(Fore.RED + "Invalid language choice")
                    play_sound(sound_error)

        elif option == "0":
                play_sound(sound_goodbye)
                print(Fore.GREEN + "Goodbye!")
                time.sleep(2.3)
                break

        else:
            print(Fore.RED + "Invalid choice!")
            play_sound(sound_error)

# Логіка на основі обраної мови
if selected_language == "Ukrainian":

    def check_version(current_version):
        url = "mine url)))))"
        response = requests.get(url)
        online_version = response.text.strip()

        if parse(online_version) > parse(current_version):
            print(
                Fore.YELLOW + f"Доступне оновлення {online_version}! Для отримання інструкцій з встановлення оновлення, будь ласка, завантажте встановлювач з https://github.com/Romuilesik/WinArchiveInstaller або з https://sites.google.com/view/romuilesik-winarchive/main/download?authuser=0, перейдіть до розділу 'Про програму' та виберіть 'Перевірити оновлення'.")
            play_sound(sound_warning)
        elif parse(online_version) < parse(current_version):
            print(Fore.YELLOW + "Ви берете участь у бета-тестуванні програми!")
            play_sound(sound_warning)
        else:
            print(Fore.GREEN + "У вас остання версія програми!")
            play_sound(sound_success)


    check_version(program_version)

    time.sleep(1)

    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(Fore.GREEN + "Ласкаво просимо до Delete_registry_key! Цю програму створив користувач під псевдонімом RoмкаР.")
    print("")
    print(Fore.RED + f"ПОПЕРЕДЖЕННЯ! ПРОГРАМА ПОВИННА БУТИ ЗАПУЩЕНА ВІД ІМЕНІ АДМІНІСТРАТОРА, ЩОБ ВИДАЛИТИ КЛЮЧ РОЗШИРЕННЯ ФАЙЛУ!")
    print("")
    while True:
        option = input("""Оберіть опцію!
1 - Видалити ключ .wnz
2 - Видалити ключ .wnzt
3- Змінити мову
0 - Вихід
: """)
        if option == "1":

            play_sound(sound_warning)
            print(Fore.RED + "Видалити ключ?")
            print("")
            delete = input("""1 - Так
2 - Ні
: """)

            if delete == "1":

                play_sound(sound_warning)
                confirm = input(Fore.YELLOW + """Ви впевнені, що хочете видалити ключ?
1 - Так
2 - Ні
: """)
                if confirm == "1":
                    def delete_default_icon(extension):
                        try:
                            parent_key = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
                            key_to_delete = winreg.OpenKey(parent_key, extension, 0, winreg.KEY_ALL_ACCESS)

                            winreg.DeleteKey(key_to_delete, 'DefaultIcon')
                            print(
                                Fore.GREEN + f"Підключ 'DefaultIcon' успішно видалено з ключа '{extension}' в реєстрі")

                            winreg.CloseKey(key_to_delete)

                            winreg.DeleteKey(parent_key, extension)
                            print(Fore.GREEN + f"Ключ розширення файлу '{extension}' успішно видалено з реєстру")

                            play_sound(sound_success)
                            exit = input("Введіть будь-що, щоб вийти: ")
                            if exit == "1":
                                print(Fore.GREEN + "До побачення!")
                            else:
                                print(Fore.GREEN + "До побачення!")
                        except Exception as e:
                            print(Fore.RED + f"Помилка при видаленні ключа розширення файлу: {e}")

                            play_sound(sound_error)

                            print(Fore.YELLOW + f"""Якщо ви не можете видалити ключ реєстру, спробуйте зробити це вручну за цією інструкцією:
Натисніть Win + R, щоб відкрити діалогове вікно “Виконати”.
Введіть regedit і натисніть Enter, щоб відкрити редактор реєстру.
У редакторі реєстру перейдіть до HKEY_CLASSES_ROOT.
Знайдіть і виберіть ключ ‘.wnz’.
Клацніть правою кнопкою миші і виберіть ‘Видалити’.
Підтвердіть видалення ключа.
Будь ласка, будьте обережні при роботі з реєстром, оскільки неправильне використання може пошкодити вашу систему.""")
                            exit = input("Введіть будь-що, щоб вийти: ")
                            if exit == "1":
                                print(Fore.GREEN + "До побачення!")
                            else:
                                print(Fore.GREEN + "До побачення!")


                    delete_default_icon('.wnz')
                    play_sound(sound_goodbye)
                    time.sleep(2.3)
                    exit()

                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До побачення!")
                    time.sleep(2.3)

            else:
                if delete == "":
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До побачення!")
                    time.sleep(2.3)
                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До побачення!")
                    time.sleep(2.3)

        elif option == "2":

            play_sound(sound_warning)
            print(Fore.RED + "Видалити ключ?")
            print("")
            delete = input("""1 - Так
2 - Ні
: """)

            if delete == "1":

                play_sound(sound_warning)
                confirm = input(Fore.YELLOW + """Ви впевнені, що хочете видалити ключ?
1 - Так
2 - Ні
: """)
                if confirm == "1":
                    def delete_default_icon(extension):
                        try:
                            parent_key = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
                            key_to_delete = winreg.OpenKey(parent_key, extension, 0, winreg.KEY_ALL_ACCESS)

                            winreg.DeleteKey(key_to_delete, 'DefaultIcon')
                            print(
                                Fore.GREEN + f"Підключ 'DefaultIcon' успішно видалено з ключа '{extension}' в реєстрі")

                            winreg.CloseKey(key_to_delete)

                            winreg.DeleteKey(parent_key, extension)
                            print(
                                Fore.GREEN + f"Ключ розширення файлу '{extension}' успішно видалено з реєстру")

                            play_sound(sound_success)
                            exit = input("Введіть будь-що, щоб вийти: ")
                            if exit == "1":
                                print(Fore.GREEN + "До побачення!")
                            else:
                                print(Fore.GREEN + "До побачення!")
                        except Exception as e:
                            print(Fore.RED + f"Помилка при видаленні ключа розширення файлу: {e}")

                            play_sound(sound_error)

                            print(Fore.YELLOW + f"""Якщо ви не можете видалити ключ реєстру, спробуйте зробити це вручну за цією інструкцією:
Натисніть Win + R, щоб відкрити діалогове вікно “Виконати”.
Введіть regedit і натисніть Enter, щоб відкрити редактор реєстру.
У редакторі реєстру перейдіть до HKEY_CLASSES_ROOT.
Знайдіть і виберіть ключ ‘.wnzt’.
Клацніть правою кнопкою миші і виберіть ‘Видалити’.
Підтвердіть видалення ключа.
Будь ласка, будьте обережні при роботі з реєстром, оскільки неправильне використання може пошкодити вашу систему.""")
                            exit = input("Введіть будь-що, щоб вийти: ")
                            if exit == "1":
                                print(Fore.GREEN + "До побачення!")
                            else:
                                print(Fore.GREEN + "До побачення!")


                    delete_default_icon('.wnzt')
                    play_sound(sound_goodbye)
                    time.sleep(2.3)
                    exit()

                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До побачення!")
                    time.sleep(2.3)

            else:
                if delete == "":
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До побачення!")
                    time.sleep(2.3)
                else:
                    play_sound(sound_goodbye)
                    print(Fore.GREEN + "До побачення!")
                    time.sleep(2.3)

        elif option == "3":
            # Встановлення мови на основі вибору користувача
            while True:
                language = input("""Оберіть мову!
1 - English
2 - Російська
3 - Українська
0 - вихід
: """)

                languages = {
                    "1": "English",
                    "2": "Russian",
                    "3": "Ukrainian"
                }

                if language in languages:
                    selected_language = languages.get(language)
                    with open("Language_key.txt", "w") as file:
                        file.write(selected_language)
                        print(
                            Fore.GREEN + f"Обрана мова '{selected_language}' була записана в Language_key.txt")
                        play_sound(sound_success)
                        print(
                            Fore.RED + "Щоб застосувати нові налаштування мови, будь ласка, перезапустіть програму.")
                        time.sleep(2)
                        sys.exit()  # Закрити програму

                elif language == "0":
                    print(Fore.GREEN + "Повернення до головного меню")
                    break

                else:
                    print(Fore.RED + "Неправильний вибір мови")
                    play_sound(sound_error)



        elif option == "0":
            play_sound(sound_goodbye)
            print(Fore.GREEN + "До побачення!")
            time.sleep(2.3)
            break

        else:
            print(Fore.RED + "Неправильний вибір!")
            play_sound(sound_error)

