# Solar Power Calculator
### Video Demo:  https://www.youtube.com/watch?v=CztzbsvyqmE
### Description:
This web application will estimate roughly how many solar panels you will need for your house, So you can anticipate how many
solar panels you will need to withstand the total load of your house's electrical devices.

All you need to do is to provide your yearly average of Energy in kilowatts.hour and to provide your country of residence, No registration required!.

This is an implementation of an ON-Grid solar powered house, meaning that in case the sun isn't giving the solar panels any energy, The system will use electricity provided by your regular provider, The system is only a rough estimation and of course you will need a professional who you can order from your solar panels provider to examine your electric load and give you an exact estimate of what inverters and solar panel models you will use and be most efficient for your system.

All countries have been saved in a text file and extracted at the start of the process as an array, the json file is the output of selenium web driver for all countries. Calculations are based on a university course I studied that put into consideration the Direct Normal Irradiance(the amount of solar radiance that actually reaches the earth's surface), the ambient temperature, energy used by user in a year, the inverter efficiency, the loss of solar panels efficiency due to dirt piling up on the surface of the solar panel used, properties of solar panel itself like rated power, max short circuit current, max open circuit current.

The results of the form will be how many solar panels you will need and how to arrange them i.e. how many panels you will need for series or parallel connection and also what inverter you will use.

(The app is built using HTML, CSS, Bootstrap, Flask framework. Data has been web scraped by selenium web driver.)



### Problems I faced:
There isn't a "free" API on any website that provides Solar radiance information for each country, I searched a lot for one,
but the ones I found were only for the temperature in each country, So I had to find another approach to finding the info. I need about each country, So I found this website Global Solar Atlas which provides all info about each country but doesn't have an API
nor a PDF which I can extract information from, The only way was to search for each country in the search bar of the site and then
take the data manually, I needed to find a way to automate this process for 195 countries and save the info to a text, And there came selenium web driver, A module for python that can automate site interactions and loop through the site and web scrape data for all countries and append their information to a dictionary that I can use later for the website(I attached the selenium program in the other file in this project), I learned all basic functions for selenium to achieve my goal.





