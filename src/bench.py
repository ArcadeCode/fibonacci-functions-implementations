from time import time_ns
def fibonacci_benchmark(function, t):
    class Time:
        def __init__(self):
            self.start = time_ns()
            self.end = None

        def stop(self):
            self.end = time_ns()
            return self.end - self.start

        def elapsed(self):
            return time_ns() - self.start

    time = Time()
    n = 1
    iterations = 0

    while True:
        function(n)
        iterations += 1
        
        # Vérifie si le temps écoulé a dépassé t secondes
        if time.elapsed() / 1_000_000_000 >= t:  # Convertir en secondes
            break
        n += 1

    print(f"Function {function.__name__} completed {iterations} iterations in {time.elapsed() / 1_000_000_000:.2f} seconds.")
    return iterations