from os import listdir, system
from os.path import basename
from sys import executable

for filename in listdir():
    if filename.endswith(".py") and basename(filename) != basename(__file__):
        if system(executable + " " + filename):
        	print("[-] Failed:", filename)
        else:
        	print("[+] Success:", filename)