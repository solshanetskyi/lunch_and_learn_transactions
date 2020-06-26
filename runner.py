from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep

from common import clean_up, create_records, print_error, print_final, print_database, print_second, print_first


def runner(first_flow, second_flow):
    clean_up()
    create_records()

    with ThreadPoolExecutor() as executor:
        first_flow_task = executor.submit(first_flow, print_first)
        sleep(2)
        second_flow_task = executor.submit(second_flow, print_second)

    try:
        first_flow_task.result()
    except Exception as e:
        print_error(f'First flow failed: {e}')

    try:
        second_flow_task.result()
    except Exception as e:
        print_error(f'Second flow failed: {e}')

    print_database(print_final)
