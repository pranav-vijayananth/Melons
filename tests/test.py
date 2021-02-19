code = input(">>> ")
code = list(code)
counter = 0

for i in range(0, len(code)):
    try:
        check = "".join(code[i+i:3]) == "::>"
        if check:
            counter += 1
        else:
            pass

    except IndexError:
        raise IndexError("There was an index error")

print(counter)    