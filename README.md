# Rate Limiter

This project demonstrates the use of a thread-safe rate limiter in Python.

## Description

The rate limiter uses a token bucket algorithm to limit the rate of requests. It is thread-safe, meaning it can be used by multiple threads at the same time without causing race conditions.

The rate limiter is implemented as a Python decorator, so it can be easily applied to any function that should be rate-limited.

## Code Snippet

Here's a snippet from the `RateLimiter` class:

```
python
self.tokens += time_passed * (self.max_requests / self.interval_seconds) # add tokens for the time passed since the last request
print(f"Tokens: {self.tokens}.")
if self.tokens > self.max_requests:
    self.tokens = self.max_requests

if self.tokens < 1:
    self.tokens -= 1
    self.last_request_time = current_time
    raise Exception("Rate limit exceeded. Please try again later.")
self.tokens -= 1
self.last_request_time = current_time
return func(*args, **kwargs)
```

## Contributing
Contributions are welcome. Please open a pull request with your changes.



