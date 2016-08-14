from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from server import db, app

executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

scheduler = BackgroundScheduler(executors=executors,job_defaults=job_defaults)


@scheduler.scheduled_job('interval', id='minimograthy_job', minutes=60)
def minimography_job():
    app.logger.info('minimograthy_job')
    from minimography import Minimography
    m = Minimography()
    m.process()

#scheduler.add_job(minimography_job,'interval',seconds=20)
# scheduler.start()
