import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        # print(f"Time taken: {end - start:.8f}")

        return result
    return wrapper
