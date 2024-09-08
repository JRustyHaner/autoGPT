import time
import sys
import csv
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import JavascriptException
import pandas as pd

# List of queires to scrape from chatgpt 
queries = []

#open the chatgpt website with the webdriver
def make_query(query):
    try:
        #open the chatgpt website with the webdriver
        driver.get("https://app.chatgpt.com/")
        time.sleep(5)
        #find the input box and send the query, it's id is prompt-textarea
        driver.find_element_by_id("prompt-textarea").send_keys(query)
        time.sleep(5)
        #click the button with data-testid="send-button 
        driver.find_element_by_css_selector("button[data-testid='send-button']").click()
        time.sleep(5)
        #get the response from the chatgpt by clicking the copy button, it's identified by aria-label="Copy"
        response = driver.find_element_by_css_selector("button[aria-label='Copy']").click()
        time.sleep(5)
        #return the response
        return response
    except NoSuchElementException as e:
        print("Element not found")
        return None
    except TimeoutException as e:
        print("Timeout")
        return None
    except JavascriptException as e:
        print("Javascript error")
        return None
    
#main
if __name__ == "__main__":\
    #make sure there are two arguments, if not print the usage
    if len(sys.argv) != 3:
        print("Usage: python3 autogpt.py <queries.csv> <output.csv>")
        print("Developed by: James 'Rusty' Haner")
        sys.exit(1)
    #initialize the webdriver
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = Chrome(options=options)
    #get the query from the first argument's csv
    queries = sys.argv[1]
    with open(queries, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            queries.append(row[0])
    #initialize the dataframe
    df = pd.DataFrame(columns=['Query', 'Response'])
    #iterate over the queries
    for query in queries:
        #make the query
        response = make_query(query)
        #add the query and response to the dataframe
        df = df.append({'Query': query, 'Response': response}, ignore_index=True)
    #save the dataframe to a csv file, the second argument
    output_file = sys.argv[2]
    df.to_csv(output_file)
    #close the webdriver
    driver.quit()
    print("Done")
    sys.exit(0)


