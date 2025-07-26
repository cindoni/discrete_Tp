"""
Name: Sidney Pham
Class: Discrete Struct Comp
Section: W02
Professor: Wenyun Zhang
Program Code 1: Bubble Sort Demonstration
"""

import random


def bubble_sort(arr):
    """Implements bubble sort algorithm."""
    n = len(arr)
    
    # Outer loop for number of passes
    for j in range(n, 0, -1):
        # Inner loop for comparisons in each pass
        for i in range(1, j):
            # Compare adjacent elements and swap if needed
            if arr[i-1] > arr[i]:
                swap(arr, i-1, i)


def swap(arr, pos1, pos2):
    """Swaps two elements in an array."""
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp


def print_array(arr, title):
    """Prints an array with a title."""
    print(f"\n{title}")
    print("-" * len(title))
    print(f"Array: {arr}")
    print(f"Length: {len(arr)}")


def main():
    """Main function to demonstrate bubble sort."""
    print("BUBBLE SORT DEMONSTRATION")
    print("=" * 50)
    
    # Get number of elements from user
    try:
        n = int(input("Enter the number of elements in the array: "))
        if n <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    # Create array of random integers
    print(f"\nCreating array of {n} random integers (1-100)...")
    arr = [random.randint(1, 100) for _ in range(n)]
    
    # Print array before sorting
    print_array(arr, "ARRAY BEFORE SORTING")
    
    # Sort the array using bubble sort
    print(f"\nSorting array using Bubble Sort algorithm...")
    bubble_sort(arr)
    
    # Print array after sorting
    print_array(arr, "ARRAY AFTER SORTING")
    
    # Verify the array is sorted
    is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    print(f"\nVerification: Array is {'correctly' if is_sorted else 'NOT'} sorted.")


if __name__ == "__main__":
    main()
