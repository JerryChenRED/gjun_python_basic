from collections import deque, Counter, namedtuple

deque_1 = deque([1, 2, 3])
deque_1.append(4)
deque_1.extend([5, 6, 7])
print(deque_1)
list_a = ['a'] + ['b', 'c', 'd']
deque_1.appendleft(0)
deque_1.extendleft([10, 9, 8])
deque_1 = [11, 12, 13] + list(deque_1)
print(deque_1)

deque_2 = deque(['a', 'b', 'c', 'd', 'e'], maxlen = 7)
deque_2.rotate(3)
print(deque_2)
deque_2.extendleft(['f', 'g', 'h'])
print(deque_2)


major_tuple = namedtuple("major_element_and_count", ["major_element", "count"])

m_1 = major_tuple(major_element=9, count=100)
m_2 = major_tuple(major_element=15, count=78)

print(m_1)
print(m_2)