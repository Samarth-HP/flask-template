from flask import Flask, request, jsonify
import logging
import time
from logging.handlers import TimedRotatingFileHandler
import psycopg2
from dotenv import load_dotenv
from functools import wraps
import os
from celery import Celery

load_dotenv()
app = Flask(__name__)

####################################################
#   database config imports                        #
####################################################
# DATABASE_HOST = os.getenv('db_host')
# DATABASE_PORT = os.getenv('db_port')
# DATABASE_USER_NAME = os.getenv('db_user_name')
# DATABASE_PASSWORD = os.getenv('db_password')
# DATABASE_NAME = os.getenv('db_name')
# DATABASE_SCHEMA = os.getenv('db_schema')
# DATABASE_TABLE = os.getenv('db_table')


####################################################
#   uncomment this block to enable logger          #
####################################################
# Set up logging
# def init_logger_def():
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)
#     try:
#         handler = TimedRotatingFileHandler(
#             "./logs/debug.log", when="midnight", interval=1, backupCount=1)
#     except:
#         handler = TimedRotatingFileHandler(
#             "../logs/debug.log", when="midnight", interval=1, backupCount=1)
#     handler.setLevel("DEBUG")
#     formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
#     handler.setFormatter(formatter)
#     # add a suffix which you want
#     handler.suffix = "%Y%m%d"
#     # need to change the extMatch variable to match the suffix for it
#     handler.extMatch = re.compile(r"^\d{8}$")
#     logger.addHandler(handler)
#
#     return logger
#
# logger = init_logger_def()


####################################################
#   initialize celery                              #
####################################################
# Initialize Celery
# app.config['CELERY_BROKER_URL'] = os.getenv('celery_broker_url')
# app.config['CELERY_RESULT_BACKEND'] = os.getenv('celery_result_backend')
# max_retries = os.getenv('max_retries')
# retry_backoff = os.getenv('retry_backoff')
# RESULT_EXPIRE_TIME = 60 * 60 * 4
# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], result_backend=app.config['CELERY_RESULT_BACKEND'], result_expires=RESULT_EXPIRE_TIME)
# celery.conf.update(app.config)


####################################################
#   initialize logstash                            #
####################################################
# logstash_host = os.getenv('logstash_host')
# logstash_port = os.getenv('logstash_port')

# Initialize Logstash
# def init_logstash_logger():
#     logstash_handler = AsynchronousLogstashHandler(
#         logstash_host,
#         int(logstash_port),
#         database_path=None,
#         transport='logstash_async.transport.BeatsTransport'
#     )
#     logstash_handler.formatter = FlaskLogstashFormatter(metadata={"beat": "{project_name}"})
#     logger = logging.getLogger("#logstash_logger")
#     logger.addHandler(logstash_handler)
#     return logger
# logstash_logger = init_logstash_logger()


####################################################
# function to setup up connection with postgres-db #
####################################################
# def get_connection():
#     """ Connect to the database server
#     Args:
#         conn_string: database connection string
#     Returns:
#         connection object
#     """
#     conn = None
#     try:
#         # logger.info('Connecting to the database ...')
#         conn = psycopg2.connect(
#             user=DATABASE_USER_NAME,
#             password=DATABASE_PASSWORD,
#             host=DATABASE_HOST,
#             port=DATABASE_PORT,
#             database=DATABASE_NAME)
#     except Exception as e:
#         logger.error(e)
#     return conn


####################################################
#   sample function to add celery tasks            #
####################################################
# @celery.task(max_retries=max_retries, retry_backoff=retry_backoff, autoretry_for=(Exception, psycopg2.Error), ignore_result=True, store_errors_even_if_ignored=True)
# def add_task(data, query, param_list):
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         # Store data in main dump table
#         cursor.execute(query, get_tuple_from_dict(data, param_list))
#         connection.commit()
#     except (Exception, psycopg2.Error) as error:
#         logger.error(f"Error in update operation {error}")
#     finally:
#         # closing database connection.
#         if connection:
#             cursor.close()
#             connection.close()
#             # logger.info("PostgreSQL connection is closed")


####################################################
#   decorator for audit logs                       #
####################################################
# def timed(func):
#     """This decorator prints the execution time for the decorated function."""
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         try:
#             result = func(*args, **kwargs)
#             end = time.time()
#             logger.info("project_name: {} ran in {}s".format(func.__name__, round(end - start, 2)))
#             logstash_logger.info("ODK-LOGS: {} ran in {}s".format(func.__name__, round(end - start, 2)))
#         except Exception as error:
#             logger.error("project_name: Exception in {} - {} : {}".format(func.__name__, type(error).__name__, error))
#             logstash_logger.error("project_name: Exception in {} - {} : {}".format(func.__name__, type(error).__name__, error))
#             return "error", 404
#         return result
#
#     return wrapper


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
