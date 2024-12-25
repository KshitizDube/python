listt_from_user = int(input("How many words do you want to enter : "))
second_list_of_words = [] 
for i in range(listt_from_user):
    word_user_gave = input("please enter your word : ")
    if "b" not in  word_user_gave:
        second_list_of_words.append(word_user_gave)
print(second_list_of_words)