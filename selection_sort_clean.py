"""
Name: Sidney Pham
Class: Discrete Struct Comp
Section: W02
Professor: Wenyun Zhang
Program Code 2: Selection Sort Demonstration
"""

import random


def selection_sort(arr):
    """Implements selection sort algorithm."""
    n = len(arr)
    
    # Traverse through all array elements
    for j in range(n):
        # Find the minimum element in remaining unsorted array
        i_min = j
        
        for i in range(j + 1, n):
            if arr[i] < arr[i_min]:
                i_min = i
        
        # Swap the found minimum element with the first element
        if i_min != j:
            swap(arr, j, i_min)


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
    """Main function to demonstrate selection sort."""
    print("SELECTION SORT DEMONSTRATION")
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
    
    # Sort the array using selection sort
    print(f"\nSorting array using Selection Sort algorithm...")
    selection_sort(arr)
    
    # Print array after sorting
    print_array(arr, "ARRAY AFTER SORTING")
    
    # Verify the array is sorted
    is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    print(f"\nVerification: Array is {'correctly' if is_sorted else 'NOT'} sorted.")


if __name__ == "__main__":
    main()
