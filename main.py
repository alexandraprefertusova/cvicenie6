def main():
    print("Hello from cviko6!")


if __name__ == "__main__":
    main()



counter = 10


def increment_global():
    global counter
    counter = counter + 1
    return counter
print(increment_global())  # 11
print(counter)