queue = []

queue.append(10)      # Enqueue
queue.append(20)
queue.append(30)

print("Queue:", queue)

print("Dequeued:", queue.pop(0))  # Dequeue

print("Queue:", queue)






def merge_sort(a):
    if len(a) <= 1: return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return sorted(left + right)

arr = [38, 27, 43, 3, 9]
print("Before:", arr)
print("After :", merge_sort(arr))
