
# Stack Implementation.
#1.push 2.Pop 3.Display 4.Reverse string using stack 5.Reverse stack using stack

stack = []

while True:
    print("\n----- STACK OPERATIONS -----")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String using Stack")
    print("5. Reverse Stack using Another Stack")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to push: "))
        stack.append(element)
        print("Element pushed successfully!")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack is Empty!")
        else:
            print("Popped Element:", stack.pop())

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is Empty!")
        else:
            print("Stack Elements:", stack[::-1])

    elif choice == 4:
        string = input("Enter a string: ")
        temp = []

        for ch in string:
            temp.append(ch)

        reverse = ""
        while temp:
            reverse += temp.pop()

        print("Reversed String:", reverse)

    elif choice == 5:
        if len(stack) == 0:
            print("Stack is Empty!")
        else:
            temp = []

            while stack:
                temp.append(stack.pop())

            while temp:
                stack.append(temp.pop())

            print("Stack Reversed Successfully!")
            print("Reversed Stack:", stack[::-1])

    elif choice == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")

    