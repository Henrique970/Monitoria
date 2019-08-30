num = 5
fatorial = 1
print(f"{num}!:", end="")
while num >= 1:
    fatorial *= num
    print(f"{num}", end="")
    print(f" x " if num != 1 else " = ", end="")
    num -= 1
print(fatorial)
