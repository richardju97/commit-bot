# commit-bot.py

import subprocess
import datetime

#print(datetime.datetime.now())

file = open("myfile.txt", 'a')
file.write("Commit on " + str(datetime.datetime.now()))
file.write("\n")
file.close()

#print(subprocess.check_output(['ls', '-l']))

