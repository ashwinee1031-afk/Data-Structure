
# Linear Queue Implementation
#1.Enqueue 2.Dequeue 3.Display 4.Reverse queue using stack 5.Merge 2 queues 6.Check if two queues are identical.

while True:
    print("\n----- LINEAR QUEUE OPERATIONS -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue using Stack")
    print("5. Merge Two Queues")
    print("6. Check Two Queues are Identical")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element: "))
        queue.append(element)
        print("Element inserted successfully!")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is Empty!")
        else:
            print("Deleted Element:", queue.pop(0))

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is Empty!")
        else:
            print("Queue Elements:", queue)

    elif choice == 4:
        if len(queue) == 0:
            print("Queue is Empty!")
        else:
            stack = []

            while queue:
                stack.append(queue.pop(0))

            while stack:
                queue.append(stack.pop())

            print("Queue Reversed Successfully!")
            print("Reversed Queue:", queue)

    elif choice == 5:
        queue2 = []
        n = int(input("Enter number of elements in second queue: "))

        for i in range(n):
            element = int(input("Enter element: "))
            queue2.append(element)

        queue.extend(queue2)

        print("Merged Queue:", queue)

    elif choice == 6:
        queue2 = []
        n = int(input("Enter number of elements in second queue: "))

        for i in range(n):
            element = int(input("Enter element: "))
            queue2.append(element)

        if queue == queue2:
            print("Both Queues are Identical!")
        else:
            print("Both Queues are Not Identical!")

    elif choice == 7:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
