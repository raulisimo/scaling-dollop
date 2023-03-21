import concurrent.futures
import time

from task_2.shared_services import SharedServices


def calculate_primes():
    start_time = time.time()

    primes = [2]    # initialize the list of primes with 2
    times = [0]     # initialize the list of times with 0
    n = 3
    while time.time() - start_time < 10:    # check time limit
        if SharedServices().is_prime(n):
            primes.append(n)
            times.append(time.time() - start_time)
        n += 2

    end_time = time.time()

    print(f"Found {len(primes)} primes in {end_time - start_time:.2f} seconds.")
    return primes, times



def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(calculate_primes)
        primes, times = future.result()
    SharedServices().plot_primes_over_time(primes)


if __name__ == '__main__':
    main()
