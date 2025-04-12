def average(numbers: list[float]) -> float:
    total: float = 0.0
    for number in numbers:
        total += number
    return total / len(numbers)

print(average([1.1, 2.2, 3.3, 4.4, 5.5]))
