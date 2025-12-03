lines = open("input.txt", "r").readlines()

# https://www.geeksforgeeks.org/dsa/largest-number-possible-after-removal-of-k-digits/
def maxnumber(n, k):
    for i in range(0, k):
        ans = 0
        i = 1
        while n // i > 0:
            temp = (n//(i * 10))*i + (n % i)
            i *= 10
            if temp > ans:
                ans = temp
        n = ans        
    return ans;

total = 0
for line in lines:
    line = line.strip()
    total += maxnumber(int(line), len(line)-12)
print(total)