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

print(
    Fore.RED + f"ПРЕДУПРЕЖДЕНИЕ! ПРОГРАММА ДОЛЖНА БЫТЬ ЗАПУЩЕНА ОТ ИМЕНИ АДМИНИСТАРТОРА ДЛЯ УДАЛЕНИЯ КЛЮЧА РАСШИРЕНИЯ ФАЙЛА!")
print("")
print(Fore.RED + "Удалить ключ?")
print("")
play_sound(sound_hello)
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
