
import requests
def get_api():
  url = "https://api.freeapi.app/api/v1/public/randomusers/13"
  response = requests.get(url)
  data = response.json()
  if data["success"] and "data" in data:
    user_data = data["data"]
    print(data)
    gen = user_data["gender"]
    loc = user_data["location"]["state"]
    # print(user_data)
    #print(gen)
    #print(loc)
    for keys, value in user_data.items():
      print( keys,value)
    # print(loc)
    # print(gen)

get_api()
