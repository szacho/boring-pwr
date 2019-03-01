from vector import Vector

v1, v2, v3, v4 = Vector(), Vector(), Vector(), Vector(2)

v1.setValues([1, 1, 1])
v2.setValues([1, 2, 3])
v3.setValues([-5, 10.0])
v4.randomize()

c = 12
pairs = [(v1, v2), (v2, v1), (v3, v4), (v1, v3), (v2, c), (c, v3)]

print("Addition")
for p in pairs: 
    try:
        print('{} + {} -> {}'.format(p[0], p[1], p[0]+p[1]))
    except Exception as e:
        print('{} + {} -> {}'.format(p[0], p[1], e))

print("\nSubstraction")
for p in pairs: 
    try:
        print('{} - {} -> {}'.format(p[0], p[1], p[0]-p[1]))
    except Exception as e:
        print('{} - {} -> {}'.format(p[0], p[1], e))

print("\nMultiplication")
for p in pairs: 
    try:
        print('{} * {} -> {}'.format(p[0], p[1], p[0]*p[1]))
    except Exception as e:
        print('{} * {} -> {}'.format(p[0], p[1], e))

print("\nOther operators")
print('v1[1] -> {}'.format(v1[1]))
print('{} in {} -> {}'.format(1, v1, 1 in v1))
print('{} in {} -> {}'.format(2, v1, 2 in v1))