l1 = [True, True, False, True, False]
l2 = [True, True, False, False, False]

correct_answer = True
for k in zip(l1, l2):
    correct_answer &= (k[0] == k[1])

print(correct_answer)
