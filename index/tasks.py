from celery import shared_task
# from testcase.celery import celery


@shared_task
def test_celery(x):
    print('test is Ok', 'and x is: ', x)

# @celery.task
# def test_celery_2nd_way(x):
#     print('test_2 is Ok', 'and x is:, x)
