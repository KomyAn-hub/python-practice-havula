name = "Anna"
surname = "Havula"
group = "IT-32"

d = 28
c = 6

# print(f"{name} {surname}, {group}")
#
# print(f"Numbers from {d} to 31:", end=" ")
# count = 0
# total_sum = 0
# product = 1
# even_count = 0
# odd_count = 0
#
# for num in range(d, 32):
#     print(num, end=" ")
#     count += 1
#     total_sum += num
#     product *= num
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
# print()
# average = total_sum / count
# print(f"Count: {count}")
# print(f"Sum: {total_sum}")
# print(f"Product: {product}")
# print(f"Average: {average:.2f}")
# print(f"Even: {even_count}, odd: {odd_count}")

# while version
print(f"Numbers from {d} to 31:", end=" ")
num = d
count_w = 0
sum_w = 0
product_w = 1
even_w = 0
odd_w = 0

while num <= 31:
    print(num, end=" ")
    count_w += 1
    sum_w += num
    product_w *= num
    if num % 2 == 0:
        even_w += 1
    else:
        odd_w += 1
    num += 1

print()
average_w = sum_w / count_w
print(f"Count: {count_w}")
print(f"Sum: {sum_w}")
print(f"Product: {product_w}")
print(f"Average: {average_w:.2f}")
print(f"Even: {even_w}, odd: {odd_w}")

print("Countdown:", end=" ")
for i in range(c, 0, -1):
    print(i, end=" ")
print()