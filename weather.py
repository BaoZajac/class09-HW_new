import sys
import datetime
import requests
import pprint


if len(sys.argv) == 3:  # podano datę na wejściu
    API_key = sys.argv[1]
    date_to_check = sys.argv[2]    # TODO: sprawdzić popoprawność podania daty?
    print(date_to_check)
elif len(sys.argv) == 2:  # nie podano daty na wejściu
    API_key = sys.argv[1]
    date_to_check = datetime.datetime.now().date() + datetime.timedelta(days=1)
    print(date_to_check)
else:
    print("Błąd - wprowadzono niepoprawne dane wejściowe z std")


url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"
params = {"q": "san francisco,us", "lat": "35", "lon": "139", "cnt": "10", "units": "metric or imperial"}
headers = {"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com", "X-RapidAPI-Key": sys.argv[1]}

response = requests.get(url, headers=headers, params=params)

from datetime import datetime    #TODO: dlaczego nie zaciąga tu fromtimestamp z import datetime?
pprint.pprint(response.json())

user_object = (response.json())
for date in user_object["list"]:
    if datetime.fromtimestamp(date["dt"]).date() == date_to_check:
        print("yes!")
        print(user_object["list"][]["pop"])
# date = (user_object["list"][0]["dt"])
# print(datetime.fromtimestamp(date).date())




# NIEDZIAŁAJĄCE API ---v----------------------------------------------------------------------

# response = requests.get(url)
# # r = requests.post(url, data={"key":"value"})
# # print(r.text)
# user_object = response.json()
# # pprint.pprint(user_object["results"][0])
# # look = user_object.get("results")     #("results")
# # print(look)
#
#
# response = requests.get(url)
# user_object = response.json()
# print(len(user_object))
#
# pprint.pprint(user_object)
# # pprint.pprint(user_object["repository"][0])
# # pprint.pprint(user_object[0])
# # pprint.pprint(user_object[0].keys())

# NIEDZIAŁAJĄCE API ---^-----------------------------------------------------------------------
