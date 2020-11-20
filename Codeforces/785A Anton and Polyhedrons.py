n = int(input())
count = 0
for i in range(n):
    s = str(input())
    if s == "Tetrahedron":
        count += 4
    elif s == "Cube":
        count += 6
    elif s == "Octahedron":
        count += 8
    elif s == "Dodecahedron":
        count += 12
    elif s == "Icosahedron":
        count += 20

print(count)