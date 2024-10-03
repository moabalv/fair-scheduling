from collections import deque
class RoundRobin:
    def __init__(self, quantum):
        self.ready_queue = deque()
        self.running = None
        self.processes = []
        self.quantum = quantum
        self.simulation = []
 
    def run(self):
        #Schedule next process
        if self.running == None and len(self.ready_queue) != 0:
            self.schedule_next_process()
        
        if self.running != None:
            # Execute process
            self.simulation.append(self.running.pid) 
            self.execute_process()

            #The process is over
            if (self.running.cpu_time == self.running.burning_time):
                self.running = None

            #The process quantum is over
            elif (self.running.cpu_time % self.quantum == 0):
                self.ready_queue.append(self.running)
                self.running = None
        else:
            self.simulation.append(None)

    def execute_process(self):
        self.update_waiting_time()
        self.running.cpu_time += 1

    def schedule_next_process(self):
        self.running = self.ready_queue.popleft()
        #Update response time if the process is virgin
        if self.running.response_time == None:
            self.running.response_time = self.running.waiting_time

    def update_waiting_time(self):
        for proc in self.ready_queue:
            proc.update_waiting_time()

    def insert_process(self, proc):
        self.processes.append(proc)
        self.ready_queue.append(proc)