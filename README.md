# Rate Limiter

This project demonstrates the use of a thread-safe rate limiter in Python.

## Description

The rate limiter uses a token bucket algorithm to limit the rate of requests. It is thread-safe, meaning it can be used by multiple threads at the same time without causing race conditions.

The rate limiter is implemented as a Python decorator, so it can be easily applied to any function that should be rate-limited.
Also the limit per minute is configurable through the constructor parameter.

## Files

- `main.py`:  This file uses the `RateLimiter` class to a method of a class `Calculator`. A request is sent every 5 seconds to demonstrate the rate limiter. The rate limit parameters are set in the constructor.

- `rate_limiter.py`: This file contains the implementation of the `RateLimiter` class. The `RateLimiter` uses a token bucket algorithm to limit the rate of requests. It is thread-safe, meaning it can be used by multiple threads at the same time without causing race conditions.

- `thread_safe.py`: Thread safe test has been demonstrated in this file for the `RateLimite` class using multiple threads. 

## Contributing

Contributions are welcome. Please open a pull request with your changes.


