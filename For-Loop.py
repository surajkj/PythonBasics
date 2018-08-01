# Using for loop
# words = ['hello','world','fibbonaci','The quick brown fox']
# for w in words:
#     print("Length of \""+ w + "\" is " +str(len(w)))


# Using Range 

# for i in range(6):
#     print(i)

# Parsing List in list
questions = ['What is your name?', 'Where do you live?', 'How old are you?']
answers = ['I\'m Jack', 'I live in Brisbane', 'I\'m 30 years old']

# First approach without using any inbuilt functions
i = 0
for q in questions:
    print(q,answers[i])
    i+=1

# Second approach using inbuilt function zip
for q, a in zip(questions,answers):
    print(q,a)
