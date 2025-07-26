"""
CSE 2300 - Complexity Analysis Project
Student: Sidney Pham
Assignment: Bubble Sort Timing Experiment

This program conducts timing experiments on bubble sort algorithm
by testing 1000 arrays of specified sizes and calculating average execution times.
"""

import random
import time


def bubble_sort(arr):
    """
    Implements bubble sort algorithm.
    
    Args:
        arr: List of integers to sort
        
    Returns:
        None (sorts in-place)
    """
    n = len(arr)
    
    # Outer loop for number of passes
    for j in range(n, 0, -1):
        # Inner loop for comparisons in each pass
        for i in range(1, j):
            # Compare adjacent elements and swap if needed
            if arr[i-1] > arr[i]:
                swap(arr, i-1, i)


def swap(arr, pos1, pos2):
    """
    Swaps two elements in an array.
    
    Args:
        arr: The array containing elements to swap
        pos1: Index of first element
        pos2: Index of second element
    """
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp


def timing_experiment(array_size, num_trials=1000):
    """
    Conducts timing experiment for bubble sort.
    
    Args:
        array_size: Size of arrays to test
        num_trials: Number of arrays to test (default: 1000)
        
    Returns:
        Average execution time in seconds
    """
    print(f"\nRunning Bubble Sort timing experiment...")
    print(f"Array size: {array_size}")
    print(f"Number of trials: {num_trials}")
    
    total_time = 0.0
    
    for trial in range(num_trials):
        # Create array of random integers
        arr = [random.randint(1, 10000) for _ in range(array_size)]
        
        # Start timing (after array creation)
        start_time = time.perf_counter()
        
        # Sort the array using bubble sort
        bubble_sort(arr)
        
        # End timing
        end_time = time.perf_counter()
        
        # Add to total time
        total_time += (end_time - start_time)
        
        # Progress indicator for larger experiments
        if (trial + 1) % 100 == 0:
            print(f"  Completed {trial + 1}/{num_trials} trials...")
    
    # Calculate average time
    average_time = total_time / num_trials
    
    print(f"Total time: {total_time:.6f} seconds")
    print(f"Average time per array: {average_time:.6f} seconds")
    
    return average_time


def main():
    """Main function to run timing experiments."""
    print("BUBBLE SORT TIMING EXPERIMENT")
    print("=" * 50)
    
    # Get array size from user
    try:
        n = int(input("Enter the array size for timing experiment: "))
        if n <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    # Run timing experiment
    avg_time = timing_experiment(n)
    
    # Display results
    print(f"\n" + "=" * 50)
    print("TIMING EXPERIMENT RESULTS")
    print("=" * 50)
    print(f"Algorithm: Bubble Sort")
    print(f"Array Size: {n}")
    print(f"Number of Trials: 1000")
    print(f"Average Execution Time: {avg_time:.6f} seconds")
    print(f"Average Execution Time: {avg_time * 1000:.3f} milliseconds")
    
    # Save results to file
    with open("bubble_sort_results.txt", "a") as f:
        f.write(f"Array Size: {n}, Average Time: {avg_time:.6f} seconds\n")
    
    print(f"\nResults saved to 'bubble_sort_results.txt'")


if __name__ == "__main__":
    main()
