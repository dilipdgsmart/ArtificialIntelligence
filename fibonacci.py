a = 0
b = 1
tot = 0
lim = int(input("Enter the upper limit: "));
print("Fibonacci Series");
print(a);
print(b);
while tot < lim:
    tot = a + b;
    print(tot,"\t");
    a = b;
    b = tot;
