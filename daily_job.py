"""
Copyright: Copyright (C) 2015 Baruch College
Description: automatic daily process
"""

# Scheduler imports
from apscheduler.schedulers.blocking import BlockingScheduler

# Job imports
from download_earnings import get_busystock_earnings
from download_close    import download_SPX

def main():

    sched = BlockingScheduler()

    @sched.scheduled_job('cron', day_of_week='mon,tue,wed,thu,fri,sat', hour=23)
    def scheduled_job():
    	print('[INFO] Job started.')
        get_busystock_earnings()
        download_SPX()
        print('[INFO] Job ended.')

    sched.start()    


if __name__ == '__main__':
    main()

