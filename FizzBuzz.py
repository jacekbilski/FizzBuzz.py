def fizz_buzz(range):
    result = []
    for x in range:
        if x % 3 == 0:
            result.append("fizz")
        elif x % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(x))
    return result


if __name__ == '__main__':
    for x in fizz_buzz(range(1, 6)):
        print(x)
