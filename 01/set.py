# class Value:
#     def __init__(self, data, _children = ()):
#         self.data = data
#         self._prev  = set(_children)
        
#     def __repr__(self):
#         return f"Value(data={self.data})"
    
#     def __add__(self, other):
#         return Value(self.data + other.data, (self, other))
        

# a = Value(10)
# print(a)
# print(a._prev)

# b = Value(20)
# print(b)
# print(b._prev)

# c = a + b

# print(c)
# print(c._prev)

new = (1,2)

my_set = set(new)
print(my_set)

