from django.test import TestCase, Client

class ApiTestCase(TestCase):

	maxDiff = None

	def test_country_data(self):
		client = Client()

		test_url = '/v1/country/Finland'

		test_response = {
			"data": [
				{
					"countryName": "Finland",
					"rank": 1,
					"ladderScore": 7.842,
					"healthyLifeExpectancy": 72,
					"generosity": -0.098,
					"gdp": 10.775
				}
			]
		}

		response = client.get(test_url)
		self.assertEqual( response.status_code, 200 )
		self.assertEqual( response.json(), test_response)

	def test_ladder_range_data(self):
		client = Client()

		test_url = '/v1/score-range/?from=7.5&to=7.8'

		test_response = {
			"data": [
				{
					"countryName": "Finland",
					"rank": 1,
					"ladderScore": 7.842,
					"healthyLifeExpectancy": 72.0,
					"generosity": -0.098,
					"gdp": 10.775
				},
				{
					"countryName": "Denmark",
					"rank": 2,
					"ladderScore": 7.62,
					"healthyLifeExpectancy": 72.7,
					"generosity": 0.03, "gdp": 10.933
				},
				{
					"countryName": "Switzerland",
					"rank": 3, 
					"ladderScore": 7.571, 
					"healthyLifeExpectancy": 74.4, 
					"generosity": 0.025, 
					"gdp": 11.117
				}, 
				{
					"countryName": "Iceland", 
					"rank": 4, 
					"ladderScore": 7.554, 
					"healthyLifeExpectancy": 73.0, 
					"generosity": 0.16, 
					"gdp": 10.878
				}
			]
		}
	
		response = client.get(test_url)
		self.assertEqual( response.status_code, 200 )
		self.assertEqual( response.json(), test_response)
