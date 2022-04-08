from pyAutoUpdate import lib_installer, file_updater

li = lib_installer(['colorama'])
fu = file_updater(['example.py'], ['/LINK/'])

li.install()
from colorama import Fore

if fu.install():
    print(Fore.YELLOW + "Files were updated, reopen app for applying changes")
    exit()

#Your code
print(Fore.GREEN + "Hello world!")
