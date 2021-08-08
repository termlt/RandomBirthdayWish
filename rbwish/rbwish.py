'''
NOTE: If you got a wish message with some letters: XX or YY or Z
That means that you need to replace them with some age info of the person you are sending this message to.
'''

import requests
from bs4 import BeautifulSoup

def wish():
	r = requests.get('https://www.birthdaymessages.com/random/')
	soup = BeautifulSoup(r.content, 'html.parser')

	#Getting the WISH text
	form = soup.find('form')
	div = form.find('div').get_text()

	if 'BirthdayMessages.com' in div:
		print('Sorry, some error occurred. Try again!')

	else:	
		split = div.split('Category:', 1)[0]
		replace = split.replace(';', ',')
		wish = replace.replace('-', ' -')

		print(wish)
