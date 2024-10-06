import os
import json
from pymongo import MongoClient, errors

# Database connection details
DB_HOST = "172.31.39.248"
DB_PORT = 8002
DB_NAME = "promociones_db"

# Function to export a collection to JSON
def export_collection_to_json(collection_name):
    # Create the directory for the collection if it doesn't exist
    directory = f"productos_db/{collection_name}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Get the collection contents
    collection = db[collection_name]
    documents = collection.find()

    # Write the collection content to JSON file
    json_file_path = f"{directory}/{collection_name}.json"
    with open(json_file_path, mode='w') as file:
        for doc in documents:
            # Remove the '_id' field if it exists
            if '_id' in doc:
                del doc['_id']
            json.dump(doc, file)
            file.write("\n")
    print(f"Exported collection {collection_name} to {json_file_path}")

# Connect to the MongoDB database with exception handling
try:
    client = MongoClient(DB_HOST, DB_PORT, serverSelectionTimeoutMS=5000)  # 5-second timeout
    db = client[DB_NAME]
    
    # Check if the connection is successful
    client.server_info()  # Will throw an exception if unable to connect
    print(f"Successfully connected to MongoDB at {DB_HOST}:{DB_PORT}")
    
    # Get the list of all collections in the database
    collections = db.list_collection_names()
    print(f"Collections in {DB_NAME}: {collections}")
    
    # Export each collection to a JSON file
    for collection_name in collections:
        export_collection_to_json(collection_name)

except errors.ServerSelectionTimeoutError as err:
    print(f"Failed to connect to MongoDB: {err}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the MongoDB connection
    client.close()

