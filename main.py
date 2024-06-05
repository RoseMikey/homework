# 1-masala
# def get_total_price(lst):
#     res = 0
#     for x in lst:
#         for k,v in x.items():
#             if k == 'price':
#                 res += v
#     return res
#
#
# print(get_total_price([
#   { "product": "Milk", "quantity": 1, "price": 1.50 } #dictdagi pricelarni bir biriga qo'shish
# ]))
# print(get_total_price([
#   { "product": "Milk", "quantity": 1, "price": 1.50 },
#   { "product": "Cereals", "quantity": 1, "price": 2.50 }
# ]))
# print(get_total_price([
#   { "product": "Milk", "quantity": 3, "price": 1.50 }
# ]))
# print(get_total_price([
#   { "product": "Milk", "quantity": 1, "price": 1.50 },
#   { "product": "Eggs", "quantity": 12, "price": 0.10 },
#   { "product": "Bread", "quantity": 2, "price": 1.60 },
#   { "product": "Cheese", "quantity": 1, "price": 4.50 }
# ]))
# print(get_total_price([
#   { "product": "Chocolate", "quantity": 1, "price": 0.10 },
#   { "product": "Lollipop", "quantity": 1, "price": 0.20 }
# ]))
# 2-masala
# def convert_to_number(dc2):
#     lst = []
#     lst1 = []
#     for k,v in dc2.items():
#         if type(v) == str:
#             b = int(v)
#             lst.append(b)
#     for k,v in dc2.items():
#         baz = dict(zip(k,lst))
#         lst1.append(baz)
#
#     return lst1
#
#
# print(convert_to_number({"piano": "200"}))
# print(convert_to_number({"piano": "200", "tv": "300"}))
# print(convert_to_number({"piano": "200", "tv": "300", "stereo": "400"}))
#
# 3-masala
# def expensive_orders(dc3,inst):
#     dc4 = {}
#     for k,v in dc3.items():
#         if v > inst:
#             dc4.update({k:v})
#     return dc4
# print(expensive_orders({ "a": 3000, "b": 200, "c": 1050 }, 1000))
# print(expensive_orders({ "Gucci Fur": 24600, "Teak Dining Table": 3200, "Louis Vutton Bag": 5550, "Dolce Gabana Heels": 4000 }, 20000))
# print(expensive_orders({ "Deluxe Burger": 35, "Icecream Shake": 4, "Fries": 5 }, 40))

#
# 4-masala
# def to_list(lst1):
#     lst2 = []
#     for k,v in lst1.items():
#         lst2.append([k,v])
#     return lst2
#
# print(to_list({ "a": 1, "b": 2 }))  # ➞ [["a", 1], ["b", 2]]
# print(to_list({ "shrimp": 15, "tots": 12 }))
# print(to_list({}))
#
# 5-masala
# def get_student_top_notes(lst3):
#     lst5 = []
#     lst4 = []
#
#     for x in lst3:
#         for k,v in x.items():
#             if type(v) == list:
#                 lst5.append(v)
#
#     for y in lst5:
#         lst4.append(max(y))
#
#     return lst4
#
# print(get_student_top_notes([
#   {
#     "id": 1,
#     "name": "Jacek",
#     "notes": [5, 3, 4, 2, 5, 5]
#   },
#   {
#     "id": 2,
#     "name": "Ewa",
#     "notes": [2, 3, 3, 3, 2, 5]
#   },
#   {
#     "id": 3,
#     "name": "Zygmunt",
#     "notes": [2, 2, 4, 4, 3, 3]
#   }
# ]))

