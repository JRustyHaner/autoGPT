import time
import sys
import csv
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import tkinter as tk
import pandas as pd

# List of queires to scrape from chatgpt 
queries = []
root = tk.Tk()

#open the chatgpt website with the webdriver
def make_query(query):
    try:
        #open the chatgpt website with the webdriver
        driver.get("https://chat.openai.com")
        time.sleep(5)
        #if there is a verify you are human clickbox, click it
        try:
            print("Human verification bypass")
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='Widget containing a Cloudflare security challenge']")))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.ctp-checkbox-label"))).click()
        except TimeoutException as e:
            print("No human verification")
            pass
        #find the input box and send the query, it's id is prompt-textarea
        #driver.find_element_by_id("prompt-textarea").send_keys(query)
        print("Sending query: " + query)
        driver.find_element(By.ID, "prompt-textarea").send_keys(query)
        time.sleep(5)
        #click the button with data-testid="send-button 
        #driver.find_element_by_css_selector("button[data-testid='send-button']").click()
        print("Clicking send button")
        driver.find_element(By.CSS_SELECTOR, "button[data-testid='send-button']").click()
        time.sleep(5)
        #get the response from the chatgpt by clicking the copy button, it's identified by aria-label="Copy"
        #response = driver.find_element_by_css_selector("button[aria-label='Copy']").click()
        print("Clicking copy button")
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Copy']").click()
        time.sleep(5)
        #get the response from the clipboard
        response = root.clipboard_get()
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
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = Chrome(options=options)
    #get the query from the first argument's csv
    queriesfile = sys.argv[1]
    queries = []
    #csv is just an array seperated by rows, so we can just read it in as a list
    with open(queriesfile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            queries.append(row[0])
    #initialize the dataframe
    df = pd.DataFrame(columns=['Query', 'Response'])
    #open the tkinter window and show a text box with the current status
    root.title("AutoGPT")
    #iterate over the queries
    for query in queries:
        #make the query
        print("Query: " + query)
        response = make_query(query)
        print("Response: " + response)
        #add the query and response to the dataframe
        df = df.append({'Query': query, 'Response': response}, ignore_index=True)
    #save the dataframe to a csv file, the second argument
    output_file = sys.argv[2]
    df.to_csv(output_file)
    #close the webdriver
    driver.quit()
    print("Done")
    sys.exit(0)


