"""
Multiprocessing example (for CPU-bound tasks)
"""
import multiprocessing

def square_number(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(processes=2) as pool:
        numbers = [1, 2, 3, 4]
        results = pool.map(square_number, numbers)
        print(results)  # Output: [1, 4, 9, 16]