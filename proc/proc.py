class Proc:
    def __init__(self, pid, burning_time, arrival):
        self.pid = pid
        self.burning_time = burning_time
        self.arrival = arrival
        self.waiting_time = 0
        self.cpu_time = 0
        self.virtual_runtime = 0
        self.response_time = None
    
    def update_waiting_time(self):
        self.waiting_time += 1

    def __lt__(self, other):
        return self.cpu_time < other.cpu_time

