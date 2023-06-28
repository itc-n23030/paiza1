def f(p):
    return "yes" if p.count("yes") > p.count("no") else "no"


print(f([input() for i in range(5)]))
