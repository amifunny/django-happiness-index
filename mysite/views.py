from django.http import HttpResponse,JsonResponse
import json

from . import df

def country_data(request, country_name):

	# Map dataframe columns to expected response keys
	column_to_key_map = {
		"Country name": "countryName",
		"rank": "rank",
		"Ladder score": "ladderScore",
		"Healthy life expectancy": "healthyLifeExpectancy",
		"Generosity": "generosity",
		"Logged GDP per capita": "gdp"
	}

	# Filter rows for given `country_name`
	country_df = df.loc[(df['Country name'] == country_name)]
	# Create new column `rank` from dataframes's index
	# Increment by 1 to start `rank` with 1 instead of 0
	country_df.loc[:,"rank"] = country_df.index+1

	# Select only columns given in map
	country_df = country_df[list(column_to_key_map.keys())]
	# Rename columns to expected response keys
	country_df = country_df.rename(columns=column_to_key_map)
	# Get rows value as array of dicts
	country_dict = country_df.to_dict(orient='records')

	return JsonResponse(
		{
			"data":country_dict
		}
	)

def ladder_range_data(request):

	# Map dataframe columns to expected response keys
	column_to_key_map = {
		"Country name": "countryName",
		"rank": "rank",
		"Ladder score": "ladderScore",
		"Healthy life expectancy": "healthyLifeExpectancy",
		"Generosity": "generosity",
		"Logged GDP per capita": "gdp"
	}

	try:
		# Convert string parameters to float
		range_from = float( request.GET.get('from') )
		range_to = float( request.GET.get('to') )
	except Exception as e:
		return HttpResponse(
			"Invalid Argument.`from` and `to` query arguments are required and must be floating numbers."
		)

	# Filter rows with "Ladder score" between `range_from` and `range_to
	ladder_range_df = df[ (range_from<df['Ladder score'].round(1)) & (df['Ladder score'].round(1)<=range_to)]
	# Create new column `rank` from dataframes's index
	# Increment by 1 to start `rank` with 1 instead of 0
	ladder_range_df.loc[:,"rank"] = ladder_range_df.index+1

	# Select only columns given in map
	ladder_range_df = ladder_range_df[list(column_to_key_map.keys())]
	# Rename columns to expected response keys
	ladder_range_df = ladder_range_df.rename(columns=column_to_key_map)
	ladder_range_dict = ladder_range_df.to_dict(orient='records')
	
	return JsonResponse(
		{
			"data": ladder_range_dict
		}
	)