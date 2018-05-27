def fibber(fib_target):
    x = 1
    y = 0
    z = 0
    while z <= fib_target:
        z = x + y
        x = y
        y = z
        if z >= fib_target:
            break
        yield z


answer = sum(filter(lambda x: x%2 ==0, fibber(4000000)))
print(answer)


