from collections import deque
class Fifo:
    ready_queue = deque()
    running = None
    processes = []

    @classmethod
    def run(cls):
        if cls.running == None and len(cls.ready_queue) != 0:
            cls.running = cls.ready_queue.popleft()
            cls.running.response_time = cls.running.waiting_time

        if cls.running != None:
            cls.update_waiting_time()
            cls.running.cpu_time += 1
            if cls.running.cpu_time == cls.running.burning_time:
                if len(cls.ready_queue) != 0:
                    cls.running = cls.ready_queue.popleft()
                    cls.running.response_time = cls.running.waiting_time
        
    
    @classmethod
    def update_waiting_time(cls):
        for proc in cls.ready_queue:
            proc.update_waiting_time()
    @classmethod
    def insert_process(cls, proc):
        cls.processes.append(proc)
        cls.ready_queue.append(proc)

