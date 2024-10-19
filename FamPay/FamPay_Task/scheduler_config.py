from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from .get_videos import get_new_videos_periodic


def initialize():
    try:
        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # Add the job
        scheduler.add_job(
            get_new_videos_periodic,
            trigger="interval",
            seconds=3,
            id="get_new_videos_job",
            max_instances=1,
            replace_existing=True,
        )

        scheduler.start()
        print("Scheduler started successfully!")
        
    except Exception as e:
        print(f"Error starting scheduler: {e}")