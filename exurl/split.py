from urllib.parse import urlsplit,parse_qs

# Function take url and return params with this format => {'paramName': ['value'], 'age': ['33'], 'name': ['dekart']}
def query(url):
	query = urlsplit(url).query
	params = parse_qs(query)
	return params

# Function take query format data and return just params value in list
def params_value(dct):
	params_value_list = []
	for param,value in dct.items():
		params_value_list.append(value[0])
	return params_value_list

# Function take [url, replacedData] and return urls split
def split_url(url, replaceMe):
	split_urls_list = []
	params_value_list = []

	params_value_url = params_value(query(url))
	# [2]- for loop to enter in params value and replace
	for param_value in params_value_url:
		chob = url.replace(param_value, replaceMe)
		split_urls_list.append(chob)

	return split_urls_list

# Function take [url, replacedData] and return urls split
def split_urls(urls, replaceMe):
	split_urls_list = []
	params_value_list = []

	# [1]- for loop to enter in urls list
	for url in urls:
		params_value_url = params_value(query(url))
		# [2]- for loop to enter in params value and replace
		for param_value in params_value_url:
			chob = url.replace(param_value, replaceMe)
			split_urls_list.append(chob)

	return split_urls_list