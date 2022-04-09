from celery import Celery
from celery.schedules import crontab
import requests

app = Celery("main", broker="redis://localhost:6379/0")

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute="*/1"),
        hello.s(),
        name="fetching data"
    )

@app.task
def hello():
    requests.post("http://127.0.0.1:8000/database")
