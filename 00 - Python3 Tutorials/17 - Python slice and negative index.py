# -*- coding: utf-8 -*-

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
c = '0123456789'

print("a[:] = " + str(a[:]))
print("a[slice(0,5)] = " + str(a[slice(0,5)]))
print("a[0:5] = " + str(a[0:5]))
print()
print("b[:] = " + str(b[:]))
print("b[4:] = " + str(b[4:]))
print("b[:6] = " + str(b[:6]))
print()
print("c[:] = " + str(c[:]))
print("c[4:] = " + str(c[4:]))
print("c[:3] = " + str(c[:3]))
print()
print(a[:])
print("a[0:9:2] = " + str(a[0:9:2]))
print("a[::2] = " + str(a[::2]))
print()
print(c[:])
print("c[::-1] = " + str(c[::-1]))
print("c[::-2] = " + str(c[::-2]))
print("c[:-4:-1] = " + str(c[:-4:-1]))
print("c[-3::-1] = " + str(c[-3::-1]))








