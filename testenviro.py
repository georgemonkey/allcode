numbers = [5, 12, 7, 3, 18]

def printMenu():
    print()
    print("Choose an option:")
    print("a - Add a number")
    print("r - Remove a number")
    print("p - Print the whole list")
    print("i - Print an individual number")
    print("1 - Print the sum of the list")
    print("2 - Print all even numbers")
    print("3 - Print numbers smaller than a given number")
    print("4 - Print the average")
    print("5 - Print the largest number")
    print("6 - Print the number closest to a given number")
    print("7 - Compare last number to average of the rest")
    print("q - Quit")
def closestTo(numbers, target):
    closest = numbers[0]
    minDiff = abs(target - closest)
    for num in numbers:
        if abs(num - target) < minDiff:
            closest = num
            minDiff = abs(num - target)
    return closest

while True:
    printMenu()
    choice = input("Enter your choice: ")

    if choice == 'a':
        value = int(input("Enter number to add: "))
        numbers.append(value)
    elif choice == 'r':
        value = int(input("Enter number to remove: "))
        if value in numbers:
            numbers.remove(value)
        else:
            print("That number is not in the list.")
    elif choice == 'p':
        print("The list is:", numbers)
    elif choice == 'i':
        index = int(input("Enter the index of the number: "))
        if 0 <= index < len(numbers):
            print("Number at index", index, "is", numbers[index])
        else:
            print("Invalid index.")
    elif choice == '1':
        print("Sum:", sum(numbers))
    elif choice == '2':
        print("Even numbers:", [n for n in numbers if n % 2 == 0])
    elif choice == '3':
        limit = int(input("Enter a number: "))
        print("Numbers smaller than", limit, ":", [n for n in numbers if n < limit])
    elif choice == '4':
        average = sum(numbers) / len(numbers)
        print("Average:", average)
    elif choice == '5':
        print("Largest number:", max(numbers))
    elif choice == '6':
        target = int(input("Enter a target number: "))
        print("Closest number to", target, "is", closestTo(numbers, target))
    elif choice == '7':
        if len(numbers) < 2:
            print("Not enough numbers to compare.")
        else:
            last = numbers[-1]
            avgOfRest = sum(numbers[:-1]) / (len(numbers) - 1)
            if last > avgOfRest:
                print("The last number is bigger than the average of the others.")
            elif last < avgOfRest:
                print("The last number is smaller than the average of the others.")
            else:
                print("The last number is equal to the average of the others.")
    elif choice == 'q':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")