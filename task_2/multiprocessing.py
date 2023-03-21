import time

import multiprocessing
from task_2.shared_services import SharedServices


def calculate_primes():
    start_time = time.time()

    primes = [2] # initialize the list of primes with 2
    times = [0] # initialize the list of times with 0

    # Define the number of processes to use
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_processes)

    n = 3
    while time.time() - start_time < 10:    # check time limit
        # Create a list of numbers to check for primality
        numbers = [n + 2 * i for i in range(num_processes)]

        # Use multiprocessing to check primality of numbers
        results = pool.map(SharedServices().is_prime, numbers)

        # Add prime numbers to the list of primes
        for i, result in enumerate(results):
            if result:
                primes.append(numbers[i])
                times.append(time.time() - start_time)

        n += 2 * num_processes

    end_time = time.time()

    # Close the pool of processes
    pool.close()
    pool.join()

    print(f"Found {len(primes)} primes in {end_time - start_time:.2f} seconds.")
    return primes, times


def main():
    primes, times = calculate_primes()
    SharedServices().plot_primes_over_time(primes)

if __name__ == '__main__':
    main()
