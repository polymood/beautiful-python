import time
import logging
from functools import wraps
from typing import Callable, Any

# Setup logging
def setup_logging() -> None:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_function_call(func: Callable) -> Callable:
    """Decorator to log function calls."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logging.info(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} finished")
        return result
    return wrapper

def measure_execution_time(func: Callable) -> Callable:
    """Decorator to measure execution time of a function."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@log_function_call
@measure_execution_time
def example_function(duration: int) -> None:
    """Example function that sleeps for a given duration."""
    time.sleep(duration)

def main() -> None:
    """Main function to demonstrate decorators."""
    setup_logging()
    example_function(2)

if __name__ == "__main__":
    main()
