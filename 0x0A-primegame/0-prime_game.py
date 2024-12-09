#!/usr/bin/python3
"""Module for prime game solution."""


def sieveOfErathosthenes(n):
    """Find primes in a given range of numbers."""
    if n < 2:
        return []

    primes = [True] * (n + 1)

    primes[0] = primes[1] = False

    p = 2
    while (p * p <= n):
        if primes[p]:
            for mul in range(p * p, n + 1, p):
                primes[mul] = False
        p += 1

    primes = [i for i in range(n + 1) if primes[i]]
    return primes


def isWinner(x, nums):
    """Return the winner of the prime game for x rounds."""
    maria_wins = ben_wins = 0

    for n in nums:
        board_state = [True] * (n + 1)
        prime_numbers = sieveOfErathosthenes(n)
        current_player = 0

        while True:
            prime_posits = [p for p in prime_numbers if board_state[p]]

            if not prime_posits:
                break
            move = prime_posits[0]

            for i in range(move, n + 1, move):
                board_state[i] = False
            # Switch player
            current_player = 1 - current_player

        if current_player == 0:
            maria_wins += 1
        else:
            ben_wins += 1

        if maria_wins > ben_wins:
            return "Maria"
        elif ben_wins > maria_wins:
            return "Ben"
        else:
            return None
