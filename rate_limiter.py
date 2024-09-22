import time
import threading
# using token bucket algorithm where tokens are added at a rate of max_requests / interval_seconds
# and tokens are consumed at a rate of 1 per request
# if tokens are less than 1, rate limit is exceeded
# tokens are added for the time passed since the last request
# this implementation is not thread-safe

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
                print(f"current_time: {current_time}. last_request_time: {self.last_request_time}. time_passed: {time_passed}.")
                self.tokens += time_passed * (self.max_requests / self.interval_seconds) # add tokens for the time passed since the last request
                self.tokens = min(self.tokens, self.max_requests)

                print(f"Tokens increased after last request: {self.tokens}.")
                if self.tokens > self.max_requests:
                    self.tokens = self.max_requests
                
                if self.tokens < 1:
                    self.tokens -= 1
                    self.last_request_time = current_time
                    print("tokens after request execution: ", self.tokens)
                    raise Exception("Rate limit exceeded. Please try again later.")
                
                self.tokens -= 1
                self.last_request_time = current_time
                print("tokens after request execution: ", self.tokens)
            return func(*args, **kwargs)
        return wrapper