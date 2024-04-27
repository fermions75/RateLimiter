# Rate Limiter

This project demonstrates the use of a thread-safe rate limiter in Python.

## Description

The rate limiter uses a token bucket algorithm to limit the rate of requests. It is thread-safe, meaning it can be used by multiple threads at the same time without causing race conditions.

The rate limiter is implemented as a Python decorator, so it can be easily applied to any function that should be rate-limited.
Also the limit per minute is configurable through the constructor parameter.

## Files

- `main.py`: This file contains the implementation of the `RateLimiter` class. The `RateLimiter` uses a token bucket algorithm to limit the rate of requests. It is not thread-safe, meaning it can not be used by multiple threads at the same time without causing race conditions. This file is to demonstrate the rate limiter in a single threaded execution.

- `thread_safe.py`: This file contains the implementation of the `RateLimiter` class. The `RateLimiter` uses a token bucket algorithm to limit the rate of requests. It is thread-safe, meaning it can be used by multiple threads at the same time without causing race conditions.

## Contributing

Contributions are welcome. Please open a pull request with your changes.


