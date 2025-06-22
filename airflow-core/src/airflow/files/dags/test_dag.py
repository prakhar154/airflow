import logging

from airflow.sdk import DAG, Param, task

logger = logging.getLogger(__name__)

with DAG(
    "test_dag",
    schedule=None,
    params={
        "my_list": Param(
            default=None,
            type=["null", "array"],
            items={
                "type": "string",
            },
        ),
    }
) as dag:

    @task
    def test_task():
        logger.info(f"my_list: {dag.params.get_resolved_or_default('my_list', [])}") # Defined param, returns None
        logger.info(f"absent_list: {dag.params.get('absent_list', [])}") # Undefined param, returns []

    test_task()

if __name__ == "__main__":
    dag.test()
