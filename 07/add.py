import time as t
target = 10
my_list = list(range(target))
my_set= set(my_list)

# print(my_list)
# print(my_set)

start  = t.time()
found_iten = target in my_list
end = t.time()
print(f"Item status : {found_iten}, List took: {end-start:.6f} seconds ")


start = t.time()
found_item = target in my_set
end = t.time()
print(f"Item status : {found_item}, Set took: {end-start:.6f} seconds ")


print(my_list)

print(my_set)  

my_list.remove(50)
print(my_list)





