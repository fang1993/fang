# class A:
#     def __init__(self):
#         print("A", end=" ")
#         super().__init__()
#
#
# class B:
#     def __init__(self):
#         print("B", end=" ")
#         super().__init__()
#
#
# class C(A, B):
#     def __init__(self):
#         print("C", end=" ")
#         A.__init__(self)
#         B.__init__(self)
#
#
# print("MRO:", [x.__name__ for x in C.__mro__])
# C()

# class A():
#     def __init__(self):
#         print('enter A')
#         print('leave A')
#
#
# class B(A):
#     def __init__(self):
#         print('enter B')
#         super().__init__()
#         print('leave B')
#
#
# class C(A):
#     def __init__(self):
#         print('enter C')
#         super().__init__()
#         print('leave C')
#
#
# class D(B, C):
#     def __init__(self):
#         print('enter D')
#         super().__init__()
#         print('leave D')
#
#
# d = D()
# import os
# a=os.pardir
# print(a)

# a = {u'2068210': [[u'93', u'0', 0, 0], [u'73', u'0', 0, 0]]}
#
# have_price_list = list()
# for hotel_id, supplier_info_list in a.items():
#     print(hotel_id)
#     print(supplier_info_list)
#     print(supplier_info_list[0][0])
#     have_price_list.append(hotel_id) if True in map(lambda i: int(i[0]) > 0, supplier_info_list) else ''
# print(have_price_list)

# a=[u'93', u'0', 0, 0]
# print(a)
# print(a[0])
# b=['93', '0', 0, 0]
# print(b)
# print(b[1])


def fn():
    print('aaa')

fn
def f1():
    print('bbb')

fn()
f1()






















