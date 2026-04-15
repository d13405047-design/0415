import math

points = {
    'A': (1, 1),
    'B': (4, 4),
    'C': (6, 1)
}
P = (3, 2)

l1_distances = {}
l2_distances = {}

for name, (x, y) in points.items():
    l1 = abs(P[0] - x) + abs(P[1] - y)
    l2 = math.hypot(P[0] - x, P[1] - y)
    l1_distances[name] = l1
    l2_distances[name] = l2

print('L1 distances:')
for name in sorted(l1_distances):
    print(f'{name}: {l1_distances[name]}')

print('\nL2 distances:')
for name in sorted(l2_distances):
    print(f'{name}: {l2_distances[name]:.4f}')

nearest_l1 = min(l1_distances, key=l1_distances.get)
nearest_l2 = min(l2_distances, key=l2_distances.get)

print(f'\nNearest neighbor under L1: {nearest_l1}')
print(f'Nearest neighbor under L2: {nearest_l2}')
