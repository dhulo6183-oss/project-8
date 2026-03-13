
import numpy as np


def create_array():

    print("\nCreate Array")
    print("1. 1D Array")
    print("2. 2D Array")

    choice = input("Enter your choice: ")

   
    if choice == "1":
        values = input("Enter numbers separated by space: ")
        data = values.split()

        arr = np.array([float(i) for i in data])
        return arr

   
    elif choice == "2":
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        total = rows * cols
        values = input(f"Enter {total} numbers separated by space: ")
        data = values.split()

        arr = np.array([float(i) for i in data])
        arr = arr.reshape(rows, cols)

        return arr

    else:
        print("Invalid choice")
        return None



def main():

    arr = None

    while True:

        print("\n===== NumPy Analyzer =====")
        print("1. Create Array")
        print("2. Indexing / Slicing")
        print("3. Combine Arrays")
        print("4. Sort Array")
        print("5. Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        
        if choice == "1":
            arr = create_array()
            print("\nArray created:")
            print(arr)

        
        elif choice == "2":

            if arr is None:
                print("Create array first!")
                continue

            print("\nSlicing Example")
            r1 = int(input("Row start: "))
            r2 = int(input("Row end: "))
            c1 = int(input("Column start: "))
            c2 = int(input("Column end: "))

            result = arr[r1:r2, c1:c2]
            print("\nSliced Array:")
            print(result)

        
        elif choice == "3":

            if arr is None:
                print("Create array first!")
                continue

            values = input("Enter elements of another array: ")
            data = values.split()

            second = np.array([float(i) for i in data])
            second = second.reshape(arr.shape)

            combined = np.vstack((arr, second))

            print("\nCombined Array:")
            print(combined)

        
        elif choice == "4":

            if arr is None:
                print("Create array first!")
                continue

            sorted_arr = np.sort(arr)

            print("\nSorted Array:")
            print(sorted_arr)

        
        elif choice == "5":

            if arr is None:
                print("Create array first!")
                continue

            print("\nStatistics")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")

            ch = input("Enter choice: ")

            if ch == "1":
                print("Sum =", np.sum(arr))

            elif ch == "2":
                print("Mean =", np.mean(arr))

            elif ch == "3":
                print("Median =", np.median(arr))

        
        elif choice == "6":
            print("Program ended")
            break

        else:
            print("Invalid choice")



main()