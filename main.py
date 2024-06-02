# part 3 finish
# def mapping(lst):
#     vocab = {}
#     for x in lst:
#         vocab[x] = x.upper()
#     return vocab
# part 4 finish
# def count_all(string):
#     son = {
#     }
#     result = 0
#     result_num = 0
#     for x in string:
#         if x.isalpha():
#             result += 1
#         if x.isdigit():
#             result_num += 1
#     son["LETTERS"] = result
#     son["DIGITS"] = result_num
#     return son
#
# print(count_all("Hello world"))
# print(count_all("H3ll0 wor1d"))
# print(count_all("149990"))
# Task1
# input1 = input("Darth Vader / Leia / Han / R2D2\n""Who can't you remember?:")
# def relation_to_luke(input1):
#     relations = {
#         "Darth Vader": "father",
#         "Leia": "sister",
#         "Han": "brother in law",
#         "R2D2": "droid"
#     }
#     for x in relations:
#         if x == input1:
#             return f"Luke, I'm your {relations[x]}."
#     return "Luke hasn't got a relation with this name?!"
#print(relation_to_luke(input1))
# Task14
# def inver(dict):
#     dict_new ={}
#     for key,value in dict.items():
#             dict_new[value] = key
#     return dict_new
#
# print(inver({
#     "z": "q","w": "f"
# }))
# print(inver({
#     "a": 1,"b":2,"c":3
# })