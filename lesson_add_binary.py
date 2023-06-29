a = "11"
b = "1"
print(int(a, 2) + int(b, 2))
c = int(a,2) + int(b,2)

# e = "12"
# f = "2A"
# print(int(e, 16) + int(f, 16))
# g = int(e) + int(f)
# print(g)


binary_string = ""

while c > 1:
    remainder = c % 2
    c = c//2
    binary_string = str(remainder) + binary_string
    print(c, remainder, binary_string)

binary_string = str(c) + binary_string
print("binary string: ", binary_string)