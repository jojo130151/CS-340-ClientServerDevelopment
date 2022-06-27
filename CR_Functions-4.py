""" 
Student: Jordan Davis
Class: CS-340-T5629 Client/Server Development
Assignment: 6-1 Milestone
Instructor: Jeff Sanford
Date: June 19, 2022

Implement Create, Read, Update, and Delete functions for animal collection in AAC database. 
This is a program to connect the database with the client-side.
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animals collection in mongoDB """
    
    
    def __init__(self, user, password, port):
        # Initializing the MongoClient 
        self.client = MongoClient("mongodb://%s:%s@localhost:%s/AAC" % (user, password, port))
        # Connet to the correct database and collection
        self.database = self.client["AAC"]
        self.collection = self.database["animals"]
    
    def create(self, userData) -> bool:
        # Implement the (C)reate in CRUD
        if userData is not None:
            # Insert the given dict data and insert it to the collection
            entry = self.collection.insert_one(userData)
            print(entry)  # Print ID just for extra verification that it insterted properly
            return True
        else:
            raise Exception("Nothing to save, because the new data is empty.")
            return False 
            
    def read(self, keyValues) -> object:
        # Implement the (R)ead in CRUD
        # Find the entries in the collection that match parameters for key and value
        cursor = self.collection.find(keyValues, {"_id": False})
        if cursor != set():
            # Iterate through the return cursor object to print each entry.
            #for x in cursor:
            #    print(x)
            return cursor
        else:
            raise Exception("Cursor returned nothing, found no results.")
            
            
    def readOne(self, keyValues) -> str:
        # Implement the (R)ead in CRUD
        # Find the entries in the collection that match parameters for key and value
        entry = self.collection.find_one(keyValues)
        entry = dumps(entry)
        return entry
            
    def update(self, lookupData, updateData):
        # Implement the (U)pdate in CRUD
        if updateData is not None:
            # Update the entries of the collection based on the given data
            updatedEntries = self.collection.update_many(lookupData, {"$set": updateData})
            # If there was a document that was updated then print the results of the update
            if updatedEntries.matched_count > 0:
                print(updatedEntries.raw_result)
        else:
            raise Exception("Can't update document, because update set perameter is empty or incorrectly formatted.")
    
    def delete(self, lookupPairs):
        # Implement the (D)elete in CRUD
        # Deletes documents from collection with the given key:value pairs
        deletes = self.collection.delete_many(lookupPairs)
        # If there were documents that were deleted then print the results of the delete
        if deletes.deleted_count > 0:
            print(deletes.raw_result)
        else:
            raise Exception("Couldn't delete file, fuction did not recognize key:value pair.")
            
    
    
           
        
    