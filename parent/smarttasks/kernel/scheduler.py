# Imports
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor

# BEGIN

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///smarttasks.lab-ctrl')
}
executors = {
    'default': ThreadPoolExecutor(2),
}
job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

# instantiate the scheduler
scheduler = BackgroundScheduler(
    jobstores=jobstores,
    executors=executors, 
    job_defaults=job_defaults
)

# END

if __name__ == '__main__':
    pass