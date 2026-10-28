# Page replacement algorithms

Simulates three classic page replacement algorithms on a random reference string and counts the page
faults each one causes.

- **FIFO:** replaces the page that has been in memory longest
- **LRU:** replaces the page used least recently
- **Optimal:** replaces the page that won't be needed for the longest time (the theoretical best)

Operating systems assignment, University of Cape Town, 2023.

## Run

```bash
python3 paging.py 4
```

The argument is the number of page frames (1 to 7). Each run generates a new reference string of 50
pages numbered 0 to 9 and prints the fault count for each algorithm:

```
FIFO: 18 Page Faults.
LRU: 15 Page Faults.
OPT: 12 Page Faults.
```
