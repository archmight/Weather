import requests
import os


def try_to_create_dictionary():
	pass #todos


def find_in_dictionary_weather(city):
	pass #todos


def check_city_in_dictionary(city):
	try_to_create_dictionary()
	weather = find_in_dictionary_weather(city)
	return weather


def get_dict_data_from_json(city, weather_api):
	link = "https://api.weatherbit.io/v2.0/current?city={}&key={}".format(city, weather_api)
	request = requests.get(link).json()
	forecast = request["data"]
	dict = {}
	for _ in forecast:
		dict = _

	result_dictionary  = {city:{"description": dict["weather"]["description"], "temperature": dict["temp"]}}
	return result_dictionary

def write_weather_data_into_dictionary(dict_data):
	pass #todos

def get_weather_by_api(city,weather_api):
	dict_request = get_dict_data_from_json(city,weather_api)
	write_weather_data_into_dictionary(dict_request)
	print(dict_request)


def city_and_weather(city = "Moscow"):
	dictionary_scaning = check_city_in_dictionary(city)
	
	if dictionary_scaning != None:
		return

	print("print weather api")
	weather_api = input()
	get_weather_by_api(city, weather_api)


def main():
	print("print city name:")
	city = input()
	city_and_weather(city);


if __name__ == '__main__':
	main();
