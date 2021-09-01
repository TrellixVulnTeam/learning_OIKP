#1 importing modules
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


#2 Default Arguments

default_args={
    "owner" : "airflow",
    "start_date":airflow.utils.dates.days_ago(2),

    #'end_date' : datetime(2021-09-01),
    "depends_on_past":False,
    "email": ['saka90030@gmail.com'],
    "email_on_failure": True,
    "email_on_retry" : False,

    #if a task fails, retry it once after waiting at least 5 min
    "retries" : 1,
    "retry_delay" : timedelta(minutes=5)
}


#Step 3:instantiate a DAG
    #Give the DAG name, configure the schedule, and set the DAG settings.

dag = DAG(
    "tutorial",
    default_args=default_args,
    description="A simple tutorial DAG",

    #continue to run DAG once per day
    schedule_interval=timedelta(days=1)   #how often DAH should be triggered.
)


#Step 4 : layout the tasks
t1 = BashOperator(
    task_id="print_date",
    bash_command="date",
    dag=dag
)

t2 = BashOperator(
    task_id="sleep",
    depends_on_past=False,
    bash_command="sleep 5",
    dag=dag
)

templated_command = """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param}}"
{% endfor %}
"""

t3 = BashOperator(
    task_id="templated",
    depends_on_past=False,
    bash_command=templated_command,
    params={"my_param":"Parameter I passed in"},
    dag=dag
)



#5 Setting up Dependencies

#this means that t2 will depend on t1 running successfully to run
t1.set_downstream(t2)

#similar to above where t3 will depend on t1
t3.set_upstream(t1)

#t1.set_downstream([t2,t3])


#bit shift operator can also be used to chain operations
# ti>>t2  t2 << t1