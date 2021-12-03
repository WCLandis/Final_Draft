#William Landis
#CIS245-340
#Final Project First Draft
#12/04/2021

#For my draft, I substituted the weather web page for a dictionary to verify city and zip code.
weather = {'Greenville' : '92', 'New York' : '75', 'Boston' : '67', 'Los Angeles' : '79', 'San Antonio' : '86'}

def getWeather():
	print('The current weather in your city/zip is: ')
	moreWeather = input('Would you like to get another weather report? (yes or no) ')

	if moreWeather == 'yes':
		main_menu()

	if moreWeather == 'no':
		print('Thanks for using my weather report! ')

def getWebdata():
	print('Attempting to retrieve web data... ')
	webData = 'yes'
	
	if webData == 'yes':
		print('Connection to web service established \n')
		getWeather()
	
	elif webData == 'no':
		print('Connection to web wervice could not be established, please try again \n ')
		main_menu()


def main_menu():
#I got my API key today, which I included here
	api_key = '94cfc8e542fc70b6db1970d4e9338019'

	while True:
		userCity = input('Please enter the name of your city \n')
		
		if userCity in weather:
			getWebdata()
			break
#I found the isdigit method to validate whether the user input is letters or numbers.
		elif userCity.isdigit() == True:
			print('This is not a valid city, please try again! \n ')

		elif weather == 'quit' or 'q':
			break
#Here is the API URL from openweathermap.org
	weather_url = 'api.openweathermap.org/data/2.5/weather?q='+ userCity + '&appid=' + api_key

print('The following program will retrieve current weather ')			
main_menu()
		

