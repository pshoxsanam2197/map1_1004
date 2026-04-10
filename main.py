# 1-m
sonlar = [1, 2, 3, 4, 5]
print(sonlar)
roy1 = list(map(lambda x: x**2, sonlar))
print(roy1)

# 2-m
sozlar = ["ali", "vali", "hasan", "husan"]
print(sozlar)
roy = list(map(lambda x: x.upper(), sozlar))
print(roy)

# 3-m
sonlar = [10, 20, 30, 40, 50]
print(sonlar)
roy = list(map(lambda x: x * 2, sonlar))
print(roy)

# 4-m
matn = ['salom', ' hello', 'privet']
print(matn)
matn1 = list(map(lambda x: len(x), matn))
print(matn1)

# 5-m
a = [1, 2, 3]
b = [4, 5, 6]
print(a)
print(b)
roy = list(map(lambda x, y: x + y, a, b))
print(roy)

# 6-m
sonlar = [-3, -1, 0, 2, -5]
print(sonlar)
roy = list(map(lambda x: abs(x), sonlar))
print(roy)

# 7-m
soz = ['aziz', 'ali', 'asad', 'diana']
print(soz)
roy = list(map(lambda x: x[::-1],soz))
print(soz)

# 8-m
roy = [3, 6, 9, 12, 15]
print(roy)
roy1 = list(map(lambda x: x ** 3, roy))
print(roy1)

# 9-m
matn = ["Python", "JavaScript", "Java", "C++", "React"]
print(matn)
roy = list(map(lambda word: word[0], matn))
print(roy)

# 10-m
son = [1, 2, 3, 4, 5, 6]
print(son)
roy = list(map(lambda x: "Juft" if x % 2 == 0 else "Toq", son))

print(roy)

# 11-m
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
print(list1)
print(list2)
roy1 = list(map(lambda x, y: x * y, list1, list2))

print(roy1)



# 1-m
word = ["Hello", "world"]
print(word)
result = " ".join(word)
print(result)

# 2-m
items = ["apple", "banana", "cherry"]
print(items)
result = ", ".join(items)
print(result)

# 3-m
chars = ["P", "Y", "T", "H", "O", "N"]
print(chars)
result = "".join(chars)

print(result)

# 4-m
roy = ["A", "B", "C"]
print(roy)
result = "-".join(roy)
print(result)

# 5-m
numbers = ['hello']

result = "*".join(map(str, numbers))
print(result)
