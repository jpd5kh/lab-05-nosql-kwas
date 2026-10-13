#!/usr/bin/env python3

import logging
import os

from pymongo import MongoClient

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)

MONGODB_URL = os.getenv('MONGODB_ATLAS_URL')
MONGODB_USER = os.getenv('MONGODB_ATLAS_USER')
MONGODB_PWD = os.getenv('MONGODB_ATLAS_PWD')

def main():
	"""Connect to MongoDB Atlas, retrieve authors and their books, and display the results grouped by authors.
	"""
	try:
		url = MONGODB_URL
		username = MONGODB_USER
		pw = MONGODB_PWD
		
		log.info("Connecting to MongoDB")
	
		client = MongoClient(url, username=username, password=pw, connectTimeoutMS=200, retryWrites=True)

		log.info("Successfully connected to MongoDB")
		
		db = client.bookstore
		authors = db.authors
		books = db.books

		log.info("Selected bookstore database and authors and books collections.")

		get_authorid = {
			"_id": {"$in": ["author_001", "author_004"]}
		}

		log.info("Retrieving authors.")

		pipeline = [
			{"$match": get_authorid},
			{
				"$lookup": {
					"from": "books",
					"localField": "_id",
					"foreignField": "author_ids",
					"as": "books",
				}
			},
			{
				"$project": {
					"name": 1,
					"books.title": 1,
					"books.published_year": 1,
					"_id": 0,
				}
			},
]

		log.info("Executing MongoDB aggregation pipeline")

		joined = list(db.authors.aggregate(pipeline))

		log.info("Aggregation completed.")
		
		print(f"Authors: {len(joined)}")

		for author in joined:
			print(f"\n{author['name']}")

			for book in author["books"]:
				print(f"  {book['title']} ({book['published_year']})")

		log.info("Finished printing list of books by author.")

	except Exception:
		log.exception("Error while processing.")

	finally:
		if client is not None:
			client.close()
			log.info("MongoDB connection closed.")
		
if __name__ == "__main__":
	main()
