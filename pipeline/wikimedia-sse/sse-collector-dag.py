import datetime
from airflow.decorators import dag, task
from airflow.models import TaskInstance


@dag(schedule='1 0 * * *', start_date=datetime.datetime(2025, 5, 1), catchup=False)
def realtime_wikimedia():
    @task.bash
    def collect_wikimedia(task_instance: TaskInstance):
        execution_date: datetime.datetime = task_instance.execution_date
        running_date = execution_date.strftime('%Y-%m-%dT%H:%M:%S')
        return (f'cd /home/storage/wikimedia-sse && '
                f'sudo -u storage nohup venv/bin/python3 sse-collector.py --datetime {running_date} '
                f'>log.out 2>&1 </dev/null & '
                f'echo $!')

    collect_wikimedia()


realtime_wikimedia = realtime_wikimedia()



