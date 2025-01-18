#1 O(n)
# lst = [1,2,3,4,5]
# sum = sum(lst)
# print(sum)

#2 O(n)
# lst = [5,2,8,1,4]
# min = min(lst)
# print(min)

#3 O(1)
# def a(n):
#     return n>0 and (n&(n-1)) == 0
# n = 16
# print(n, a(n))

#4 O(n + m)
# lst1 = [1,2,3,4]
# lst2 = [3,4,5,6]
# a = set(lst1) & set(lst2)
# print(print("Количество совпадений:", len(a)))

#5 O(n)
# from collections import Counter

# lst = [1, 2, 2, 3, 3, 3]
# counter = Counter(lst)
# for number, count in counter.items():
#     print(f"{number} встречается {count} раз(а)")