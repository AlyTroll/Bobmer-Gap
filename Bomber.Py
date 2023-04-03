system("python -m pip install os")
from os import system
import os
system("python -m pip install ArseinRubika==4.8.2")
system("python -m pip install colorama")
system("python -m pip install pyfiglet")
os.system('clear')
from libraryArsein import Robot_rubika
import rainbowtext,pyfiglet
import colorama
import os
red = '31[31m'
yellow = '31[31m'
green = '31[31m'
blue = '31[31m'
pink = '31[31m'
white = '31[31m'
os.system('clear')
print(rainbowtext.text(pyfiglet.figlet_format("Ali TROLL")
user = input("Enter Number Bomb: ")
print(yellow+"{"red+"1"yellow+"}"red+"Bomber")
print(yellow+"{"red+"2"yellow+"}"red+"Bomber (Send Message)")
print("")
if user == 1:
   while True:
          for auth in auth:
           try:
auth = input("Please Enter auth : ")
Gap = input("Please Enter Link Gap : ")
os.system('clear')
bot = Robot_rubika(auth)
info = bot.joinGroup(Gap)
gap = info['data']['group']['group_guid']
bot.leaveGroup(gap)
print(green+"BOMB✓")
           except:
                continue
if user == 2:
      while True:
           for auth in auth:
               try:
auth = input("Please Enter auth : ")
Gap = input("Please Enter Link Gap : ")
message = input("Enter Message : ")
os.system('clear')
bot = Robot_rubika(auth)
info = bot.joinGroup(Gap)
gap = info['data']['group']['group_guid']
bot.sendMessage(gap,message)
bot.leaveGroup(gap)
print(green+"BOMB✓")
           except:
                continue
     else:
print(red+"EROR")
