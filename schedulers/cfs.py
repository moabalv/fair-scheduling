import heapq

class CFS:
    def __init__(self, target_latency, min_granularity, scheduler_tick):
        self.target_latency = target_latency
        self.min_granularity = min_granularity
        self.ready_queue = [] #heap
        self.processes = []
        self.running = None
        self.quantum = 0
        self.scheduler_tick = scheduler_tick
        self.clock = 0
        self.simulation = []

    def run(self):
        #Interrupts the CPU and verifies if there's a process with a lower virtual runtime
        if self.clock == self.scheduler_tick:
            self.clock = 0
            self.schedule_next_process()

        # A process is scheduled
        if self.running != None:
            
            self.register_simulation()
            self.execute_process()
        
            #The process is over
            if (self.running.cpu_time == self.running.burning_time):
                    self.running = None
                    self.schedule_next_process()
            #The process quantum is over
            elif (self.quantum == self.calculate_time_slice()):
                    heapq.heappush(self.ready_queue, self.running)
                    self.quantum = 0
                    self.running = None
                    self.schedule_next_process()
        #There's no process running, try scheduling something!
        else: 
            self.schedule_next_process()
            self.execute_process()
            self.register_simulation()

    def register_simulation(self):
        if (self.running == None):
            self.simulation.append(None)
        else:
            self.simulation.append(self.running.pid)

    def execute_process(self):
        if self.running != None:
            self.update_waiting_time()
            self.quantum += 1
            self.running.virtual_runtime += 1
            self.running.cpu_time += 1
            self.clock += 1


    def calculate_time_slice(self):
        if (len(self.ready_queue) > 0):
            actual = self.target_latency // len(self.ready_queue)
            self.time_slice =  actual
            if actual < self.min_granularity:
                self.time_slice = self.min_granularity
        else:
            self.time_slice = self.target_latency

    def schedule_next_process(self):
        if len(self.ready_queue) > 0:
           temp = heapq.heappop(self.ready_queue)
           # There's no process running
           if self.running == None:
               self.running = temp 

               if self.running.response_time == None:
                  self.running.response_time = self.running.waiting_time

           # Schedulling the lowest run time
           elif temp.virtual_runtime < self.running.virtual_runtime:
               heapq.heappush(self.ready_queue, self.running)
               self.running = temp
               if self.running.response_time == None:
                  self.running.response_time = self.running.waiting_time
           else:
               heapq.heappush(self.ready_queue, temp)
               
           
    def insert_process(self, proc):
        self.processes.append(proc)
        proc.virtual_runtime = self.get_lowest_virtual_runtime()
        heapq.heappush(self.ready_queue, proc)

    def get_lowest_virtual_runtime(self):
        if (len(self.ready_queue) > 0):
            lowest = self.ready_queue[0].virtual_runtime
        else:
            lowest = 0
        if (self.running != None and self.running.virtual_runtime < lowest):
            lowest = self.running.virtual_runtime
        return lowest

    def update_waiting_time(self):
        for proc in self.ready_queue:
            proc.update_waiting_time()
