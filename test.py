word = "I am fine"
n = len(word)
word1 = word.upper()
word2 = word.lower()
converted_word = ""
for i in range(n):
    if i%2==0:
        converted_word += word2[i]
    else:
        converted_word += word1[i]
print(converted_word)

# x = "Kacha badam"
# for i in range(len(x)-1,-1,-1):
#     print(i)
#     print(x[i])

n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()

# n = int(input("enter number"))
# sum = 0
# for num in range(1,n+1,1):
#     sum = sum + num
# print("sum of first ", n ,"numbers is :", sum)
# average = sum / n
# print("average of ",n,"number is:",average)