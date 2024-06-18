import threading
import concurrent.futures
import logging
from typing import List
import time

# Setup logging
def setup_logging() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("multithreading.log"),
            logging.StreamHandler()
        ]
    )

class Task:
    """A class to represent a task that can be executed in a thread."""
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(self.name)

    def execute(self, duration: int) -> None:
        """Execute the task, simulating a long-running operation."""
        self.logger.info(f"Starting task {self.name} with duration {duration}")
        try:
            for i in range(duration):
                self.logger.debug(f"Task {self.name} running: {i+1}/{duration}")
                time.sleep(1)
            self.logger.info(f"Task {self.name} completed")
        except Exception as e:
            self.logger.error(f"Error occurred in task {self.name}", exc_info=True)
            raise

def run_tasks_sequential(tasks: List[Task], durations: List[int]) -> None:
    """Run tasks sequentially, ensuring one waits for the other."""
    for task, duration in zip(tasks, durations):
        task.execute(duration)

def run_tasks_concurrent(tasks: List[Task], durations: List[int]) -> None:
    """Run tasks concurrently using threading."""
    threads = []
    for task, duration in zip(tasks, durations):
        thread = threading.Thread(target=task.execute, args=(duration,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

def run_tasks_async(tasks: List[Task], durations: List[int]) -> None:
    """Run tasks asynchronously using concurrent.futures."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(task.execute, duration) for task, duration in zip(tasks, durations)]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logging.error("Error occurred during async execution", exc_info=True)

def main() -> None:
    """Main function to demonstrate multithreading and asynchronous execution."""
    setup_logging()

    tasks = [Task(f"Task-{i}") for i in range(3)]
    durations = [2, 3, 1]

    print("Running tasks sequentially:")
    run_tasks_sequential(tasks, durations)

    print("\nRunning tasks concurrently:")
    run_tasks_concurrent(tasks, durations)

    print("\nRunning tasks asynchronously:")
    run_tasks_async(tasks, durations)

if __name__ == "__main__":
    main()
