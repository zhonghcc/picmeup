from apscheduler.schedulers.background import BackgroundScheduler
from server import db,app

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

scheduler = BackgroundScheduler(job_defaults=job_defaults)


@scheduler.scheduled_job('interval',id='minimograthy_job',seconds=40)
def minimography_job():
    print 'hello'
    from minimography import Minimography
    m=Minimography()
    m.process()

#scheduler.add_job(minimography_job,'interval',id='minimograthy_job',seconds=20)
#scheduler.start()

