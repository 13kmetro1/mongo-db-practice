import sys


#TODO: Write your username and answer to each query as a string in the return statements 
# in the functions below. Do not change the function names. 

# Write your queries using multi-line strings and use proper indentation to increase readability.
# For Q6 & Q7 write your map/reduce code as multi-line string. For example:
# 
# def query6():
#     return """
# 
#             var mapFunction1 = function() {
#                ...
#             }
# 
#             var reduceFunction1 = function(a, b) {
#                return ...
#             }
# 
#             db.countries.mapReduce(mapFunction1, reduceFunction1, {
#                ...
#             })
#           """

# Your result should have the attributes in the same order as appeared in the sample answers. 

# Make sure to test that python prints out the strings correctly.

# usage: python hw6.py

def username():
	return "Kmetro"
    
def query1():
    return """
     db.countries.find({$or:[{"area":{$gt: 10000000}},{"area":{$lt: 10}}]},{"_id":0,"area":1,"name":"$name.common"}).pretty() 
          """ 

def query2():
    return """
            db.countries.find({"translations.ita.official": "Repubblica di Malta"},{"_id": 0, "capital": 1}).pretty()
           """
            
def query3():
    return """
            db.countries.find({"latlng.0":{$gte: 40,$lte:45},"latlng.1":{$gte: 10,$lte:20} },{"_id":0,"capital":1,"name":"$name.common"}).pretty()
           """ 

def query4():
    return """
            db.countries.aggregate([ { $project:{"_id":0,"name":"$name.common",numberOfCurrencies:{$size: { "$ifNull": [ "$currency", [] ] } } } }, { $sort:{"numberOfCurrencies":-1,"name":1} },{ $limit : 5 } ])
           """

def query5():
    return """
            db.countries.aggregate([ {$group:{_id:"$subregion","value":{$sum:"$area"}}}])
           """ 

def query6():
    return """
            var mapFunction1 = function() {emit(this.subregion, this.area);}
            var reduceFunction1 = function(subregion, area) {return Array.sum(area);}
            db.countries.mapReduce(mapFunction1, reduceFunction1, {out: {inline:1}})
           """

def query7():
    return """
            var reducer = function(key, values){ var count = 0; values.forEach(function(v) { count +=v;}); return count;}
 var mapper = function() {var country = this.name.official.split(" "); for(var i = country.length -1; i>= 0 ; i--){emit(country[i],1);}}
 db.countries.mapReduce(mapper, reducer, {out: {inline:1} , query:{"subregion":"Southern Asia"}})
           """ 

def query9():
    return """
            db.countries.aggregate([{ $match: { "name.common" : "United States"}},{$lookup:{from:"countries", localField: "borders", foreignField: "cca3", as: "neighborCountryname"}},{$unwind:"$neighborCountryname"},{$project:{_id:0, "name":"$name.common" ,neighborCountryname:"$neighborCountryname.name.common"}}]).pretty()
           """


#Do not edit below

def main():
	query_options = {1: query1(), 2: query2(), 3: query3(), 4: query4(), 
		5: query5(), 6: query6(), 7: query7(), 9: query9()}
	
	if len(sys.argv) == 1:
		if username() == "username":
			print("Make sure to change the username function to return your username.")
			return
		else:
			print(username())
		for query in query_options.values():
			print(query)
	elif len(sys.argv) == 2:
		if sys.argv[1] == "username":
			print(username())
		else:
			print(query_options[int(sys.argv[1])])

	
if __name__ == "__main__":
   main()
