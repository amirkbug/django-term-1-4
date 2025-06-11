from celery import shared_task
import time

@shared_task
def send_mail():
    time.sleep(5)
    print("email sended")