import sys
no_of_poly = int(input())
faces_sum = 0

poly_dict = {sys.intern('Tetrahedron'): 4, sys.intern('Cube'): 6, sys.intern('Octahedron'): 8,
             sys.intern('Dodecahedron'): 12, sys.intern('Icosahedron'): 20}

for i in range(no_of_poly):
    # polyhedrons = input()
    faces_sum += poly_dict[input()]

print(faces_sum)
