name = "Anna"
surname = "Havula"
group = "IT-32"

d = 28
c = 6
n = d * c

print(f"{name} {surname}, {group}")
print(f"n = {d} * {c} = {n}")

divisors = []
divisors_sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
        divisors_sum += i

print("Divisors:", " ".join(str(x) for x in divisors))
print(f"Divisors count: {len(divisors)}, sum: {divisors_sum}")

# prime check with break/else
if n < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    else:
        is_prime = True

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

primes = []
for num in range(2, n + 1):
    is_num_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_num_prime = False
            break
    if is_num_prime:
        primes.append(num)

print("Primes up to", n, ":", " ".join(str(p) for p in primes))
print(f"Primes count: {len(primes)}")