# commit-bot.py

import subprocess
import datetime
#from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

s = BlockingScheduler()

d = datetime.datetime(2017, 8, 3, 1, 16, 00)

def write(d):
    file = open("myfile.txt", 'a')
    file.write("Commit on " + str(datetime.datetime.now()))
    file.write("\n")
    file.close()

#    d += datetime.timedelta(seconds=10) # for testing/debugging
    d += datetime.timedelta(days=1)
    s.add_job(write, 'date', run_date=d, args=[d])

s.add_job(write, 'date', run_date=d, args=[d])

#print(datetime.datetime.now())

#print(subprocess.check_output(['ls', '-l']))

s.start()
#s.print_jobs()
