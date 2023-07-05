def hashTable():
  phone_book = dict()
  phone_book['parth'] = 123835
  phone_book['takkar'] = 123833455
  return phone_book


cache = {}
def get_data(url):
  if (cache.get(url)):
    return cache[url]
  else:
    data =get_data_from_server(url)
    cache[url] = data
    return data

def get_data_from_server(url):
  return 'data for: ' + str(url)


table = hashTable()
parth = table.get('parth')
takkar = table.get('takkar')

print(hashTable())
print(parth)
print(takkar)



