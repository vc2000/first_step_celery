import celery


@celery.task()
def print_hello():
    logger = print_hello.get_logger()
    logger.info("Hello")


@celery.task(name='tasks.play_task')
def play_task():  
    print('play something')
    return "say hi"

"""@celery.task(name='tasks.pause_task')
def pause_task():  
    print('enough fun')
    return 'enough fun'"""