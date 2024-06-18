import sys
import os
import unittest
import logging

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from multithreading_example import Task, run_tasks_sequential, run_tasks_concurrent, run_tasks_async, setup_logging

class TestMultithreadingExample(unittest.TestCase):

    def setUp(self):
        setup_logging()
        self.tasks = [Task(f"TestTask-{i}") for i in range(3)]
        self.durations = [1, 2, 1]

    def test_sequential_execution(self):
        with self.assertLogs(level='INFO') as cm:
            run_tasks_sequential(self.tasks, self.durations)
        self.assertIn("INFO:TestTask-0:Starting task TestTask-0 with duration 1", cm.output)
        self.assertIn("INFO:TestTask-1:Starting task TestTask-1 with duration 2", cm.output)
        self.assertIn("INFO:TestTask-2:Starting task TestTask-2 with duration 1", cm.output)

    def test_concurrent_execution(self):
        with self.assertLogs(level='INFO') as cm:
            run_tasks_concurrent(self.tasks, self.durations)
        self.assertIn("INFO:TestTask-0:Starting task TestTask-0 with duration 1", cm.output)
        self.assertIn("INFO:TestTask-1:Starting task TestTask-1 with duration 2", cm.output)
        self.assertIn("INFO:TestTask-2:Starting task TestTask-2 with duration 1", cm.output)

    def test_async_execution(self):
        with self.assertLogs(level='INFO') as cm:
            run_tasks_async(self.tasks, self.durations)
        self.assertIn("INFO:TestTask-0:Starting task TestTask-0 with duration 1", cm.output)
        self.assertIn("INFO:TestTask-1:Starting task TestTask-1 with duration 2", cm.output)
        self.assertIn("INFO:TestTask-2:Starting task TestTask-2 with duration 1", cm.output)

if __name__ == "__main__":
    unittest.main()
