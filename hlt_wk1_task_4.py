
# Calculate depreciation on Bike
#Calculate Depreciation @ 10% per annum, till the value reaches $1,000

price_of_bike = 2000
year_of_bike = 0

while price_of_bike > 1000:
    year_of_bike += 1
    print("New Price of Bike is ", "$",int(price_of_bike), "in Year", year_of_bike)
    price_of_bike = price_of_bike * 0.9
    