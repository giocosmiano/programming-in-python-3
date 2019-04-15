numbers = []

while True:
    line = input("enter a number or Enter to finish: ")
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        numbers += [number]
    else:
        break

count = len(numbers)

if count:
    total = sum(numbers)
    print("numbers:", numbers)
    print("count =", count, "sum =", total,
          "lowest =", min(numbers), "highest =", max(numbers),
          "mean =", total / count)
