#AutoGPT: Documentation

This script automates scraping responses from ChatGPT using a headless Chrome browser. It takes a CSV file containing queries and outputs a CSV file with both queries and corresponding responses.
Dependencies

    Python 3.x
    ```pip install undetected_chromedriver selenium pandas setuptools```


##Usage

```python3 autogpt.py <queries.csv> <output.csv>```

    <queries.csv>: Path to a CSV file containing one query per line.
    <output.csv>: Path to the output CSV file containing queries and responses.

Developed by: James 'Rusty' Haner

##Script Functionality

    Imports: Necessary libraries for interacting with Chrome, handling exceptions, file processing, and displaying progress.
    make_query function: Takes a query string as input.
        Opens the ChatGPT website using a headless Chrome browser.
        Bypasses potential human verification (if present).
        Locates the query input box and sends the provided query.
        Clicks the "send" button.
        Waits for a response, clicks the "copy" button (to copy response to clipboard).
        Retrieves the response text from the clipboard using Tkinter.
        Handles potential exceptions like missing elements, timeouts, and JavaScript errors by returning None.
    Main:
        Checks for correct number of arguments (script name, queries file, output file).
        Initializes a headless Chrome browser with options to bypass sandbox restrictions.
        Reads queries from the provided CSV file into a list.
        Creates a pandas DataFrame with columns for "Query" and "Response".
        Opens a Tkinter window with title "AutoGPT" (optional for visual progress).
        Iterates through each query:
            Calls make_query to submit the query and retrieve the response.
            Appends both query and response to the DataFrame.
        Saves the DataFrame as a CSV file with the specified output path.
        Quits the Chrome browser.
        Prints completion message and exits the script.