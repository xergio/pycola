
import time
import random
import multiprocessing

import loader
import item



class Pycola(object):
    
    def __init__(self, workers=5, loader_obj=loader.Loader, item_obj=item.Item):
        self._num_workers = workers
        self._items_queue = multiprocessing.JoinableQueue()
        self._loader_obj = loader_obj
        self._item_obj = item_obj
    

    def loop(self):
        try:
            while True:
                self.launch()
                self.fill()
                time.sleep(5)

        except KeyboardInterrupt:
            print "Stopping main loop"


    def launch(self):
        active_workers = len(multiprocessing.active_children())
        for w in range(self._num_workers - active_workers):
            Worker(self._items_queue, self._item_obj).start()


    def fill(self):
        if self._items_queue.qsize() < 50:

            item_list = self.get_items()
            print "adding %d" % len(item_list)

            for item in item_list:
                self._items_queue.put(item)
        
        print "qsize: %d" % self._items_queue.qsize()
            
            
    def get_items(self):
        return self._loader_obj().load()



class Worker(multiprocessing.Process):

    def __init__(self, items_queue, item_obj):
        multiprocessing.Process.__init__(self)
        self._items_queue = items_queue
        self._item_obj = item_obj
    

    def run(self):
        try:
            self.loop()
            
        except KeyboardInterrupt:
            print "Terminating %s" % self.name
        
        
    def loop(self):
        while True:
            if not self._items_queue.empty():
                item = self._items_queue.get()
            else:
                item = None
        
            if item is not None:
                start_time = time.time()
                
                result = self._item_obj(item)()
                self._items_queue.task_done()

                self.wait(start_time, item)

            else:
                time.sleep(0.5) # idle, empty queue


    def wait(self, start_time, item):
        done_time = time.time() - start_time
        sleep_time = 1 - (done_time if done_time > 0 else 0)

        if sleep_time < 0: sleep_time = 0.00001
        print "%s execute %d in %f. sleep %f" % (self.name, item, done_time, sleep_time)
        time.sleep(sleep_time)
