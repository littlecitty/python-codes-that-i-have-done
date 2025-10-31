#39. Print a dictionary sorted by value.
a=input("enter a sentence. :").strip().split()
b={}

for i in a:
    b[i]=b.get(i,0)+1

for word, freq in sorted(b.items(), key=lambda x: x[1]):
    print(word, ":", freq)



#reverse
for word, freq in sorted(b.items(), key=lambda x: x[1], reverse=True):
    print(word, ":", freq)



#pythonic
from collections import Counter
print(dict(sorted((c := Counter(a := input("Enter sentence: ").split())).items(), key=lambda x: x[1], reverse=True)))



#pythonic oneline with strip and split
from collections import Counter
print(dict(sorted(Counter(w.strip() for w in input("enter a sentence: ").split()).items(), key=lambda x: x[1])))

