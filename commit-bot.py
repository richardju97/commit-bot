# commit-bot.py

import subprocess
import datetime
#from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

s = BlockingScheduler()

def write():
    file = open("myfile.txt", 'a')
    file.write("Commit on " + str(datetime.datetime.now()))
    file.write("\n")
    file.close()

d = datetime.datetime(2017, 8, 3, 00, 16, 00)
s.add_job(write, 'date', run_date=d)

#print(datetime.datetime.now())

d += datetime.timedelta(seconds=10)
s.add_job(write, 'date', run_date=d)

#print(subprocess.check_output(['ls', '-l']))

s.start()
#s.print_jobs()
