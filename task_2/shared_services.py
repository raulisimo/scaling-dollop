import math

from matplotlib import pyplot as plt


class SharedServices:

    def is_prime(self, n):
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            # Check odd numbers from 3 up to sqrt(n)
            for i in range(3, int(math.sqrt(n))+1, 2):
                if n % i == 0:
                    return False
            return True

    def plot_primes_over_time(self, primes):
        plt.plot([i for i in range(len(primes))], primes)
        plt.xlabel("Time (seconds)")
        plt.ylabel("Number of primes found")
        plt.title('Number of primes over time')

        plt.show()
