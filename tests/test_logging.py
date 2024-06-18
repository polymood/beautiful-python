import sys
import os
import unittest
import logging

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.logging_example import setup_logging, TaskProcessor

class TestLoggingExample(unittest.TestCase):

    def setUp(self):
        setup_logging()
        self.logger = logging.getLogger("TestLogger")

    def test_simple_task(self):
        task = TaskProcessor("SimpleTask")
        with self.assertLogs(task.logger, level='INFO') as cm:
            task.start_task()
        self.assertIn("INFO:SimpleTask:Starting task", cm.output)
        self.assertIn("INFO:SimpleTask:Task completed successfully", cm.output)

    def test_task_with_warning(self):
        task = TaskProcessor("TaskWithWarning")
        with self.assertLogs(task.logger, level='WARNING') as cm:
            task.start_task()
        self.assertIn("WARNING:TaskWithWarning:This task may cause warnings", cm.output)

    def test_task_with_error(self):
        task = TaskProcessor("TaskWithError")
        with self.assertLogs(task.logger, level='ERROR') as cm:
            with self.assertRaises(RuntimeError):
                task.start_task()
        self.assertIn("ERROR:TaskWithError:This task is designed to fail", cm.output)
        self.assertIn("ERROR:TaskWithError:An error occurred while executing the task", cm.output)

if __name__ == "__main__":
    unittest.main()
