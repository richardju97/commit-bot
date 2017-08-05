# commit-bot.py

import subprocess
import datetime
#from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

s = BlockingScheduler()

d = datetime.datetime(2017, 8, 4, 20, 30, 00)

def write(d):
    file = open("myfile.txt", 'a')
    n = str(datetime.datetime.now())
    file.write("Commit on " + n)
    file.write("\n")
    file.close()
    subprocess.check_output(['git', 'add', 'myfile.txt'])
    msg = "Commit from Commit Bot" + n
    subprocess.check_output(['git', 'commit', '-m', msg])
    subprocess.check_output(['git', 'push', 'origin', 'master'])

#    d += datetime.timedelta(seconds=10) # for testing/debugging
    d += datetime.timedelta(days=1)
    s.add_job(write, 'date', run_date=d, args=[d])

s.add_job(write, 'date', run_date=d, args=[d])

#print(datetime.datetime.now())

#print(subprocess.check_output(['ls', '-l']))

s.start()
#s.print_jobs()
