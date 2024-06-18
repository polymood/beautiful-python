import logging

def setup_logging() -> None:
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )

class TaskProcessor:
    """A class to process tasks with logging."""

    def __init__(self, task_name: str):
        self.task_name = task_name
        self.logger = logging.getLogger(self.task_name)

    def start_task(self) -> None:
        """Start the task and log the process."""
        self.logger.info("Starting task")
        try:
            self._execute_task()
        except Exception as e:
            self.logger.error("An error occurred while executing the task", exc_info=True)
            raise

    def _execute_task(self) -> None:
        """Execute the task and log the process."""
        self.logger.debug("Executing task")
        if self.task_name == "TaskWithWarning":
            self.logger.warning("This task may cause warnings")
        elif self.task_name == "TaskWithError":
            self.logger.error("This task is designed to fail")
            raise RuntimeError("Intentional error for demonstration")
        self.logger.info("Task completed successfully")

def main() -> None:
    """Main function to demonstrate logging."""
    setup_logging()

    task1 = TaskProcessor("SimpleTask")
    task2 = TaskProcessor("TaskWithWarning")
    task3 = TaskProcessor("TaskWithError")

    try:
        task1.start_task()
    except Exception as e:
        print(f"Error occurred: {e}")

    try:
        task2.start_task()
    except Exception as e:
        print(f"Error occurred: {e}")

    try:
        task3.start_task()
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
