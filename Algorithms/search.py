from collections import deque


graph = {}
graph["you"]= ["alice", "bob", "claire"]
graph["bob"]= ["anuj", "peggy"]
graph["alice"]= ["peggy"]
graph["claire"]= ["thom", "jonny"]
graph["anuj"]= []
graph["peggy"]= []
graph["thom"]= []
graph["jonny"]= []

graph
def person_is_seller(name):
  return name[0] == "m" or name[0] == "a" or name[0] == "n" or name[0] == "g" or name[0] == "o" or name[-1] == "m"

def search(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = []
  while search_queue:
    person = search_queue.popleft()
    if not person in searched:
      if person_is_seller(person):
        print(person + " is a mango seller!")
        return True
      else:
        search_queue += graph[person]
        searched.append(person)
  return False

search("you")