import json
import time
from extensitrace import ExtensiTrace, Task


logger: ExtensiTrace = ExtensiTrace(log_file='event_log.jsonl', task_flush_limit=10)

@logger.log(track=True)
def test():
    logger.add_metadata({'key': 'value'})
    test2()
    pass

@logger.log()
def test2():
    pass

@logger.log(track=True)
def test3():
    pass

def check_num_task_ids():
    with open('event_log.jsonl', 'r') as file:
        json_data = [json.loads(line) for line in file]
        log_data = [Task(**entry) for entry in json_data]
        task_ids = [entry.task_id for entry in log_data if entry.task_id is not None]
        return len(set(task_ids))
    
    
    
if __name__ == '__main__':
    with open('event_log.jsonl', 'w') as file:
        file.write('')

    for i in range(25):
        test()
        if i == 9:
            assert check_num_task_ids() == 10
    assert check_num_task_ids() == 20 
    # Upon destruction there will be 5 tasks which will also be flushed