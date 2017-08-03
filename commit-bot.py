# commit-bot.py

import subprocess
import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

s = BlockingScheduler()

def myFunction():
    file = open("myfile.txt", 'a')
    file.write("Commit on " + str(datetime.datetime.now()))
    file.write("\n")
    file.close()

s.add_job(myFunction, 'date', run_date=datetime.datetime(2017, 8, 2, 23, 59, 50))

#print(datetime.datetime.now())



#print(subprocess.check_output(['ls', '-l']))

s.start()
#s.print_jobs()
