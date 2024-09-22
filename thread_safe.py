import time
import threading
from rate_limiter import RateLimiter


# Example usage
class Calculator:
    def __init__(self, max_requests, interval_seconds):
        self.rate_limiter = RateLimiter(max_requests, interval_seconds)

    @property
    def get_sum(self):
        @self.rate_limiter  # rate limit the get_sum method using the decorator
        def get_sum(thread_number, a, b):
            return a + b
        return get_sum
    
def call_method_get_sum(thread_number):
    second = 0
    for i in range(1, 11):
        print(f"This is request number {i} at second {second}. from thread {thread_number}.")
        try:
            val = calc_object.get_sum(thread_number, 1, 2)
        except Exception as e:
            print(e) 
        finally:
            second += 5
            time.sleep(5)

if __name__ == "__main__":
    calc_object = Calculator(max_requests=5, interval_seconds=60)

    # Test rate-limited method
    # Create and start multiple threads
    threads = [threading.Thread(target=call_method_get_sum, args=(i,)) for i in range(2)]
    
    for i, thread in enumerate(threads):
        print(f"Starting thread {i}")
        thread.start()


    # Wait for all threads to finish
    for i, thread in enumerate(threads):
        thread.join()
        print(f"Thread {i} finished")