import pandas as pd 
data = pd.read_csv(r'C:\Users\behro\OneDrive\Desktop\pytthon project\file.csv')


#print(data)
#show dataset


#print(data.head())
#it shows the first n rows the data(by default n = 5)


#shape
#it shows the total no of rows and no. of columns of the dataframe
#print(data.shape)


# index
# provide the index of the dataframe
#print(data.index)


#columns
# it shows the name of each columns
#print(data.columns)


#data types
# it shows type of each column
#print(data.dtypes)
 

#unique
#in a column it shows the unique values.
# it can be applied on a single column only not on the whole dataframe
# print(data['Weather'].unique())


#nunique
#total no. of unique values in each column
#print(data.nunique())


#count
# total no. of non-null in each column
#print(data.count())


#value_counts
# shows the unique values with their count
#print(data['Weather'].value_counts())


#info
# provides basic information about the dataframe
#print(data.info())


###################################################################


#1 find all the unique "wind speed" values in the data
#show the number of unique values
#unique_wind_speed_number = print(data["Wind Speed_km/h"].nunique())
#show the array of unique values 
#unique_wind_speed = print(data["Wind Speed_km/h"].unique())


#2 find the number of times when the weather is exactly clear
# group by
#print(data.groupby("Weather").get_group('Clear '))


#3 find the number of times when the wind speed was exactly 4 km/h
#print(data[data['Wind Speed_km/h'] == 4])


#4 find out the nulls and not nulls values in data
#print(data.isnull().sum()) # retrive a boolean
#print(data.isnull())  # retrive a number of nulls
#print(data.notnull().sum()) # not null values


#5 rename the coloumn "weather" of the dataframe to "weather condition"
#this command just rename the column for temp purpose
#print(data.rename(columns= {"Weather" : "Weather Condition"}))
#if we want to rename it as permanent name we should use inplace = True command
#print(data.rename(columns= {"Weather" : "Weather Condition"}, inplace= True))


#6 what is the mean "visibility" ?
#print(data.Visibility_km.mean())


#7 what is the standard deviation of "pressure" in this data
#print(data.Press_kPa.std())


#8 what is the variance of relative humidity in this data?
#print(data["Rel Hum_%"].var())


#9 find all instances when "snow" was recorded
#print(data["Weather"].value_counts())
#print(data["Weather"] == "snow") # it return boolean
#print(data[data["Weather"] == "Snow"]) it rurn the number of snow condition
#to show the records that contains the word "snow"
#print(data[data["Weather"].str.contains("Snow")])


#10 find all instances when "wind speed is above 24" and visibility is 25
#print(data[(data["Wind Speed_km/h"] > 24) & (data['Visibility_km'] == 25)])


#11 what is the mean value of each column against each weather condition
#print(data.groupby('Weather').mean())


#12 min and max of value of each column against each weather condition
#print(data.groupby("Weather").min())
#print(data.groupby("Weather").max())


#13 show all the records where weather condition is fog
#print(data[data["Weather"] == "Fog"])


#14 find all instance when Weather is Clear or visibility is above 40
#print(data[(data["Weather"] == "Clear") | (data["Visibility_km"] > 40)])


#15 find all instances when
# A weather is Clear and relative humidity is greater than 50
# B  visibility is above 40
#print(data[(data["Weather"] == "Clear") & (data["Rel Hum_%"] > 50) | (data["Visibility_km"] > 40)])
