# soup_of_the_day.py
#
# Download and print the UVic soups of the day.
# (Python 3 only)
#
# B. Bird - 11/30/2017


import re #Regular expression support
import urllib.request #Support for fetching webpages

#URL of the UVic "Soup of the day" page
soup_url = "https://www.uvic.ca/services/food/home/events/current/todays-soups.php"

#Fetch the webpage
#Note: We should be checking for connection errors here
#Question: How would this be written if the "with" statement were not used?
with urllib.request.urlopen(soup_url) as page:
	#Read the page data and store it in a string
	#The 'decode' step converts the raw data from read()
	#into string data.
	page_data = page.read().decode('utf-8')


#First, match <article ...> ... </article>
#Notice that re.DOTALL is used to allow matches to cross lines
for article_block in re.findall('<article.*?>(.*?)</article>', page_data, re.DOTALL):
	#The soups for each location are in a block which looks like
	#<h3><a href="...">(place_name)</a>(block of soup data)</div>
	for place, soup_block in re.findall('<h3><a href=.*?>(.*?)</a>(.*?)</div>', article_block, re.DOTALL):
		print('Location: %s'%place)
		#Inside the list of soups, each soup is contained between <li> and </li>
		for soup_name in re.findall('<li>(.*?)</li>',soup_block):
			print('    Soup: %s'%soup_name)
