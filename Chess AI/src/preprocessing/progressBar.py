import sys
import time

class ProgressBar:
    def __init__(self, total, length=100):
        self.total = total
        self.length = length
        self.start_time = time.time()
        self.current = 0

    # Call this function to update the progress bar
    def update(self, iteration, total):
        self.current = iteration
        self.total = total
        percent = ("{0:.1f}").format(100 * (self.current / float(total)))
        filled_length = int(self.length * self.current // total)
        bar = '█' * filled_length + '-' * (self.length - filled_length)
        sys.stdout.write('\r|%s| %s%%' % (bar, percent))
        sys.stdout.flush()

    # Call this function to update the progress bar, but it will be smooth by adding 1 per .5 seconds
    def smooth_update(self, iteration):
        amount = iteration - self.current
        for i in range(int(amount * 2)):
            self.update(iteration + (i * .5), self.total)
            time.sleep(.05)
        


