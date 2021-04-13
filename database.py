import pymongo

con = pymongo.MongoClient("mongodb://localhost:27017")
mydb = con["Taxi"]
mycol = mydb["passengers"]
mycol1 = mydb["Details"]
mycol2 = mydb["Ridedetails"]
