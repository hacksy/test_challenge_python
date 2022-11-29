from timeit import default_timer as timer


class TimeLoggerRepository:

    def __init__(self):
        self.initial = 0
        self.title = ""

    def start(self, title):
        self.title = title
        self.initial = timer()

    def stop(self):
        final = timer()
        total_time = final - self.initial
        # Write to file
        with open("logger.txt", "a") as f:
            f.write("{} -  Request duration: {}\n".format(self.title, total_time))
