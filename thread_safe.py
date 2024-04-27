import time
import threading

# using token bucket algorithm where tokens are added at a rate of max_requests / interval_seconds
# and tokens are consumed at a rate of 1 per request
# if tokens are less than 1, rate limit is exceeded
# tokens are added for the time passed since the last request
# this implementation is thread safe
# the lock is used to ensure that only one thread can access the tokens and last_request_time at a time
class RateLimiter:
    def __init__(self, max_requests, interval_seconds):
        self.max_requests = max_requests
        self.interval_seconds = interval_seconds
        self.tokens = max_requests
        self.last_request_time = time.time()
        self.lock = threading.Lock()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self.lock:
                current_time = time.time()
                time_passed = current_time - self.last_request_time
                # print(f"current_time: {current_time}. last_request_time: {self.last_request_time}. time_passed: {time_passed}. from thread {args[0]}.")
                self.tokens += time_passed * (self.max_requests / self.interval_seconds)  # add tokens for the time passed since the last request
                # print(f"Tokens: {self.tokens}.")
                if self.tokens > self.max_requests:
                    self.tokens = self.max_requests
                
                if self.tokens < 1:
                    # print("Rate limit exceeded. Please try again later.")
                    self.tokens -= 1
                    self.last_request_time = current_time
                    # print("tokens after request: ", self.tokens)
                    raise Exception("Rate limit exceeded. Please try again later.")
                self.tokens -= 1
                self.last_request_time = current_time
                # print("calculation done for thread ", args[0])
                # print("tokens after request: ", self.tokens)
            return func(*args, **kwargs)
        return wrapper

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

calc_object = Calculator(max_requests=5, interval_seconds=60)

def call_method_get_sum(thread_number):
    second = 0
    for i in range(1, 11):
        print(f"This is request number {i} at second {second}. from thread {thread_number}.")
        try:
            val = calc_object.get_sum(thread_number, 1, 2)
            # print(val)
        except Exception as e:
            print(e) 
        finally:
            second += 5
            time.sleep(10) # for test purposes, sleep for 10 seconds before making the next request



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