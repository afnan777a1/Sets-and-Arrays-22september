setx = {"Green", "blue"}
sety = {"blue", "Yellow"}

print(f"Original set elements:\n{setx}\n{sety}")


print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)

print("\nUnion of two said sets:")
setz = setx.union(sety)
print(setz)

print("\nDifference of two said sets:")
setz = setx.difference(sety)
print(setz)

print("\nSymmetric of two said sets:")
setz = setx.symmetric_difference(sety)
print(setz)