"""
CSE 2300 - Complexity Analysis Project
Student: Sidney Pham
Assignment: Comprehensive Timing Experiment

"""

import random
import time
import csv
from datetime import datetime


def bubble_sort(arr):
    """Implements bubble sort algorithm."""
    n = len(arr)
    for j in range(n, 0, -1):
        for i in range(1, j):
            if arr[i-1] > arr[i]:
                swap(arr, i-1, i)


def selection_sort(arr):
    """Implements selection sort algorithm."""
    n = len(arr)
    for j in range(n):
        i_min = j
        for i in range(j + 1, n):
            if arr[i] < arr[i_min]:
                i_min = i
        if i_min != j:
            swap(arr, j, i_min)


def swap(arr, pos1, pos2):
    """Swaps two elements in an array."""
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp


def run_timing_experiment(sort_function, sort_name, array_size, num_trials=1000):
    """
    Runs timing experiment for a given sorting algorithm.
    
    Args:
        sort_function: The sorting function to test
        sort_name: Name of the sorting algorithm
        array_size: Size of arrays to test
        num_trials: Number of trials to run
        
    Returns:
        Average execution time in seconds
    """
    print(f"\nRunning {sort_name} timing experiment...")
    print(f"Array size: {array_size}")
    print(f"Number of trials: {num_trials}")
    
    total_time = 0.0
    
    for trial in range(num_trials):
        # Create array of random integers
        arr = [random.randint(1, 10000) for _ in range(array_size)]
        
        # Start timing (after array creation)
        start_time = time.perf_counter()
        
        # Sort the array
        sort_function(arr.copy())  # Use copy to avoid modifying original
        
        # End timing
        end_time = time.perf_counter()
        
        # Add to total time
        total_time += (end_time - start_time)
        
        # Progress indicator
        if (trial + 1) % 200 == 0:
            print(f"  Completed {trial + 1}/{num_trials} trials...")
    
    # Calculate average time
    average_time = total_time / num_trials
    
    print(f"Total time: {total_time:.6f} seconds")
    print(f"Average time per array: {average_time:.6f} seconds")
    
    return average_time


def main():
    """Main function to run comprehensive timing experiments."""
    print("COMPREHENSIVE SORTING ALGORITHMS TIMING EXPERIMENT")
    print("=" * 70)
    print(f"Student: Sidney Pham")
    print(f"Course: CSE 2300")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Test parameters
    array_sizes = [500, 2500, 5000]
    num_trials = 1000
    
    # Store results
    results = []
    
    print(f"\nTesting both algorithms on array sizes: {array_sizes}")
    print(f"Number of trials per test: {num_trials}")
    print(f"Total experiments: {len(array_sizes) * 2} = {len(array_sizes) * 2 * num_trials} individual sorts")
    
    # Run experiments for each array size
    for size in array_sizes:
        print(f"\n" + "=" * 50)
        print(f"TESTING ARRAY SIZE: {size}")
        print("=" * 50)
        
        # Test Bubble Sort
        bubble_time = run_timing_experiment(bubble_sort, "Bubble Sort", size, num_trials)
        
        # Test Selection Sort
        selection_time = run_timing_experiment(selection_sort, "Selection Sort", size, num_trials)
        
        # Store results
        results.append({
            'Array Size': size,
            'Bubble Sort (seconds)': bubble_time,
            'Selection Sort (seconds)': selection_time,
            'Bubble Sort (ms)': bubble_time * 1000,
            'Selection Sort (ms)': selection_time * 1000
        })
        
        # Display comparison for this size
        print(f"\n--- COMPARISON FOR SIZE {size} ---")
        print(f"Bubble Sort:    {bubble_time:.6f} seconds ({bubble_time * 1000:.3f} ms)")
        print(f"Selection Sort: {selection_time:.6f} seconds ({selection_time * 1000:.3f} ms)")
        
        if bubble_time < selection_time:
            ratio = selection_time / bubble_time
            print(f"Bubble Sort is {ratio:.2f}x faster for size {size}")
        else:
            ratio = bubble_time / selection_time
            print(f"Selection Sort is {ratio:.2f}x faster for size {size}")
    
    # Display final results summary
    print(f"\n" + "=" * 70)
    print("FINAL RESULTS SUMMARY")
    print("=" * 70)
    
    print(f"{'Array Size':<12} {'Bubble Sort (ms)':<18} {'Selection Sort (ms)':<20} {'Faster Algorithm':<15}")
    print("-" * 70)
    
    for result in results:
        size = result['Array Size']
        bubble_ms = result['Bubble Sort (ms)']
        selection_ms = result['Selection Sort (ms)']
        faster = "Bubble Sort" if bubble_ms < selection_ms else "Selection Sort"
        
        print(f"{size:<12} {bubble_ms:<18.3f} {selection_ms:<20.3f} {faster:<15}")
    
    # Save results to CSV file
    csv_filename = f"sorting_experiment_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Array Size', 'Bubble Sort (seconds)', 'Selection Sort (seconds)', 
                     'Bubble Sort (ms)', 'Selection Sort (ms)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    print(f"\nResults saved to: {csv_filename}")
    
    # Generate analysis
    print(f"\n" + "=" * 70)
    print("COMPLEXITY ANALYSIS")
    print("=" * 70)
    print("Both algorithms have O(n²) time complexity.")
    print("Expected behavior: Execution time should increase quadratically with input size.")
    print("\nTheoretical time ratios for quadratic growth:")
    print(f"Size 2500 vs 500: {(2500/500)**2:.1f}x slower")
    print(f"Size 5000 vs 500: {(5000/500)**2:.1f}x slower")
    print(f"Size 5000 vs 2500: {(5000/2500)**2:.1f}x slower")
    
    print(f"\nActual time ratios observed:")
    bubble_500 = results[0]['Bubble Sort (ms)']
    bubble_2500 = results[1]['Bubble Sort (ms)']
    bubble_5000 = results[2]['Bubble Sort (ms)']
    
    print(f"Bubble Sort - Size 2500 vs 500: {bubble_2500/bubble_500:.1f}x")
    print(f"Bubble Sort - Size 5000 vs 500: {bubble_5000/bubble_500:.1f}x")
    print(f"Bubble Sort - Size 5000 vs 2500: {bubble_5000/bubble_2500:.1f}x")
    
    selection_500 = results[0]['Selection Sort (ms)']
    selection_2500 = results[1]['Selection Sort (ms)']
    selection_5000 = results[2]['Selection Sort (ms)']
    
    print(f"Selection Sort - Size 2500 vs 500: {selection_2500/selection_500:.1f}x")
    print(f"Selection Sort - Size 5000 vs 500: {selection_5000/selection_500:.1f}x")
    print(f"Selection Sort - Size 5000 vs 2500: {selection_5000/selection_2500:.1f}x")
    
    print(f"\nExperiment completed successfully!")
    print(f"Total runtime: Approximately {(len(array_sizes) * 2 * num_trials * max(array_sizes) * 0.000001):.1f} minutes")


if __name__ == "__main__":
    main()