# 6-masala
# def checkout(lg9):
#     res = 0
#     for x in lg9:
#         for k,v in x.items():
#             if type(v) == int and bool:
#                 res += v
#     return res
# print(checkout([
#   {"desc": "potato chips", "prc": 2, "qty": 2, "taxable": False},
#   {"desc": "soda", "prc": 3, "qty": 2, "taxable": False},
#   {"desc": "paper plates", "prc": 5, "qty": 1, "taxable": True}
# ]))
#
# 7-masala
# def count_repetitions(lst5):
#     lg = {}
#     for x in lst5:
#         b = lst5.count(x)
#         lg.update({x:b})
#
#     return lg
#
# print(count_repetitions(["cat", "dog", "cat", "cow", "cow", "cow"]))  #bir xil elementlarni countlash ms-->{ cow: 3, cat: 2, dog: 1 }
# print(count_repetitions([1, 5, 5, 5, 12, 12, 0, 0, 0, 0, 0, 0]))
# print(count_repetitions(["Infinity", "null", "Infinity", "null", "null"]))
# 8-masala
# def organize(lg11):
#     lg = {}
#     if len(lg11) == 0:
#         return {}
#
#     else:
#         b = lg11.split(",")
#         lg.update({'name': b[0]})
#         lg.update({'age': b[1]})
#         lg.update({'occupation': b[-1]})
#         return lg
# print(organize("Jameel Saeb, 15, CEO of facebook")) #--->{"name": "Jameel Saeb","age": 15,"occupation": "CEO of facebook"}
# print(organize("John Mayer, 41, Singer"))
# print(organize(""))
#
# 9-masala
# def keys_and_values(lg10):
#     lstp = []
#     lstk = []
#     lstv = []
#     for k,v in lg10.items():
#         lstv.append(v)
#         lstk.append(k)
#     lstp.append(lstk)
#     lstp.append(lstv)
#     return lstp
#
#
# print(keys_and_values({ "a": 1, "b": 2, "c": 3 }))
# print(keys_and_values({ "a": "Apple", "b": "Microsoft", "c": "Google" }))
# print(keys_and_values({ "key1": True, "key2": False, "key3": True }))
# 11-masala
# def organize(lg11):
#     lg = {}
#     if len(lg11) == 0:
#         return {}
#
#     else:
#         b = lg11.split(",")
#         lg.update({'name': b[0]})
#         lg.update({'age': b[1]})
#         lg.update({'occupation': b[-1]})
#         return lg
# print(organize("Jameel Saeb, 15, CEO of facebook")) #--->{"name": "Jameel Saeb","age": 15,"occupation": "CEO of facebook"}
# print(organize("John Mayer, 41, Singer"))
# print(organize(""))
#
# 11-masala
# def lgs12(lg):
#     res = 0
#     for x in lg:
#         for k,v in x.items():
#             if type(v) == list:
#                 res += v[-1]
#
#
#     for x in lg:
#         x.update({'notes':res})
#
#     return lg
#
# print(lgs12([
#   { 'name': "John", 'notes': [3, 5, 4]}]))  #➞ [{ name: "John", avgNote: 4 }]]))
# 12- masala
# def top_note(dc):
#     for k,v in dc.items():
#         if k == 'notes':
#             for _ in v:
#                 dc.update({'notes':max(v)})
#         return dc
# print(top_note({ "name": "John", "notes": [3, 5, 4] }))
# print(top_note({ "name": "Max", "notes": [1, 4, 6] }))
# print(top_note({ "name": "Zygmund", "notes": [1, 2, 3] }))
#
# 13-masala
# def items_purchase(lg13,dl):
#     lstp = []
#
#     for k,v in lg13.items():
#         if v > dl:
#             pass
#
#         elif dl > v:
#             lstp.append(k)
#     return lstp
#
#
# print(items_purchase({
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }, "$300"))
# print(items_purchase({
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
#   }, "$100"))
# print(items_purchase({
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"},
# "$1"))
#
# 14-masala
# def invert(dc1):
#     a = []
#     b = []
#     for x,y in dc1.items():
#         a.append(x)
#         b.append(y)
#     g = dict(zip(b,a))
#     return g
# print(invert({ "z": "q", "w": "f" }))
# print(invert({ "a": 1, "b": 2, "c": 3 }))
# print(invert({ "zebra": "koala", "horse": "camel" }))

# 15-masala
# def maximum_score(lg15):
#     res = 0
#     for x in lg15:
#         for k,v in x.items():
#             if type(v) == int:
#                 res += v
#
#     return res
#
#git init
# print(maximum_score([  #dictdagi sonlarni yig'indisi
#   { "tile": "N", "score": 1 },
#   { "tile": "K", "score": 5 },
#   { "tile": "Z", "score": 10 },
#   { "tile": "X", "score": 8 },
#   { "tile": "D", "score": 2 },
#   { "tile": "A", "score": 1 },
#   { "tile": "E", "score": 1 }
# ]))
# print(maximum_score([
#   { "tile": "B", "score": 2 },
#   { "tile": "V", "score": 4 },
#   { "tile": "F", "score": 4 },
#   { "tile": "U", "score": 1 },
#   { "tile": "D", "score": 2 },
#   { "tile": "O", "score": 1 },
#   { "tile": "U", "score": 1 }
# ]))
