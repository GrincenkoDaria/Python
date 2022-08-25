from functools import cache


book = dict()
book["apple"]= 0.67
book["milk"]= 1.49
book["avokado"]= 1.49
print(book)
print(book["avokado"])

phone_book = {}
phone_book["Jenny"] =8923345
phone_book["emergency"] = 911
print(phone_book["Jenny"])

voted = {}
def check_voter(name):
  if voted.get(name):
    print('kick them out!')
  else:
    voted[name]= True
    print('let them vote!')
    
check_voter('Tom')
check_voter('Mike')
check_voter('Tom')


cache = {}
def get_page(url):
  if cache.get(url):
    return cache[url]
  else:
    data = get_data_from_server(url)
    cache[url] = data
    return data
  
