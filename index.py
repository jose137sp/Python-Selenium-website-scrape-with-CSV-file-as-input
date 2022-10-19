from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv


with open('./example.csv', newline='') as csvfile: 
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader: 
        driver = webdriver.Chrome('/Users/josesaavedra/webdriver/chromedriver') # Here you have to put the path to your chromedriver
        driver.get("https://www.google.com") # Here you have to put the url of the page you want to scrape
        elem = driver.find_element(By.NAME, "q") # Here you have to put the name of the input field (inspect the page to find it)
        elem.clear() # Clear the input field
        print(row[0]) # Print the value of the row of the csv file
        elem.send_keys(row[0]) # Send the value of the row of the csv file to the input field
        elem.send_keys(Keys.RETURN) # Press enter
        assert "No results found." not in driver.page_source # Assert that the page contains the value of the row of the csv file
        # driver.quit() # Close the browser






