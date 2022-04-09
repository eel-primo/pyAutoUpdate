from pyAutoUpdate import lib_installer, file_updater

li = lib_installer(['colorama'])
fu = file_updater(['example.py'], ['https://raw.githubusercontent.com/eel-primo/pyAutoUpdate/main/example.py'])

li.install()
from colorama import Fore

#Sadly, but works fine only on Linux :(
if fu.install():
    print(Fore.YELLOW + "Files were updated, reopen app for applying changes")
    exit()

#Your code
print(Fore.GREEN + "Hello world!")
input()
