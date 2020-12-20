# https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/
import time
import logging
import multiprocessing
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# Initializations
event_handler = LoggingEventHandler()
observer = Observer()

folder = "C:/Users/Notebook/Downloads"
folder1 = "C:/Users/Notebook/Documents"


def monitor_folder(folder):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    observer.schedule(event_handler, folder, recursive=True)
    observer.start()

    try:
        while True:
            # Set the thread sleep time
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    m = multiprocessing.Process(target=monitor_folder, args=(folder,))
    m1 = multiprocessing.Process(target=monitor_folder, args=(folder1,))
    m.start()
    m1.start()
