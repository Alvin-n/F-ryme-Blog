from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep
from .inform_using_mail import send_mail_to
sleeplogger = get_task_logger(__name__)@task(name='my_first_task')
def my_first_task(duration):
    subject= 'Celery'
    message= 'message from celery'
    receiver= 'nasibov.elvin412@gmail.com'
    is_task_completed= False
    error=''
    try:
        sleep(duration)
        is_task_completed= True
    except Exception as err:
        error= str(err)
        logger.error(error)
    if is_task_completed:
        send_mail_to(subject,message,receiver)
    else:
        send_mail_to(subject,error,receiver)
    return('first_task_done')




# from celery import shared_task


# print("TEST TEST TEST TEST")
# @shared_task
# def exporter_handler(file_path=None, **kwargs):
#     print('test')