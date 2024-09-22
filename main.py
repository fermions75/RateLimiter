from rate_limiter import RateLimiter
import time

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
    

if __name__ == "__main__":
    # configure rate limit per minute through constructor
    calc_object = Calculator(max_requests=5, interval_seconds=60) # 5 requests per minute

    # Test rate-limited method
    second = 0
    for i in range(1, 11):
        print(f"This is request number {i} at second {second}.")
        try:
            val = calc_object.get_sum(1, 2)
            print(f"Sum: {val}")
        except Exception as e:
            print(e)
        finally:
            second += 5
            time.sleep(5)