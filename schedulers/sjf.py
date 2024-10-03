class SJF:
    def __init__(self):
        self.ready_queue = []
        self.processes = []
        self.simulation = []
        self.running = None
    
    def run(self):
        if self.running == None and len(self.ready_queue) > 0:
            self.running = self.ready_queue.pop(0)
            self.running.response_time = self.running.waiting_time 
    
        if self.running != None:
            self.simulation.append(self.running.pid)
            self.execute_process()

            #The process is over
            if (self.running.cpu_time == self.running.burning_time):
                self.running = None
        
    def execute_process(self):
        self.update_waiting_time()
        self.running.cpu_time += 1

    def update_waiting_time(self):
        for proc in self.ready_queue:
            proc.update_waiting_time()

    def insert_process(self, proc):
        self.ready_queue.append(proc)
        self.ready_queue.sort(key=lambda proc: proc.burning_time)
        self.processes.append(proc)