""" Get all primes till N. """


def primes_sieve(limit):
    """ Sieve of Eratosthenes. """
    limitn = limit + 1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i * 2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

def primes_sieve2(limit):
    """ Sieve of Eratosthenes. """
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

assert list(primes_sieve(17)) == [2, 3, 5, 7, 11, 13, 17]


# But you can also binary search it (only ran a few tests but it worked on all of them):
# I'm guessing the binary search solution will be the fastest when dealing with big numbers.
def modulo(a, b):
    left = 0
    right = a
    while ( left < right ):
        m = (left + right) / 2
        if ( a - m*b >= b ):
            left = m + 1
        else:
            right = m

    return a - left*b


assert modulo(7, 2) == 1
