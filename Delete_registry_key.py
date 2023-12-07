import winreg
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
import colorama
from colorama import Fore

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

colorama.init(autoreset=True)

pygame.init()
pygame.mixer.init()

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

sound_error.set_volume(0.2)
sound_success.set_volume(0.2)
sound_hello.set_volume(0.2)
sound_goodbye.set_volume(0.2)
sound_test.set_volume(0.2)
sound_warning.set_volume(0.2)

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

time.sleep(1.4)

# Логика на основе выбранного языка
if selected_language == "Russian":
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(Fore.RED + f"ПРЕДУПРЕЖДЕНИЕ! ПРОГРАММА ДОЛЖНА БЫТЬ ЗАПУЩЕНА ОТ ИМЕНИ АДМИНИСТАРТОРА ДЛЯ УДАЛЕНИЯ КЛЮЧА РАСШИРЕНИЯ ФАЙЛА!")
    print("")
    while True:
        option = input("""Выберете опцию!
1 - удалить ключ
2- изменить язык
0 - выход
: """)
        if option == "1":

            play_sound(sound_warning)
            print(Fore.RED + "Удалить ключ?")
            print("")
            delete = input("""1 - да
2 - нет
: """)

            if delete == "1":

                play_sound(sound_warning)
                confirm = input(Fore.YELLOW + """Вы уверены что хотите удалить ключ?
1 - да
2 - нет
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
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(Fore.RED + f"WARNING! THE PROGRAM MUST BE RUN AS ADMINISTRATOR TO DELETE THE FILE EXTENSION KEY!")
    print("")
    while True:
        option = input("""Choose an option!
1 - delete key
2- change language
0 - exit
: """)
        if option == "1":

            play_sound(sound_warning)
            print(Fore.RED + "Delete key?")
            print("")
            delete = input("""1 - yes
2 - no
: """)

            if delete == "1":

                play_sound(sound_warning)
                confirm = input(Fore.YELLOW + """Are you sure you want to delete the key?
1 - yes
2 - no
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
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(
        Fore.RED + f"ПОПЕРЕДЖЕННЯ! ПРОГРАМА ПОВИННА БУТИ ЗАПУЩЕНА ВІД ІМЕНІ АДМІНІСТРАТОРА, ЩОБ ВИДАЛИТИ КЛЮЧ РОЗШИРЕННЯ ФАЙЛУ!")
    print("")
    while True:
        option = input("""Оберіть опцію!
1 - видалити ключ
2- змінити мову
0 - вихід
: """)
        if option == "1":

            play_sound(sound_warning)
            print(Fore.RED + "Видалити ключ?")
            print("")
            delete = input("""1 - так
2 - ні
: """)

            if delete == "1":

                play_sound(sound_warning)
                confirm = input(Fore.YELLOW + """Ви впевнені, що хочете видалити ключ?
1 - так
2 - ні
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

