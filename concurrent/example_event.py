'''
event & thread examples
'''
import time
import  threading

def countdown_evt(n, start_evt):
	print("Countdown Task starting")
	start_evt.set()

	while n > 0:
		print("T-minus {}".format(n))
		n -= 1
		time.sleep(0.5)

class PreiodicTimer:
	"""docstring for PreiodicTimer"""
	def __init__(self, interval):
		self._interval = interval
		self._flag = 0
		self._cv = threading.Condition()

	def start(self):
		t = threading.Thread(target=self.run, daemon=True)
		t.start()

	def run(self):
		while True:
			time.sleep(self._interval)
			with self._cv:
				self._flag ^= 1
				self._cv.notify_all()

	def wait_for_tick(self):
		with self._cv:
			last_flag = self._flag
			while self._flag == last_flag:
				self._cv.wait()

def worker(n, sema):
	sema.acquire()
	print("working {}".format(n))

def test1():
	start_evt = Event()

	print("Launch countdown")
	t = Thread(target=countdown_evt, args=(10, start_evt))
	t.start()

	start_evt.wait()
	print("countdown is running")

def test2():
	ptimer = PreiodicTimer(0.5)
	ptimer.start()

	def countdown(n):
		while n>0:
			ptimer.wait_for_tick()
			print("T-minus {}".format(n))
			n -= 1
			
	def countup(last):
		n = 0
		while n<last:
			ptimer.wait_for_tick()
			print("counting", n)
			n += 1

	threading.Thread(target=countdown, args=(10,)).start()
	threading.Thread(target=countup, args=(5,)).start()

def test3():
	sema = threading.Semaphore()
	nworkers = 10

	for i in range(nworkers):
		t = threading.Thread(target=worker, args=(i, sema,))
		t.start()

	for i in range(nworkers):
		sema.release()

if __name__ == '__main__':
	test3()