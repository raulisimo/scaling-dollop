import time

import matplotlib.pyplot as plt

from task_2.shared_services import SharedServices


def find_primes():
    start_time = time.time()
    num_primes = 0
    primes = []

    while time.time() - start_time < 10:
        if SharedServices().is_prime(num_primes):
            primes.append(num_primes)
        num_primes += 1

    end_time = time.time()
    return primes, end_time - start_time


def plot_primes_over_time(primes, time):
    plt.plot([i for i in range(len(primes))], primes)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Number of primes found")
    plt.title(f"Prime numbers found over {time:.2f} seconds")
    plt.show()


def main():
    primes, time = find_primes()
    SharedServices().plot_primes_over_time(primes, time)
    print(f"Found {len(primes)} primes in {time:.2f} seconds.")


if __name__ == '__main__':
    main()
