import singer
import pandas as pd

LOGGER = singer.get_logger()

schema = {
	'properties': {
		'id': {'type': 'string'},
		'name': {'type': 'string'},
		'data_utc': {'type': 'string', 'format': 'data-time'},
		# space more more fields
	}
}

def main():
	url = 'https://api.spacexdata.com/v4/launches'
	df = pd.read_json(url)
	
	records = df.to_dict(orient='records')
	
	singer.write_schema('launches', schema, 'id')
	singer.write_records('launches', records)

if __name__ == '__main__':
	main()