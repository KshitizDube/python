listt_from_user = int(input("How many words do you want to enter : "))
second_list_of_words = [] 
third_list = []
B_list =[]
for i in range(listt_from_user):
    word_user_gave = input("please enter your word : ")
    second_list_of_words.append(word_user_gave)
print(second_list_of_words)
for p in second_list_of_words:
    if "b" not in p:
        third_list.append(p)
    else:
        B_list.append(p)
print(f"This is the lists with no words containing b, {third_list}")
print(B_list)
    