from apscheduler.schedulers.background import BackgroundScheduler
from server import db,app
scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval',id='minimograthy_job',seconds=20)
def minimography_job():
    print 'hello'
    from minimography import Minimography
    db.session
    m=Minimography()
    m.process()

#scheduler.add_job(minimography_job,'interval',id='minimograthy_job',seconds=20)
#scheduler.start()

