import time
from threading import Thread

def countdown(n):
	while n > 0:
		print("T-minus {}".format(n))
		n -= 1
		time.sleep(1)

def countup(n):
	for i in range(n):
		print("T-add {}".format(i))
		time.sleep(1)

class CountDownTask(object):
	"""docstring for CountDownTask"""
	def __init__(self):
		super(CountDownTask, self).__init__()
		self._running = True

	def terminate(self):
		self._running = False

	def running(self, n):
		while self._running and n > 0:
			print("T-minus {}".format(n))
			n -= 1
			time.sleep(1)

class CountDownThread(Thread):
	"""docstring for Count"""
	def __init__(self, n):
		super().__init__()
		self.n = n
	def run(self):
		while self.n > 0:
			print("T-minus {}".format(self.n))
			self.n -= 1
			time.sleep(0.5)
		

def test1():
	t = Thread(target=countdown, args=(10,), daemon=True)
	t2 = Thread(target=countup, args=(5,), daemon=True)
	t.start()
	t2.start()
	t.join()
	while True:
		time.sleep(3)
		if t.is_alive():
			print("thread is still running.")
		else:
			print("completed")
			return

def test2():
	c = CountDownTask()
	t = Thread(target=c.running, args=(10,), daemon=True)
	t.start()
	c.terminate()
	t.join()

def test3():
	import multiprocessing
	c = CountDownThread(5)
	c.start()

if __name__ == '__main__':
	test3()