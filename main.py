import time

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

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            time_passed = current_time - self.last_request_time
            # print(f"current_time: {current_time}. last_request_time: {self.last_request_time}. time_passed: {time_passed}.")
            self.tokens += time_passed * (self.max_requests / self.interval_seconds) # add tokens for the time passed since the last request
            print(f"Tokens: {self.tokens}.")
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
            # print("tokens after request: ", self.tokens)
            return func(*args, **kwargs)
        return wrapper

# Example usage
class Calculator:
    def __init__(self, max_requests, interval_seconds):
        self.rate_limiter = RateLimiter(max_requests, interval_seconds)

    @property
    def get_sum(self):
        @self.rate_limiter # rate limit the get_sum method using the decorator
        def get_sum(a, b):
            return a + b
        return get_sum

# configure rate limit per minute through constructor
calc_object = Calculator(max_requests=5, interval_seconds=60) # 5 requests per minute

# Test rate-limited method
second = 0
for i in range(1, 11):
    print(f"This is request number {i} at second {second}.")
    try:
        val = calc_object.get_sum(1, 2)
        print(val)
    except Exception as e:
        print(e)
    finally:
        second += 5
        time.sleep(5)