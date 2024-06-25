import pendulum
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from datetime import timedelta


default_args = {
    "owner": "airflow",
    "retries": 1,
    "email": ["zheros9303@gmail.com"],
    "retry_delay": timedelta(minutes=5),
}


@dag(
    default_args=default_args,
    schedule_interval=None,
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    tags=["python package list check"],
)
def airflow_environment_check():
    """
    ### Dag Documentation
    mwaa 인스턴스의 각종 환경 설정을 확인하기 위한 dag입니다.
    """
    check_python_environment = BashOperator(
        task_id="check_python_version",
        bash_command="python3 --version; python3 -m pip list",
    )

    check_python_environment


dag = airflow_environment_check()