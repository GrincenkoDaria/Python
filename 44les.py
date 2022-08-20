import json
from random import randint
str_json ="""{
"response": {
	"count": 5961888,
	"items": [{
		"first_name": "Misha",
		"id": 531956548,
		"last_name": "Musaev",
		"can_access_closed": true

	}, {
		"first_name": "Diana",
		"id": 641956548,
		"last_name": "Shavcenko",
		"can_access_closed": true

	}]
}
}"""

data = json.loads(str_json)
print(data["response"]["count"])
for item in data['response']['items']:
  print(item)
  
for item in data['response']['items']:
  del item["id"]
  item['likes']= randint(100,2000)
print(data['response']['items'])


new_json = json.dumps(data, indent=2)
print(new_json)

print(json.loads(new_json))
with open("my.json","w") as file:
	json.dump(data,file, indent=3)