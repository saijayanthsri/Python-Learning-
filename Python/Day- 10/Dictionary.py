#store data in dictionary

languages={
    "python": "Basic language for coding",
    "java": "Intermediate language for coding",
    "SQL": "Structured Query language"
}

print(languages["SQL"])

#to add in the dict

languages["html"]= "hyper"
#print(languages)

#to wipe existing dict
empty_dictionary= {}

languages= {}
print(languages)

#nested dictionary

car = {
    "maruti" : "alto",
    "volks" : "vento",
    "mahindra" : "scorpio",
    "audi" : "Q7"
}
print(car)

cars = {
    "maruti" : ["alto", "swift", "brezza", "Xl6"],
    "volks" : ["vento", "polo", "ameo"],
    "mahindra" : ["scorpio", "thar", "xuv700"],
    "audi" : ["Q7", "m30", "Q5"]
}
print(cars)

#range in nesting

print(cars["mahindra"][4])


#nested list

nested_list = ["A", "B",["C", "D"]]

print(nested_list[2][1])#print "D" from the nested list


