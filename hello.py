"""간단한 파이썬 예제: 인사, 구구단, 합계 계산."""


def greet(name):
    return f"안녕하세요, {name}님!"


def times_table(n):
    return [f"{n} x {i} = {n * i}" for i in range(1, 10)]


def main():
    print(greet("Claude"))
    print()
    print("[구구단 7단]")
    for line in times_table(7):
        print(line)
    print()
    numbers = list(range(1, 101))
    print(f"1부터 100까지의 합: {sum(numbers)}")


if __name__ == "__main__":
    main()
