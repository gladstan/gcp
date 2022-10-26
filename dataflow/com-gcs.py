from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


classairflow.providers.google.cloud.sensors.gcs.GCSObjectUpdateSensor\
    (bucket,
      object,
     ts_func=ts_function, google_cloud_conn_id='google_cloud_default',
     delegate_to=None,
     impersonation_chain=None)

