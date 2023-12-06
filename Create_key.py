import shutil
import winreg
import sys
import ctypes
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import colorama
from colorama import Fore

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

colorama.init(autoreset=True)

# Инициализация Pygame
pygame.init()

# Настройка аудио
pygame.mixer.init()

# Получаем путь к исполняемому файлу
executable_directory = os.path.dirname(sys.executable)

colorama.init(autoreset=True)

# Инициализация Pygame
pygame.init()

# Настройка аудио
pygame.mixer.init()

def get_script_path():
    return os.path.dirname(os.path.abspath(__file__))

def create_extension_key(extension):

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

    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, extension, 0, winreg.KEY_READ) as ext_key:
            print(Fore.GREEN + f"Ключ {extension} уже существует.")
            print(Fore.GREEN + f"Ключ реестра = {ext_key}")

    except FileNotFoundError:
        try:
            with winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, extension, 0, winreg.KEY_WRITE) as ext_key:
                print(Fore.GREEN + f"Ключ {extension} успешно создан.")
            print(Fore.RED + "Чтобы изменения вступили в силу, перезапустите Компьютер")

        except Exception as e:
            print(Fore.RED + f"ПРЕДУПРЕЖДЕНИЕ! ПРОГРАММА ДОЛЖНА БЫТЬ ЗАПУЩЕНА ОТ ИМЕНИ АДМИНИСТРАТОРА ДЛЯ НАСТРОЙКИ ДАННЫХ!: {e}")


def change_icon(extension, icon_path=None):
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

    try:
        create_extension_key(extension)

        # Создаем папку 'WinArch' в 'C:\Program Files', если она еще не существует
        os.makedirs('C:\\Program Files\\WinArch\\Icons', exist_ok=True)
        # Копируем каждый файл в папке 'Icons' в новую папку
        for file in os.listdir('Icons'):
            shutil.copy2(os.path.join('Icons', file), 'C:\\Program Files\\WinArch\\Icons')
        # Устанавливаем путь к иконке
        icon_path = 'C:\\Program Files\\WinArch\\Icons\\WinArchive.ico'

        # Изменяем значение ключа
        print(Fore.GREEN + "Изменяем значение ключа")
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, extension, 0, winreg.KEY_WRITE) as ext_key:
            with winreg.CreateKey(ext_key, 'DefaultIcon') as icon_key:
                winreg.SetValueEx(icon_key, '', 0, winreg.REG_SZ, icon_path)
                print(Fore.GREEN + f"Программа успешно изменила значение ключа в реестре '{extension}'")
                print(Fore.RED + "Чтобы изменения вступили в силу, перезапустите Компьютер")
                print(Fore.YELLOW + "Если вы не запускаете программу впервые или не удаляли ключ то можете проигорировать данное сообщение")

    except Exception as e:
        print(Fore.RED + f"Ошибка при изменении ключа реестра: {e}")
        play_sound(sound_error)

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