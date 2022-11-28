# 9. Create a dictionary describing a mobile phone. 
# Use at least 6 key-value pairs of data. Use different value types. 
# Then, using 'for' loop, display the contents of the dictionary. 
# To read a key and value, use the items() method.

phone = {
    "number" : 434232323,
    "country" : "Poland",
    "brand" : "iPhone",
    "year_of_production" : 2021,
    "warranty_time" : "24 months",
    "charging_port" : "Lightning"
}

for key, value in phone.items():
    print(key, value)
    
print("----------------")

for item in phone.items():
    print(item)