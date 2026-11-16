import time
import random
import matplotlib.pyplot as plt
import csv
import os


def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


sizes = [100, 500, 1000, 2000]
bubble_times = []
merge_times = []

for size in sizes:
    data = [random.randint(1, 10000) for _ in range(size)]

    start = time.perf_counter()
    bubble_sort(data)
    bubble_times.append(time.perf_counter() - start)

    start = time.perf_counter()
    merge_sort(data)
    merge_times.append(time.perf_counter() - start)

print("\n=== Performance Testing ===")
print("Dataset Size | Bubble Sort (seconds) | Merge Sort (seconds)")

for i in range(len(sizes)):
    print(
        f"{sizes[i]:12} | "
        f"{bubble_times[i]:21.6f} | "
        f"{merge_times[i]:19.6f}"
    )

import csv
import os

os.makedirs("results", exist_ok=True)

with open("results/performance_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Dataset Size",
        "Bubble Sort Time (seconds)",
        "Merge Sort Time (seconds)"
    ])

    for i in range(len(sizes)):
        writer.writerow([
            sizes[i],
            bubble_times[i],
            merge_times[i]
        ])

print("\nPerformance results saved to results/performance_results.csv")


plt.plot(sizes, bubble_times, marker="o", label="Bubble Sort")
plt.plot(sizes, merge_times, marker="o", label="Merge Sort")

plt.xlabel("Dataset Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Bubble Sort vs Merge Sort Performance")
plt.legend()
plt.grid(True)

plt.savefig("results/performance_comparison.png")
plt.close()

print("Performance graph saved successfully!")

#plt.savefig("results/performance_comparison.png")
#plt.show()
