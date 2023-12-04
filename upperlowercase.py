sentence = input("Enter a sentence : ")
wordList = sentence.split(" ")
print("This sentence has", len(wordList), "words")
digCnt = upCnt = loCnt = 0
for ch in sentence:
    if ch.isdigit():
        digCnt += 1
    elif ch.isupper():
        upCnt += 1
    elif ch.islower():
        loCnt += 1
print("This sentence contains: ")
print(digCnt,"digits")
print(upCnt,"uppercases")
print(loCnt,"lowercases")
