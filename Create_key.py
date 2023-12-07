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
    # Checking if the script is run as an administrator
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    # If the script is not run as an administrator, request elevation of privileges
    if not is_admin():
        # Restarting the script as an administrator
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, extension, 0, winreg.KEY_READ) as ext_key:
            print(Fore.GREEN + f"The key {extension} already exists.")
            print(Fore.GREEN + f"Registry key = {ext_key}")

    except FileNotFoundError:
        try:
            with winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, extension, 0, winreg.KEY_WRITE) as ext_key:
                print(Fore.GREEN + f"The key {extension} has been successfully created.")
            print(Fore.RED + "Restart your computer for the changes to take effect.")

        except Exception as e:
            print(
                Fore.RED + f"WARNING! THE PROGRAM MUST BE RUN AS AN ADMINISTRATOR TO CONFIGURE THE DATA!: {e}")


def change_icon(extension, icon_path=None):
    # Checking if the script is run as an administrator
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    # If the script is not run as an administrator, requesting elevation of privileges
    if not is_admin():
        # Restarting the script as an administrator
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    try:
        create_extension_key(extension)

        # Create the 'WinArch' folder in 'C:\Program Files' if it doesn't exist yet
        os.makedirs('C:\\Program Files\\WinArch\\Icons', exist_ok=True)
        # Copy each file in the 'Icons' folder to the new directory
        for file in os.listdir('Icons'):
            shutil.copy2(os.path.join('Icons', file), 'C:\\Program Files\\WinArch\\Icons')
        # Set the path to the icon
        icon_path = 'C:\\Program Files\\WinArch\\Icons\\WinArchive.ico'

        # Change the registry key value
        print(Fore.GREEN + "Changing the key value")
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, extension, 0, winreg.KEY_WRITE) as ext_key:
            with winreg.CreateKey(ext_key, 'DefaultIcon') as icon_key:
                winreg.SetValueEx(icon_key, '', 0, winreg.REG_SZ, icon_path)
                print(Fore.GREEN + f"The program successfully changed the registry key value '{extension}'")
                print(Fore.RED + "Restart your computer for the changes to take effect")
                print(
                    Fore.YELLOW + "If you are not running the program for the first time or have not deleted the key, you can ignore this message")

    except Exception as e:
        print(Fore.RED + f"Error while changing the registry key: {e}")
        play_sound(sound_error)

# Sounds for pygame
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