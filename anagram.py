from collections import Counter as counter
a = input()
b = input()
p = dict(counter(a))
print(p)
q = dict(counter(b))
print(q)
count = 0
for key,pair in p.items():
    if key not in q.keys():
        count += pair
    else:
        value_p = p[key]
        value_q = q[key]
        value = max(value_p,value_q) - min(value_p,value_q)
        count += value

for key,pair in q.items():
    if key not in p.keys():
        count += pair

print(count)
