def find_nth_term(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    else:
        return find_nth_term(n-2) + find_nth_term(n-1)


def fibo_series(n):
    series = []
    for i in range(0, n):
        result = find_nth_term(i)
        series.append(result)
        print(series)


range_ser = int(input("enter a range: "))
fibo_series(range_ser)
