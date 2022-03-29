import sys
import datetime
import requests
import pprint


# if len(sys.argv) == 3:  # podano datę na wejściu
#     API_key = sys.argv[1]
#     date_to_check = sys.argv[2]    # TODO: sprawdzić popoprawność podania daty?
# elif len(sys.argv) == 2:  # nie podano daty na wejściu
#     API_key = sys.argv[1]
#     date_to_check = datetime.datetime.now().date() + datetime.timedelta(days=1)
# else:
#     print("Błąd - wprowadzono niepoprawne dane wejściowe z std")


url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

querystring = {"q": "san francisco,us", "lat": "35", "lon": "139", "cnt": "10", "units": "metric or imperial"}

headers = {
	"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
    "X-RapidAPI-Key": sys.argv[1]
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())

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
