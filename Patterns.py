# L Shape
print("L Shape\n")
n = int(input("Enter height of L shape: "))

for i in range(n):
    if i == n - 1:
        print('*' * n)  # Base of L
    else:
        print('*')      # Vertical part

# Right-sided Pyramid
print("\nRight Sided Pyramid")
for i in range(7):
    x = '*' * (i + 1)
    print(f'{x:>10}')  # Right aligned

# Left-sided Pyramid
print("\nLeft Sided Pyramid")
for i in range(1, 8):  # start from 1 to match right pyramid height
    x = '*' * i
    print(f'{x:<10}')  # Left aligned

# Normal Pyramid (Centered)
print("\nNormal Pyramid")
for i in range(1, 7):
    x = '*' * (2 * i - 1)
    print(f'{x:^11}')  # Centered in 11 spaces
