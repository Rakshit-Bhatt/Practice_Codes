import timeit, sys

ST_old=timeit.default_timer()
old_list=[int(x) for x in range(1111111)]

print(old_list)

print((sys.getsizeof(old_list)/1024), "kilobytes... KB")
print("time consumed in old: ", (timeit.default_timer() - ST_old))



print()

ST_new=timeit.default_timer()
new_list=(int(x) for x in range(10101010))

print(new_list)

print(sys.getsizeof(new_list)," bytes")
print("time consumed in new: ", (timeit.default_timer() - ST_new))
 