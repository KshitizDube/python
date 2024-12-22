'''
input = "my love is raja"
output = "ym evol si ajar"
'''

sentence = input("what is you sentence ")
word_list = sentence.split()
reverse_sentence =""
for word in word_list :
    reverse_sentence = reverse_sentence  + word[::-1] + "  "
print(reverse_sentence)
