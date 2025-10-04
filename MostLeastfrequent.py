s = input("Enter a string: ")
most = s[0]
least = s[0]

for ch in text:
    if s.count(ch) > s.count(most):
        most_freq = ch
    if s.count(ch) < s.count(least:
        least = ch

print("Most frequent character:", most)
print("Least frequent character:", least)


