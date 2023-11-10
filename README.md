# Python Scripting Toolbox: 100 Scripts for Developers

In this extensive book, we will begin a study of many scripts that demonstrate the remarkable possibilities of Python across a variety of different fields. Whether you're an experienced developer looking for new tools or a newbie eager to grasp the power of the language, this book is your gateway to a world of solutions that are not only practical but also efficient and inventive. Each script is a useful example of Python's versatility, since it provides answers to issues that are encountered in the real world and functions as an important resource for Python programmers, enthusiasts, and beginners alike. Come along with us as we dissect the art and science of Python scripting, and we'll show you a hundred different ways to appreciate the language's elegant syntax and powerful capabilities.

# INDEX
**1. Web Scraping Scripts:**
- 1.1. Extract news headlines from a website.
- 1.2. Scrape product information from an e-commerce site.
- 1.3. Monitor and extract stock prices.
- 1.4. Scraping multilingual content for translation purposes
- 1.5. Scrape weather forecasts for specific locations.

**2. Automation Scripts:**
- 2.1. Automate repetitive file management tasks.
- 2.2. Automate email sending with attachments.
- 2.3. Create a script to schedule and run tasks.
- 2.4. Automate data backup processes.
- 2.5. Build a script to automate software installations.

**3. Data Analysis and Visualization Scripts:**
- 3.1. Analyze and visualize financial data.
- 3.2. Create graphs and charts for data presentations.
- 3.3. Analyze and visualize weather data.
- 3.4. Generate statistics from survey data.
- 3.5. Create word cloud visualizations from text data.

**4. Image Processing Scripts:**
- 4.1. Crop and resize images.
- 4.2. Apply filters and effects to photos.
- 4.3. Create image thumbnails.
- 4.4. Extract text from images using OCR.
- 4.5. Watermark images with a logo or text.

**5. Text Processing Scripts:**
- 5.1. Perform sentiment analysis on text data.
- 5.2. Build a script for text summarization.
- 5.3. Create a spell-checker or grammar checker.
- 5.4. Convert text to speech or speech to text.
- 5.5. Generate random text for testing purposes.

**6. File Management Scripts:**
- 6.1. Sort and organize files in a directory.
- 6.2. Search for files with specific extensions.
- 6.3. Clean up duplicate files.
- 6.4. Monitor changes in file directories.
- 6.5. Rename files in bulk according to a pattern.

**7. System Monitoring and Reporting Scripts:**
- 7.1. Monitor system resource usage (CPU, memory, disk).
- 7.2. Generate daily/weekly reports on system statistics.
- 7.3. Monitor network traffic and generate reports.
- 7.4. Create a script to log and analyze system events.
- 7.5. Build a script to track and notify about system uptime.

**8. Games and Entertainment Scripts:**
- 8.1. Create a simple text-based game.
- 8.2. Build a script to generate random jokes or facts.
- 8.3. Design a quiz or trivia game.
- 8.4. Develop a script for generating random art.
- 8.5. Create a script to simulate rolling dice.

**9. Utility Scripts:**
- 9.1. Calculate and convert units (e.g., currency exchange rates).
- 9.2. Create a script for generating strong passwords.
- 9.3. Build a simple calculator.
- 9.4. Convert between different file formats (e.g., PDF to text).
- 9.5. Implement a URL shortener.

**10. Network and Internet Scripts:**
- 10.1. Ping multiple hosts to check their status.
- 10.2. Monitor website availability and response times.
- 10.3. Retrieve and analyze website headers.
- 10.4. Create a port scanner to check for open ports.
- 10.5. Automate interactions with web APIs.

**11. Security Scripts:**
- 11.1. Encrypt and decrypt files.
- 11.2. Create a simple password manager.
- 11.3. Generate and verify digital signatures.
- 11.4. Build a script for secure file deletion.
- 11.5. Create a basic firewall rule manager.

**12. IoT and Hardware Control Scripts:**
- 12.1. Build scripts to control IoT devices (e.g., lights, thermostats).
- 12.2. Monitor and display sensor data (e.g., temperature, humidity).
- 12.3. Control a robot or drone.
- 12.4. Capture and analyze data from webcams or cameras.
- 12.5. Create a script to interface with microcontrollers (e.g., Arduino).

**13. AI and Machine Learning Scripts:**
- 13.1. Implement a basic machine learning model (e.g., linear regression).
- 13.2. Develop a simple chatbot using natural language processing.
- 13.3. Train a model for image recognition.
- 13.4. Create a recommendation system.
- 13.5. Build a script for sentiment analysis on social media data.

**14. Database Scripts:**
- 14.1. Automate database backup and restore.
- 14.2. Generate and execute SQL queries.
- 14.3. Build a script for database migration.
- 14.4. Extract data from databases to CSV or Excel files.
- 14.5. Create a basic CRUD application.

**15. Education and Learning Scripts:**
- 15.1. Create flashcards for studying.
- 15.2. Build a script for math problem generation.
- 15.3. Develop a spelling or vocabulary quiz.
- 15.4. Implement a script for learning a new language.
- 15.5. Create a timer for productivity and focus.

---
## 1. Web Scraping Scripts:

Web scraping scripts are programs designed to extract data from websites. These scripts use various techniques to navigate through the structure of web pages, locate relevant information, and then retrieve and store that data for further use. Web scraping is commonly used for tasks such as data extraction, data mining, and content aggregation.

### 1.1. Extract news headlines from a website
To extract news headlines from a website using Python, you can use the `requests` library to fetch the HTML content of the webpage and `BeautifulSoup` for parsing the HTML and extracting the headlines. Here's a basic example using these libraries:

```python
import requests
from bs4 import BeautifulSoup

def get_headlines(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the HTML elements containing the headlines
        # Adjust the CSS selectors based on the structure of the webpage
        headlines = soup.select('.headline-class')  # Replace with the actual CSS selector

        # Extract and print the headlines
        for headline in headlines:
            print(headline.text)
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

# Replace 'https://example.com' with the actual URL of the website
get_headlines('https://example.com')
```

Note:

1. You need to install the `requests` and `beautifulsoup4` libraries if you haven't already. You can do this using:

   ```bash
   pip install requests beautifulsoup4
   ```

2. Adjust the CSS selector inside the `soup.select()` method to match the structure of the HTML containing the headlines on the specific website you are targeting.

---

### 1.2. Scrape product information from an e-commerce site
Web scraping e-commerce sites should be done ethically and in compliance with the site's terms of service. Here's a basic example using Python, `requests`, and `BeautifulSoup` to scrape product information from an e-commerce site. In this example, we'll use a hypothetical URL, and you should replace it with the actual URL of the e-commerce site you want to scrape:

```python
import requests
from bs4 import BeautifulSoup

def scrape_product_information(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the HTML elements containing product information
        # Adjust the CSS selectors based on the structure of the webpage
        product_containers = soup.select('.product-container-class')  # Replace with the actual CSS selector

        # Extract and print product information
        for product_container in product_containers:
            # Extract product details (adjust the CSS selectors accordingly)
            product_name = product_container.select_one('.product-name-class').text.strip()
            product_price = product_container.select_one('.product-price-class').text.strip()

            print(f"Product Name: {product_name}")
            print(f"Product Price: {product_price}")
            print("-" * 50)
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

# Replace 'https://example-ecommerce-site.com' with the actual URL of the e-commerce site
scrape_product_information('https://example-ecommerce-site.com')
```

Things to note:

1. Install the required libraries using:

   ```bash
   pip install requests beautifulsoup4
   ```

2. Adjust the CSS selectors inside `soup.select()` to match the structure of the HTML containing product information on the specific e-commerce site you are targeting.

3. Web scraping should be done responsibly, and you should be aware of the legal and ethical implications. Some websites may have restrictions on web scraping in their terms of service. Always review and comply with the terms of the website you are scraping.

4. Make requests at a reasonable rate to avoid overloading the server and potential IP blocking.

---

### 1.3. Monitor and extract stock prices
To monitor and extract stock prices with Python, you can use various libraries, and one popular choice is `yfinance` for Yahoo Finance data. Here's a simple example:

First, you need to install the `yfinance` library:

```bash
pip install yfinance
```

Now, you can use the following Python script to get stock prices:

```python
import yfinance as yf
import time

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.history(period='1d')['Close'].iloc[-1]
    return price

def monitor_stock_price(ticker, interval_seconds=60):
    while True:
        price = get_stock_price(ticker)
        print(f'{ticker} Stock Price: ${price:.2f}')
        time.sleep(interval_seconds)

# Replace 'AAPL' with the stock symbol you want to monitor (e.g., 'AAPL' for Apple)
stock_symbol = 'AAPL'

# Monitor stock price every 60 seconds
monitor_stock_price(stock_symbol)
```

Replace `'AAPL'` with the stock symbol of the company you're interested in. This script will continuously print the stock price at the specified interval (in seconds). You can adjust the `interval_seconds` parameter based on how frequently you want to check the stock price.


---

### 1.4. Scraping multilingual content for translation purposes
To scrape multilingual content for translation purposes using Python, you can use the `requests` library for making HTTP requests and `BeautifulSoup` for parsing HTML content. Additionally, you may want to use a translation API, such as Google Translate, to translate the content. Here's a basic example using these libraries:

```python
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def scrape_and_translate(url, target_language='en'):
    # Make an HTTP request to the website
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content from the webpage
        text_content = soup.get_text()

        # Translate the text content
        translator = Translator()
        translated_content = translator.translate(text_content, dest=target_language).text

        return translated_content
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None

# Example usage
url_to_scrape = 'https://example.com'
translated_text = scrape_and_translate(url_to_scrape, target_language='fr')

if translated_text:
    print(f"Translated Content:\n{translated_text}")
```

In this example:

- The `requests` library is used to make an HTTP request to the specified URL.
- `BeautifulSoup` is used to parse the HTML content and extract the text.
- The `googletrans` library is used for translation. Install it using `pip install googletrans==4.0.0-rc1`.

Note: Make sure to review the terms of service of the translation API you use and comply with any usage restrictions.

---
### 1.5. Scrape weather forecasts for specific locations
You can scrape weather forecasts using Python with the help of web scraping libraries like BeautifulSoup and requests. Here's a simple example using Python:

```python
import requests
from bs4 import BeautifulSoup

def scrape_weather(location):
    # Replace 'YOUR_WEATHER_WEBSITE_URL' with the actual URL of the weather website you want to scrape
    url = f'YOUR_WEATHER_WEBSITE_URL/{location}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Use BeautifulSoup to extract the relevant information from the HTML
        # Replace these selectors with the actual HTML elements that contain the weather information
        temperature = soup.select_one('.temperature').text
        condition = soup.select_one('.weather-condition').text

        print(f'Temperature: {temperature}\nCondition: {condition}')
    else:
        print('Failed to retrieve weather information.')

# Replace 'CITY_NAME' with the name of the city for which you want to get the weather forecast
scrape_weather('CITY_NAME')
```

Before using this code, you need to inspect the HTML structure of the website from which you want to scrape weather information. Determine the appropriate HTML tags and classes that contain the data you need, and update the code accordingly.

---

## 2. Automation Scripts:

Automation scripts are programs designed to perform repetitive tasks or processes without direct human intervention, enhancing efficiency and reducing manual workload. These scripts leverage programming languages to streamline routine operations, ranging from file management and data processing to system monitoring and software installations. Automation scripts contribute to increased productivity, decreased error rates, and consistent task execution across various domains, such as system administration, data analysis, and software development. By eliminating manual intervention in repetitive workflows, automation scripts empower users to focus on more complex and strategic aspects of their work, ultimately optimizing resource utilization and enhancing overall operational effectiveness.

### 2.1. Automate repetitive file management tasks
Automating repetitive file management tasks with Python can save time and effort. Here's a general guide on how to perform common file management tasks using Python:

1. **Renaming Files:**
   To rename files, you can use the `os` module. Here's an example that renames all files in a directory by adding a prefix:

   ```python
   import os

   folder_path = '/path/to/your/files'
   prefix = 'new_prefix_'

   for filename in os.listdir(folder_path):
       if os.path.isfile(os.path.join(folder_path, filename)):
           new_filename = prefix + filename
           os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
   ```

2. **Moving Files:**
   To move files from one directory to another, use the `shutil` module:

   ```python
   import shutil

   source_path = '/path/to/source'
   destination_path = '/path/to/destination'

   shutil.move(source_path, destination_path)
   ```

3. **Copying Files:**
   For copying files, also use the `shutil` module:

   ```python
   import shutil

   source_path = '/path/to/source'
   destination_path = '/path/to/destination'

   shutil.copy(source_path, destination_path)
   ```

4. **Deleting Files:**
   To delete files, you can use the `os` module:

   ```python
   import os

   file_to_delete = '/path/to/your/file.txt'

   if os.path.exists(file_to_delete):
       os.remove(file_to_delete)
   else:
       print("The file does not exist.")
   ```

5. **Batch Processing:**
   To apply the same operation to multiple files, you can use loops and functions. For example, if you want to delete all files with a certain extension:

   ```python
   import os

   folder_path = '/path/to/your/files'
   extension_to_delete = '.txt'

   for filename in os.listdir(folder_path):
       if filename.endswith(extension_to_delete):
           file_to_delete = os.path.join(folder_path, filename)
           os.remove(file_to_delete)
   ```

Make sure to replace the paths and filenames with your actual file paths and names. Additionally, exercise caution when performing operations like file deletion to avoid accidental loss of data. Always test your scripts on a small set of files before applying them to a larger dataset.

### 2.2. Automate email sending with attachments
To automate email sending with attachments in Python, you can use the `smtplib` library for sending emails and the `email` library for composing emails with attachments. Below is a simple example using Gmail as the email provider, but you can adapt it for other providers as well.

Firstly, you need to enable "Less secure app access" in your Gmail account settings or generate an "App Password" if you have two-factor authentication enabled.

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject, body, to_email, attachment_path):
    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'  # Use App Password if two-factor authentication is enabled

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach body as plain text
    msg.attach(MIMEText(body, 'plain'))

    # Attach file
    attachment = open(attachment_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
    msg.attach(part)

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, to_email, msg.as_string())

    print(f"Email sent successfully to {to_email}")

# Example usage
send_email(
    subject='Test Email with Attachment',
    body='This is the body of the email.',
    to_email='recipient@example.com',
    attachment_path='/path/to/your/file.txt'
)
```

Make sure to replace the placeholder values with your own email details and the actual file path you want to attach. Additionally, always keep your email credentials secure and consider using environment variables to store sensitive information.

### 2.3. Create a script to schedule and run tasks
To schedule and run tasks in Python, you can use the `schedule` library, which is a lightweight library that provides a simple interface for job scheduling. First, you need to install the library using:

```bash
pip install schedule
```

Now, you can create a script to schedule and run tasks at specified intervals. Here's a simple example:

```python
import schedule
import time

def job():
    print("Task is running...")

# Schedule the job to run every 1 hour
schedule.every(1).hours.do(job)

# You can add more schedules for different intervals
# For example, every 30 minutes: schedule.every(30).minutes.do(job)
# For every day at a specific time: schedule.every().day.at("10:30").do(job)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)  # You can adjust the sleep duration as needed
```

This script defines a `job` function that prints a message, schedules the job to run every hour using `schedule.every(1).hours.do(job)`, and then runs the scheduler in a loop with a short delay between iterations.

You can customize the scheduling based on your needs, and you can also modify the `job` function to perform any task you want.

Remember to adapt the script according to your specific requirements and adjust the scheduling intervals accordingly. Additionally, consider using more robust solutions like Celery for more complex task scheduling in larger projects.

### 2.4. Automate data backup processes
Automating data backup processes in Python can be achieved using various libraries and tools. One popular library for file operations is `shutil`, and combining it with a scheduling library like `schedule` can help automate the backup process. Here's a simple example:

1. Install the `schedule` library if you haven't already:

```bash
pip install schedule
```

2. Create a Python script to perform the backup:

```python
import shutil
import schedule
import time
import datetime

def backup():
    source_directory = "/path/to/source"
    backup_directory = "/path/to/backup"

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_folder = f"backup_{timestamp}"

    try:
        shutil.copytree(source_directory, f"{backup_directory}/{backup_folder}")
        print("Backup completed successfully.")
    except Exception as e:
        print(f"Backup failed. Error: {e}")

# Schedule the backup to run every day at a specific time (e.g., 2:00 AM)
schedule.every().day.at("02:00").do(backup)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
```

In this script:

- The `backup` function uses `shutil.copytree` to copy the entire source directory to a new backup folder within the specified backup directory.
- The backup folder is named with a timestamp to ensure uniqueness.
- The `schedule` library is used to schedule the backup function to run every day at a specific time (adjust the time as needed).

Adjust the `source_directory` and `backup_directory` variables according to your setup. You can also customize the backup schedule and implement more advanced features based on your specific requirements.

Keep in mind that this is a basic example, and in a production environment, you might want to consider error handling, logging, and possibly more robust backup solutions depending on your needs.

### 2.5. Build a script to automate software installations
Automating software installations in Python can be done using the `subprocess` module to run system commands. Below is a simple example script that installs multiple software packages on a Linux system using the package manager (e.g., `apt` for Ubuntu):

```python
import subprocess

def install_software(packages):
    try:
        for package in packages:
            print(f"Installing {package}...")
            subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
            print(f"{package} installed successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package}. {e}")

if __name__ == "__main__":
    # List of software packages to install
    software_packages = ["package1", "package2", "package3"]

    # Run the installation
    install_software(software_packages)
```

Replace `"package1"`, `"package2"`, etc., with the actual package names you want to install. You may need to adjust the package manager command (`sudo apt install`) based on the package manager used by your operating system.

Remember:

- Ensure that the script is executed with appropriate privileges to install software (`sudo` is used in this example).
- Be cautious when automating installations, especially with the use of `sudo`. Unauthorized or incorrect installations can affect system stability.

This script is a basic example, and in a production environment, you might want to consider additional features such as logging, error handling, and more robust configuration options.

---
## 3. Data Analysis and Visualization Scripts:

Data Analysis and Visualization Scripts are tools developed to process and interpret large datasets, extracting meaningful insights and presenting them in a comprehensible format. These scripts often employ programming languages like Python or R, utilizing statistical techniques and visualization libraries to uncover patterns, trends, and relationships within the data. From generating descriptive statistics to creating informative charts and graphs, these scripts assist analysts and researchers in transforming raw data into actionable knowledge. Whether used for business intelligence, scientific research, or decision-making processes, Data Analysis and Visualization Scripts play a crucial role in unlocking the potential of data, enabling informed decision-making and facilitating a deeper understanding of complex information.

### 3.1. Analyze and visualize financial data
Analyzing and visualizing financial data can be done using various Python libraries. Two popular libraries for this purpose are `pandas` for data manipulation and analysis and `matplotlib` for creating visualizations. Here's a simple example to get you started:

1. **Install necessary libraries:**

```bash
pip install pandas matplotlib
```

2. **Sample Python script for financial data analysis and visualization:**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Sample financial data (replace this with your dataset)
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Price': [100, 105, 98, 102, 110],
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

# Plotting the financial data
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Price'], marker='o', linestyle='-', color='b')
plt.title('Financial Data Analysis')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.show()
```

This example assumes you have a time series of financial data with 'Date' and 'Price' columns. Adjust the script according to your actual dataset.

3. Enhance with financial libraries:**

For more advanced financial analysis and visualizations, you can consider using libraries such as `numpy` for numerical operations, `pandas_datareader` for fetching financial data from various sources, and `mplfinance` for specialized financial plots.

```bash
pip install numpy pandas_datareader mplfinance
```

Below is a more comprehensive example:

```python
import pandas_datareader as pdr
import numpy as np
import mplfinance as mpf

# Fetch financial data from Yahoo Finance
symbol = 'AAPL'
start_date = '2022-01-01'
end_date = '2023-01-01'
financial_data = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)

# Calculate moving average
financial_data['MA20'] = financial_data['Close'].rolling(window=20).mean()

# Plot candlestick chart with moving average
mpf.plot(
    financial_data,
    type='candle',
    mav=(20,),
    title=f'{symbol} Stock Price and 20-Day Moving Average',
    ylabel='Price',
    show_nontrading=True,
)
```

This script fetches stock data for Apple (AAPL) from Yahoo Finance, calculates a 20-day moving average, and visualizes the data using `mplfinance`. Adjust the symbol, start_date, and end_date according to your needs.

---
### 3.2. Create graphs and charts for data presentations
Creating graphs and charts for data presentations in Python can be done using various libraries. Two commonly used libraries for this purpose are `matplotlib` and `seaborn`. Here are examples of how you can create different types of charts using these libraries:

1. **Install necessary libraries:**

```bash
pip install matplotlib seaborn
```

2. **Example scripts for different types of charts:**

**Bar Chart:**

```python
import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C']
values = [25, 40, 30]

# Create a bar chart
plt.bar(categories, values, color='blue')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
```

**Line Chart:**

```python
import matplotlib.pyplot as plt

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values = [10, 12, 18, 15, 20]

# Create a line chart
plt.plot(x_values, y_values, marker='o', linestyle='-', color='green')
plt.title('Line Chart Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

**Scatter Plot:**

```python
import matplotlib.pyplot as plt

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values = [10, 12, 18, 15, 20]

# Create a scatter plot
plt.scatter(x_values, y_values, color='red')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

**Histogram:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate random data for the histogram
data = np.random.randn(1000)

# Create a histogram
plt.hist(data, bins=20, color='purple', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
```

**Heatmap (using seaborn):**

```python
import seaborn as sns
import numpy as np

# Generate random data for the heatmap
data = np.random.rand(5, 5)

# Create a heatmap using seaborn
sns.heatmap(data, annot=True, cmap='viridis')
plt.title('Heatmap Example')
plt.show()
```

These are just basic examples, and both `matplotlib` and `seaborn` offer a wide range of customization options for creating complex and informative data visualizations. Adjust the scripts based on your specific data and visualization requirements.

---
### 3.3. Analyze and visualize weather data
Analyzing and visualizing weather data can be done using Python with the help of various libraries. For this purpose, you might want to use libraries such as `pandas` for data manipulation, `matplotlib` for plotting, and `seaborn` for additional plotting styles. Here's a basic example to get you started:

1. **Install necessary libraries:**

```bash
pip install pandas matplotlib seaborn
```

2. **Example script:**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample weather data (replace this with your own data)
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Temperature': [25, 28, 22, 30, 26],
    'Humidity': [60, 55, 70, 45, 50],
    'Wind Speed': [10, 12, 8, 15, 11]
}

# Create a DataFrame
weather_df = pd.DataFrame(data)
weather_df['Date'] = pd.to_datetime(weather_df['Date'])

# Print the DataFrame
print(weather_df)

# Plotting
plt.figure(figsize=(12, 6))

# Line plot for temperature
plt.subplot(2, 2, 1)
sns.lineplot(x='Date', y='Temperature', data=weather_df)
plt.title('Temperature Over Time')

# Bar plot for humidity
plt.subplot(2, 2, 2)
sns.barplot(x='Date', y='Humidity', data=weather_df)
plt.title('Humidity Over Time')

# Scatter plot for temperature vs. wind speed
plt.subplot(2, 2, 3)
sns.scatterplot(x='Temperature', y='Wind Speed', data=weather_df)
plt.title('Temperature vs. Wind Speed')

# Heatmap for correlation matrix
plt.subplot(2, 2, 4)
corr_matrix = weather_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

plt.tight_layout()
plt.show()
```

In this example, I've used a synthetic dataset with columns for date, temperature, humidity, and wind speed. The script creates different types of plots such as line plot, bar plot, scatter plot, and a heatmap showing the correlation matrix between variables.

Replace the sample data with your actual weather data for meaningful visualizations. Adjust the script based on the specific aspects of weather data you want to analyze and visualize.

---
### 3.4. Generate statistics from survey data
To generate statistics from survey data in Python, you can use the `pandas` library for data manipulation and the `matplotlib` library for visualization. Below is a basic example to get you started:

1. **Install necessary libraries:**

```bash
pip install pandas matplotlib
```

2. **Example script:**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Sample survey data (replace this with your own data)
data = {
    'Age': [25, 30, 22, 35, 28, 40, 32, 28, 22, 36],
    'Income': [50000, 60000, 45000, 75000, 55000, 80000, 70000, 60000, 48000, 72000],
    'Satisfaction': [4, 5, 3, 5, 4, 5, 4, 3, 3, 5],
    'Education': ['Bachelor', 'Master', 'Bachelor', 'PhD', 'Bachelor', 'PhD', 'Master', 'Bachelor', 'Master', 'PhD']
}

# Create a DataFrame
survey_df = pd.DataFrame(data)

# Print basic statistics
print("Basic Statistics:")
print(survey_df.describe())

# Plotting
plt.figure(figsize=(12, 4))

# Histogram for Age
plt.subplot(1, 3, 1)
plt.hist(survey_df['Age'], bins=5, edgecolor='black')
plt.title('Age Distribution')

# Boxplot for Income
plt.subplot(1, 3, 2)
plt.boxplot(survey_df['Income'])
plt.title('Income Distribution')

# Bar plot for Education
plt.subplot(1, 3, 3)
education_counts = survey_df['Education'].value_counts()
education_counts.plot(kind='bar', color='skyblue')
plt.title('Education Level')

plt.tight_layout()
plt.show()
```

In this example, I've used a synthetic dataset with columns for age, income, satisfaction, and education. The script calculates basic statistics using `describe()` and creates different types of plots such as a histogram, boxplot, and bar plot.

Replace the sample data with your actual survey data for meaningful statistics and visualizations. Adjust the script based on the specific aspects of your survey data that you want to analyze and visualize.

---
### 3.5. Create word cloud visualizations from text data
To create word cloud visualizations from text data in Python, you can use the `wordcloud` library along with other libraries such as `matplotlib` for visualization and `nltk` for text processing. Here's a basic example:

1. **Install necessary libraries:**

```bash
pip install wordcloud matplotlib nltk
```

2. **Example script:**

```python
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import download

# Download NLTK resources (stopwords)
download('stopwords')
download('punkt')

# Sample text data (replace this with your own text)
text_data = """
Python is an amazing programming language. It is widely used for data analysis,
machine learning, and web development. Python has a large and active community
that contributes to its growth and success.
"""

# Tokenize the text and remove stopwords
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(text_data)
filtered_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]

# Join the tokens into a single string
processed_text = ' '.join(filtered_tokens)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(processed_text)

# Plot the WordCloud image
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

In this example, the script preprocesses the text by tokenizing it, converting words to lowercase, and removing common English stopwords. The processed text is then used to generate a word cloud using the `WordCloud` class from the `wordcloud` library.

Replace the `text_data` variable with your actual text data. Adjust the preprocessing steps based on your specific requirements. You can also customize the appearance of the word cloud by modifying parameters in the `WordCloud` constructor.

---

## 4. Image Processing Scripts:

Image Processing Scripts are computational tools designed to manipulate and enhance digital images through various algorithms and techniques. Leveraging programming languages such as Python or MATLAB, these scripts perform tasks like resizing, cropping, filtering, and applying effects to images. More advanced applications involve tasks like object recognition, segmentation, and color correction. Image Processing Scripts are vital in fields ranging from photography and graphic design to medical imaging and computer vision, providing a versatile toolkit for professionals and researchers to modify and analyze images for diverse purposes. Whether automating routine edits or extracting intricate details from complex visual data, these scripts contribute to the efficiency and accuracy of image-related tasks across multiple domains.

### 4.1. Crop and resize images
To crop and resize images with Python, you can use the Pillow (PIL) library. If you haven't installed Pillow yet, you can do so by running:

```bash
pip install Pillow
```

Now, here's an example Python script to crop and resize an image:

```python
from PIL import Image

def crop_and_resize(input_path, output_path, crop_box, new_size):
    # Open the image
    img = Image.open(input_path)

    # Crop the image
    cropped_img = img.crop(crop_box)

    # Resize the cropped image
    resized_img = cropped_img.resize(new_size)

    # Save the result
    resized_img.save(output_path)

# Example usage:
input_image = "path/to/your/input_image.jpg"
output_image = "path/to/your/output_image.jpg"

# Define the crop box (left, upper, right, lower)
crop_box = (100, 100, 500, 500)

# Define the new size (width, height)
new_size = (300, 300)

# Call the function
crop_and_resize(input_image, output_image, crop_box, new_size)
```

Replace `"path/to/your/input_image.jpg"` and `"path/to/your/output_image.jpg"` with the actual paths for your input and output images.

In this example:
- `crop_box` defines the region to be cropped from the original image.
- `new_size` specifies the width and height of the resized image.

Adjust these parameters according to your requirements. Run the script, and it will crop and resize the image accordingly.

---
### 4.2. Apply filters and effects to photos
To apply filters and effects to photos in Python, you can use the Pillow (PIL) library. Here's an example script that applies a few filters to an image:

```python
from PIL import Image, ImageFilter

def apply_filters(input_path, output_path):
    # Open the image
    img = Image.open(input_path)

    # Apply filters
    filtered_img = img.filter(ImageFilter.BLUR)
    filtered_img = filtered_img.filter(ImageFilter.CONTOUR)
    filtered_img = filtered_img.filter(ImageFilter.EDGE_ENHANCE)

    # Save the result
    filtered_img.save(output_path)

# Example usage:
input_image = "path/to/your/input_image.jpg"
output_image = "path/to/your/output_image.jpg"

# Call the function
apply_filters(input_image, output_image)
```

Replace `"path/to/your/input_image.jpg"` and `"path/to/your/output_image.jpg"` with the actual paths for your input and output images.

In this example, I've applied a few standard filters like BLUR, CONTOUR, and EDGE_ENHANCE. You can experiment with other filters provided by the `ImageFilter` module in Pillow.

Run the script, and it will apply the specified filters to the image and save the result. Adjust the filters according to your preferences and requirements.

---
### 4.3. Create image thumbnails
To create image thumbnails in Python, you can use the Pillow (PIL) library. Here's a simple script to generate thumbnails from an image:

```python
from PIL import Image

def create_thumbnail(input_path, output_path, thumbnail_size=(100, 100)):
    # Open the image
    img = Image.open(input_path)

    # Create a thumbnail
    img.thumbnail(thumbnail_size)

    # Save the thumbnail
    img.save(output_path)

# Example usage:
input_image = "path/to/your/input_image.jpg"
output_thumbnail = "path/to/your/output_thumbnail.jpg"

# Call the function
create_thumbnail(input_image, output_thumbnail)
```

Replace `"path/to/your/input_image.jpg"` and `"path/to/your/output_thumbnail.jpg"` with the actual paths for your input image and the desired output thumbnail.

In this example, a thumbnail size of (100, 100) pixels is used, but you can adjust the `thumbnail_size` parameter according to your requirements.

Run the script, and it will generate a thumbnail of the specified size and save it to the output path.

---
### 4.4. Extract text from images using OCR
To extract text from images using Optical Character Recognition (OCR) in Python, you can use the Tesseract OCR engine along with the `pytesseract` library. Additionally, you'll need to have Tesseract installed on your machine.

Here's an example script to perform OCR on an image:

```python
from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    # Open the image using Pillow (PIL)
    img = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text

# Example usage:
image_path = "path/to/your/image.jpg"

# Call the function
result_text = extract_text_from_image(image_path)

# Print the extracted text
print("Extracted Text:")
print(result_text)
```

Replace `"path/to/your/image.jpg"` with the actual path to your image.

Before running this script, make sure to install the required libraries:

```bash
pip install pillow pytesseract
```

Also, you need to have Tesseract installed on your machine. You can download it from the official GitHub repository: https://github.com/tesseract-ocr/tesseract

After installing Tesseract, you might need to specify its executable path in your script. Update the `pytesseract.pytesseract.tesseract_cmd` variable accordingly:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Example path for Windows
```

Adjust the path based on your operating system. Once everything is set up, run the script, and it will print the extracted text from the image.

---
### 4.5. Watermark images with a logo or text
To watermark images with a logo or text in Python, you can use the `PIL` (Pillow) library for image processing. Below is an example script that demonstrates how to add a watermark to an image:

```python
from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text):
    # Open the input image
    original_image = Image.open(input_image_path)

    # Create a copy of the original image to avoid modifying it directly
    watermarked_image = original_image.copy()

    # Initialize ImageDraw for drawing on the image
    draw = ImageDraw.Draw(watermarked_image)

    # Set watermark text font and size
    font = ImageFont.load_default()

    # Set watermark text color and opacity
    text_color = (255, 255, 255)  # White
    text_opacity = 100  # Opacity level (0-255)

    # Calculate watermark position (you can adjust the position as needed)
    watermark_position = (10, 10)

    # Add text watermark to the image
    draw.text(watermark_position, watermark_text, font=font, fill=text_color + (text_opacity,))

    # Save the watermarked image
    watermarked_image.save(output_image_path)

if __name__ == "__main__":
    # Example usage:
    input_image_path = "path/to/your/image.jpg"
    output_image_path = "path/to/output/watermarked_image.jpg"
    watermark_text = "Your Watermark"

    add_watermark(input_image_path, output_image_path, watermark_text)
```

Replace `"path/to/your/image.jpg"` with the actual path to your input image and `"path/to/output/watermarked_image.jpg"` with the desired path for the watermarked output image. You can also customize the `watermark_text`, font, color, opacity, and position based on your preferences.

Before running the script, make sure to install the Pillow library:

```bash
pip install pillow
```

Run the script, and it will create a new image with the specified watermark text. You can modify the script to add a logo instead of text by loading the logo image and pasting it onto the original image at the desired position.

---

## 5. Text Processing Scripts:

Text Processing Scripts are computational tools designed to manipulate and analyze textual data using programming languages like Python or Java. These scripts can perform a wide range of tasks, from simple text cleaning and formatting to more complex operations like sentiment analysis, natural language processing, and information extraction. They are employed in various applications such as data preprocessing for machine learning, content analysis for social media, and text summarization for information retrieval. Text Processing Scripts play a crucial role in automating and streamlining text-related tasks, enabling researchers, developers, and data scientists to efficiently handle and derive insights from large volumes of textual information across different domains.

### 5.1. Perform sentiment analysis on text data
Sentiment analysis involves determining the sentiment expressed in a piece of text, such as whether it is positive, negative, or neutral. The `nltk` (Natural Language Toolkit) library in Python is commonly used for sentiment analysis. Below is an example script demonstrating how to perform sentiment analysis using `nltk`:

```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    # Initialize the Sentiment Intensity Analyzer
    sia = SentimentIntensityAnalyzer()

    # Get the polarity scores for the text
    sentiment_scores = sia.polarity_scores(text)

    # Determine sentiment based on the compound score
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        sentiment = 'Positive'
    elif compound_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment, sentiment_scores

if __name__ == "__main__":
    # Example usage:
    text_to_analyze = "I love using Python for natural language processing!"

    sentiment_result, scores = analyze_sentiment(text_to_analyze)

    print(f"Text: {text_to_analyze}")
    print(f"Sentiment: {sentiment_result}")
    print(f"Sentiment Scores: {scores}")
```

Before running the script, you need to install the `nltk` library:

```bash
pip install nltk
```

Additionally, you may need to download the `vader_lexicon` data used by the sentiment analyzer:

```python
import nltk
nltk.download('vader_lexicon')
```

Replace the `text_to_analyze` variable with the text you want to analyze. The script will output the sentiment (Positive, Negative, or Neutral) and the sentiment scores, including the compound score that represents the overall sentiment. Adjust the threshold values in the script to customize the sentiment classification based on your preferences.

---
### 5.2. Build a script for text summarization
Text summarization is a complex task, and there are multiple approaches to achieve it. One popular method is to use the `gensim` library, which provides an implementation of the TextRank algorithm for extractive summarization. Here's an example script:

```python
from gensim.summarization import summarize

def summarize_text(text, ratio=0.2):
    """
    Summarize a given text using the TextRank algorithm.

    Parameters:
    - text (str): The input text to be summarized.
    - ratio (float): The ratio of the original text to keep in the summary (default is 0.2).

    Returns:
    - summary (str): The summarized text.
    """
    summary = summarize(text, ratio=ratio)
    return summary

if __name__ == "__main__":
    # Example usage:
    input_text = """
    GPT-3, the latest and largest language model developed by OpenAI, has gained significant attention for its remarkable natural language processing capabilities.
    The model, with its 175 billion parameters, has been applied to various tasks, including text generation, translation, and summarization.
    Text summarization, in particular, is a useful application of GPT-3, allowing for the extraction of key information from lengthy documents.
    """

    summarized_text = summarize_text(input_text)

    print("Original Text:")
    print(input_text)
    print("\nSummarized Text:")
    print(summarized_text)
```

Before running the script, you need to install the `gensim` library:

```bash
pip install gensim
```

Replace the `input_text` variable with the text you want to summarize. The script uses the `summarize` function from `gensim` to perform extractive summarization. The `ratio` parameter determines the proportion of the original text to be retained in the summary. Adjust this parameter as needed.

---
### 5.3. Create a spell-checker or grammar checker
Creating a spell-checker or grammar checker involves using language processing libraries, and one popular choice is the `language_tool_python` library. It's a Python wrapper for the LanguageTool API, which can check grammar and style issues in a given text. Here's an example script:

First, install the library:

```bash
pip install language-tool-python
```

Now, you can create a simple spell-checker/grammar-checker script:

```python
import language_tool_python

def check_text(text):
    """
    Check grammar and spelling in the given text.

    Parameters:
    - text (str): The input text to be checked.

    Returns:
    - matches (list): A list of grammar and spelling suggestions.
    """
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    return matches

def correct_text(text, matches):
    """
    Correct the text based on the grammar and spelling suggestions.

    Parameters:
    - text (str): The input text to be corrected.
    - matches (list): A list of grammar and spelling suggestions.

    Returns:
    - corrected_text (str): The corrected text.
    """
    corrected_text = language_tool_python.correct(text, matches)
    return corrected_text

if __name__ == "__main__":
    # Example usage:
    input_text = "This is an example sentence with some grammatical and spel mistakes."

    # Check the text
    matches = check_text(input_text)

    if matches:
        print("Grammar and spelling issues found:")
        for match in matches:
            print(match)

        # Correct the text
        corrected_text = correct_text(input_text, matches)
        print("\nCorrected Text:")
        print(corrected_text)
    else:
        print("No grammar or spelling issues found.")
```

Replace the `input_text` variable with the text you want to check. The script uses the `LanguageTool` class to check the text and provides a list of matches (grammar and spelling issues). It then uses the `correct` function to correct the text based on the suggestions. Adjust the language code ('en-US' in this case) based on your requirements.

---
### 5.4. Convert text to speech or speech to text
To convert text to speech or speech to text in Python, you can use libraries such as `gTTS` (Google Text-to-Speech) for text-to-speech conversion and `SpeechRecognition` for speech-to-text conversion. Here's how you can do both:

__Text to Speech (TTS):__

Install the `gTTS` library:

```bash
pip install gtts
```

Now, you can create a simple script for text-to-speech conversion:

```python
from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    """
    Convert text to speech.

    Parameters:
    - text (str): The input text to be converted.
    - language (str): The language code (default is 'en').

    Returns:
    - audio_path (str): The path to the generated audio file.
    """
    tts = gTTS(text=text, lang=language)
    audio_path = 'output.mp3'
    tts.save(audio_path)
    return audio_path

if __name__ == "__main__":
    input_text = "Hello, how are you today?"

    # Convert text to speech
    audio_path = text_to_speech(input_text)

    # Play the generated audio file
    os.system(f"start {audio_path}")
```

Replace `input_text` with the text you want to convert. The script uses `gTTS` to create an audio file (`output.mp3`) and plays it using the default audio player.

__Speech to Text (STT):__

Install the `SpeechRecognition` library:

```bash
pip install SpeechRecognition
```

You'll also need to install the `pyaudio` library for microphone input:

```bash
pip install pyaudio
```

Now, create a script for speech-to-text conversion:

```python
import speech_recognition as sr

def speech_to_text():
    """
    Convert speech to text using the microphone.

    Returns:
    - text (str): The recognized text.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

if __name__ == "__main__":
    # Convert speech to text
    recognized_text = speech_to_text()
```

This script uses the `SpeechRecognition` library to capture audio from the microphone and recognize speech using the Google Speech Recognition service. Adjust the microphone input settings as needed.

---
### 5.5. Generate random text for testing purposes
You can use the `LoremText` module from the `faker` library to generate random text for testing purposes in Python. First, you need to install the `faker` library:

```bash
pip install faker
```

Now, you can create a script to generate random text:

```python
from faker import Faker

def generate_random_text(paragraphs=3, sentences_per_paragraph=5):
    """
    Generate random text for testing purposes.

    Parameters:
    - paragraphs (int): Number of paragraphs (default is 3).
    - sentences_per_paragraph (int): Number of sentences per paragraph (default is 5).

    Returns:
    - random_text (str): The generated random text.
    """
    fake = Faker()
    fake.seed(0)  # Set seed for reproducibility

    random_text = "\n".join(
        fake.paragraph(nb_sentences=sentences_per_paragraph) for _ in range(paragraphs)
    )

    return random_text

if __name__ == "__main__":
    # Generate random text
    text = generate_random_text()

    # Print the generated text
    print(text)
```

Adjust the `paragraphs` and `sentences_per_paragraph` parameters as needed. The `Faker` library allows you to generate various types of fake data, and in this case, we're using it to create random paragraphs. The `seed(0)` line ensures reproducibility if you want to generate the same random text later.

---
## 6. File Management Scripts:

File Management Scripts are automation tools developed using programming languages like Python or Bash to perform various tasks related to file organization, manipulation, and maintenance. These scripts can encompass functionalities such as sorting and organizing files within directories, searching for specific file types or patterns, removing duplicate files, and monitoring changes in file directories. File Management Scripts are invaluable for streamlining routine file-related operations, enhancing efficiency in tasks like data cleanup, and ensuring the structured organization of digital assets. They provide users with the ability to automate repetitive file management chores, saving time and reducing the likelihood of errors in handling large volumes of data and documents.

### 6.1. Sort and organize files in a directory
To sort and organize files in a directory using Python, you can use the `os` and `shutil` modules. Here's a simple example script that sorts files based on their extensions and organizes them into corresponding folders:

```python
import os
import shutil

def organize_files(source_directory, destination_directory):
    """
    Organize files in the source directory and move them to corresponding folders
    based on their file extensions in the destination directory.

    Parameters:
    - source_directory (str): Path to the source directory.
    - destination_directory (str): Path to the destination directory.
    """
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Iterate over files in the source directory
    for filename in os.listdir(source_directory):
        source_path = os.path.join(source_directory, filename)

        # Check if it's a file
        if os.path.isfile(source_path):
            # Get the file extension
            _, extension = os.path.splitext(filename)

            # Remove the dot from the extension
            extension = extension[1:]

            # Create a folder for the extension if it doesn't exist
            extension_folder = os.path.join(destination_directory, extension)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            # Move the file to the corresponding folder
            destination_path = os.path.join(extension_folder, filename)
            shutil.move(source_path, destination_path)

if __name__ == "__main__":
    # Specify source and destination directories
    source_dir = "/path/to/source/directory"
    destination_dir = "/path/to/destination/directory"

    # Organize files
    organize_files(source_dir, destination_dir)
```

Replace "/path/to/source/directory" and "/path/to/destination/directory" with the actual paths of your source and destination directories. This script will create subdirectories in the destination directory based on file extensions and move the files accordingly. Adjust the script based on your specific needs and preferences.

---
### 6.2. Search for files with specific extensions
To search for files with specific extensions in a directory using Python, you can use the `os` module. Here's a simple script that demonstrates how to do this:

```python
import os

def search_files(directory, extensions):
    """
    Search for files with specific extensions in a directory.

    Parameters:
    - directory (str): Path to the directory to search.
    - extensions (list): List of file extensions to look for.

    Returns:
    - List of file paths matching the specified extensions.
    """
    matching_files = []

    # Iterate over files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file has a matching extension
            if any(file.lower().endswith(ext.lower()) for ext in extensions):
                file_path = os.path.join(root, file)
                matching_files.append(file_path)

    return matching_files

if __name__ == "__main__":
    # Specify the directory and extensions to search for
    search_directory = "/path/to/search/directory"
    desired_extensions = [".txt", ".pdf", ".docx"]

    # Search for files
    result_files = search_files(search_directory, desired_extensions)

    # Print the matching file paths
    if result_files:
        print("Matching files:")
        for file_path in result_files:
            print(file_path)
    else:
        print("No matching files found.")
```

Replace "/path/to/search/directory" with the actual path of the directory you want to search, and modify the `desired_extensions` list to include the file extensions you're interested in. This script will recursively search for files with the specified extensions in the given directory and its subdirectories.

Feel free to customize the script based on your specific requirements.

---
### 6.3. Clean up duplicate files
Cleaning up duplicate files in a directory can be achieved by comparing file contents and removing redundant copies. Here's a Python script that identifies and removes duplicate files based on their content:

```python
import os
import hashlib

def hash_file(file_path, block_size=65536):
    """
    Generate the hash of a file.

    Parameters:
    - file_path (str): Path to the file.
    - block_size (int): Block size for reading the file.

    Returns:
    - Hexadecimal representation of the file hash.
    """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read(block_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file.read(block_size)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    """
    Find duplicate files in a directory.

    Parameters:
    - directory (str): Path to the directory.

    Returns:
    - Dictionary where keys are file hashes and values are lists of file paths.
    """
    file_hash_dict = {}
    duplicate_files = {}

    # Iterate over files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)

            # Check if the hash is already in the dictionary
            if file_hash in file_hash_dict:
                # Duplicate found
                if file_hash not in duplicate_files:
                    duplicate_files[file_hash] = [file_hash_dict[file_hash]]
                duplicate_files[file_hash].append(file_path)
            else:
                file_hash_dict[file_hash] = file_path

    return duplicate_files

def remove_duplicates(duplicate_files):
    """
    Remove duplicate files.

    Parameters:
    - duplicate_files (dict): Dictionary with duplicate file information.
    """
    for file_hash, duplicates in duplicate_files.items():
        # Keep the first file and remove duplicates
        for duplicate in duplicates[1:]:
            os.remove(duplicate)
            print(f"Removed duplicate: {duplicate}")

if __name__ == "__main__":
    # Specify the directory to search for duplicates
    search_directory = "/path/to/search/directory"

    # Find duplicate files
    duplicates = find_duplicate_files(search_directory)

    # Remove duplicates
    if duplicates:
        print("Duplicate files found:")
        for file_hash, files in duplicates.items():
            print(f"Hash: {file_hash}")
            for file_path in files:
                print(f"  {file_path}")
        remove_duplicates(duplicates)
    else:
        print("No duplicate files found.")
```

Replace "/path/to/search/directory" with the actual path of the directory you want to search for duplicates. This script uses MD5 hashing to compare file contents and removes redundant copies while keeping the first occurrence. Please use it with caution and make sure to have backups before running it on valuable data.

---
### 6.4. Monitor changes in file directories
Monitoring changes in file directories can be achieved using the `watchdog` library in Python. This library provides a simple API for monitoring file system events. You can install it using:

```bash
pip install watchdog
```

Here's an example script that monitors a directory for file system events:

```python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        # File modified
        print(f'File {event.src_path} has been modified')

    def on_created(self, event):
        if event.is_directory:
            return
        # File created
        print(f'File {event.src_path} has been created')

    def on_deleted(self, event):
        if event.is_directory:
            return
        # File deleted
        print(f'File {event.src_path} has been deleted')

if __name__ == "__main__":
    path = "/path/to/directory/to/monitor"

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

Replace "/path/to/directory/to/monitor" with the actual path of the directory you want to monitor. This script will print messages when files are modified, created, or deleted within the specified directory.

Make sure to adapt the script according to your specific use case. You can extend the `MyHandler` class to include additional event handling methods if needed.

---
### 6.5. Rename files in bulk according to a pattern
To rename files in bulk according to a pattern in Python, you can use the `os` module for interacting with the file system and the `re` module for regular expressions. Here's an example script that renames files in a directory based on a specified pattern:

```python
import os
import re

def rename_files(directory, pattern):
    # Get the list of files in the directory
    files = os.listdir(directory)

    # Compile the regular expression pattern
    regex_pattern = re.compile(pattern)

    for filename in files:
        # Check if the filename matches the pattern
        match = regex_pattern.match(filename)
        if match:
            # Construct the new filename based on the pattern
            new_filename = match.group(1)  # Adjust this line based on your pattern
            new_filepath = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(os.path.join(directory, filename), new_filepath)
            print(f'Renamed: {filename} to {new_filename}')

if __name__ == "__main__":
    # Specify the directory and pattern
    directory_to_rename = "/path/to/directory"
    renaming_pattern = r'your_pattern_(\d+)\.txt'  # Adjust this pattern based on your needs

    # Call the rename_files function
    rename_files(directory_to_rename, renaming_pattern)
```

Replace "/path/to/directory" with the actual path of the directory containing the files you want to rename. Adjust the `renaming_pattern` variable according to the pattern you want to match. The example pattern assumes you want to extract numbers from filenames, but you should customize it based on your specific requirements.

Make sure to review and understand the regular expression and adjust it to match your file naming pattern accurately. Always back up your files before running any script that modifies file names.

---
## 7. System Monitoring and Reporting Scripts:

System Monitoring and Reporting Scripts are powerful tools developed using languages like Python or Bash to track and analyze various aspects of a computer system's performance. These scripts actively monitor critical system resources such as CPU usage, memory utilization, and disk activity. They can generate regular reports summarizing system statistics on a daily or weekly basis, providing insights into resource trends and potential issues. Additionally, these scripts may include functionalities to log and analyze system events, check network traffic, and ensure system uptime. By automating these monitoring tasks, System Monitoring and Reporting Scripts empower users to proactively manage their systems, identify potential bottlenecks or failures, and maintain optimal performance.

### 7.1. Monitor system resource usage (CPU, memory, disk)
To monitor system resource usage (CPU, memory, disk) with Python, you can use third-party libraries like psutil. Here's a simple example script that shows how to use psutil to monitor these resources:

```python
import psutil
import time

def monitor_resources():
    while True:
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)

        # Memory usage
        memory_info = psutil.virtual_memory()
        used_memory = memory_info.used
        total_memory = memory_info.total
        memory_percent = memory_info.percent

        # Disk usage
        disk_info = psutil.disk_usage('/')
        used_disk = disk_info.used
        total_disk = disk_info.total
        disk_percent = disk_info.percent

        # Print the information
        print(f"CPU Usage: {cpu_percent}%")
        print(f"Memory Usage: {used_memory / (1024 ** 3):.2f} GB / {total_memory / (1024 ** 3):.2f} GB ({memory_percent}%)")
        print(f"Disk Usage: {used_disk / (1024 ** 3):.2f} GB / {total_disk / (1024 ** 3):.2f} GB ({disk_percent}%)")

        # Sleep for a while before checking again
        time.sleep(5)

if __name__ == "__main__":
    monitor_resources()
```

This script uses the `psutil` library to retrieve CPU, memory, and disk usage information. The `psutil.cpu_percent` function is used to get the CPU usage percentage, and the `psutil.virtual_memory` and `psutil.disk_usage` functions provide information about memory and disk usage, respectively.

The script runs in an infinite loop, printing the resource usage information every 5 seconds. You can customize the interval or add additional functionality based on your specific requirements. To use this script, you'll need to install the psutil library by running:

```bash
pip install psutil
```

Make sure to adapt the script according to your needs, and keep in mind that it may require administrative privileges to access certain system information.

---
### 7.2. Generate daily/weekly reports on system statistics
To generate daily or weekly reports on system statistics using Python, you can modify the script provided earlier to write the information to a file. Here's an example that writes daily reports to a text file:

```python
import psutil
import time
from datetime import datetime, timedelta

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_report(report_path, content):
    with open(report_path, 'a') as file:
        file.write(content + '\n')

def monitor_and_report(report_path):
    while True:
        timestamp = get_timestamp()

        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)

        # Memory usage
        memory_info = psutil.virtual_memory()
        used_memory = memory_info.used
        total_memory = memory_info.total
        memory_percent = memory_info.percent

        # Disk usage
        disk_info = psutil.disk_usage('/')
        used_disk = disk_info.used
        total_disk = disk_info.total
        disk_percent = disk_info.percent

        # Prepare the report content
        report_content = (
            f"Timestamp: {timestamp}\n"
            f"CPU Usage: {cpu_percent}%\n"
            f"Memory Usage: {used_memory / (1024 ** 3):.2f} GB / {total_memory / (1024 ** 3):.2f} GB ({memory_percent}%)\n"
            f"Disk Usage: {used_disk / (1024 ** 3):.2f} GB / {total_disk / (1024 ** 3):.2f} GB ({disk_percent}%)\n"
        )

        # Write the report to the file
        write_report(report_path, report_content)

        # Sleep for 24 hours (86400 seconds) before generating the next report
        time.sleep(86400)

if __name__ == "__main__":
    daily_report_path = 'daily_system_report.txt'
    monitor_and_report(daily_report_path)
```

This script continuously monitors system statistics and appends the collected information to a text file (`daily_system_report.txt`). You can adjust the file path and customize the report content as needed.

Keep in mind that this script will run indefinitely, generating a report once per day. You can modify the sleep duration to adjust the reporting frequency. Additionally, you may want to consider using a more structured format for the reports, such as CSV or JSON, depending on your reporting needs.

---
### 7.3. Monitor network traffic and generate reports
Monitoring network traffic and generating reports can be done using Python with the help of external libraries such as `psutil` and `scapy`. Below is a basic example to get you started. Please note that you need to install the `psutil` and `scapy` libraries if you haven't already:

```bash
pip install psutil scapy
```

Now, you can use the following Python script to monitor network traffic and generate reports:

```python
import psutil
from scapy.all import sniff

def get_network_usage():
    # Get current network statistics
    network_stats = psutil.net_io_counters()
    bytes_sent = network_stats.bytes_sent
    bytes_received = network_stats.bytes_recv

    return bytes_sent, bytes_received

def packet_callback(packet):
    # Handle each packet received during sniffing
    if packet.haslayer("IP"):
        # Extract source and destination IP addresses
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst

        # You can perform further analysis or logging here

def monitor_network(report_path):
    while True:
        # Get network usage before sniffing
        initial_sent, initial_received = get_network_usage()

        # Sniff packets for a specific duration (e.g., 60 seconds)
        sniff(prn=packet_callback, store=0, timeout=60)

        # Get network usage after sniffing
        final_sent, final_received = get_network_usage()

        # Calculate the difference in bytes
        sent_diff = final_sent - initial_sent
        received_diff = final_received - initial_received

        # Prepare the report content
        report_content = (
            f"Bytes Sent: {sent_diff}\n"
            f"Bytes Received: {received_diff}\n"
        )

        # Write the report to the file
        with open(report_path, 'a') as file:
            file.write(report_content + '\n')

if __name__ == "__main__":
    network_report_path = 'network_traffic_report.txt'
    monitor_network(network_report_path)
```

This script continuously monitors network traffic for a specified duration (60 seconds in this case) and logs the difference in bytes sent and received during that period. It uses the `psutil` library to obtain initial and final network statistics and `scapy` for packet sniffing.

Note: Sniffing network traffic may require elevated privileges. Ensure that you have the necessary permissions to capture packets on your network. Also, this script provides a basic example, and you may need to customize it based on your specific reporting requirements.

---
### 7.4. Create a script to log and analyze system events
To log and analyze system events in Python, you can use the `psutil` library to gather system information and the `logging` module to create log entries. Here's a simple script that logs CPU and memory usage at regular intervals:

```python
import psutil
import logging
import time

# Configure logging
logging.basicConfig(filename='system_events.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def log_system_stats():
    # Get CPU and memory usage
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_stats = psutil.virtual_memory()

    # Log the information
    logging.info(f"CPU Usage: {cpu_percent}% | Memory Usage: {memory_stats.percent}%")

if __name__ == "__main__":
    try:
        # Log system stats every 5 minutes
        while True:
            log_system_stats()
            time.sleep(300)  # 300 seconds = 5 minutes

    except KeyboardInterrupt:
        print("Logging stopped.")
```

This script logs CPU and memory usage information every 5 minutes and stores it in a file named `system_events.log`. You can customize the logging interval and add more system metrics as needed.

To analyze the logs, you can use various tools or write additional Python scripts to parse and extract specific information from the log file.

Keep in mind that this is a basic example, and you might want to extend it based on your specific needs. Additionally, you can explore more advanced logging frameworks like `loguru` or integrate with external services for log analysis.

---
### 7.5. Build a script to track and notify about system uptime
To track and notify about system uptime using Python, you can create a script that periodically checks the system uptime and sends notifications when certain conditions are met. Here's a simple example using the `psutil` library for system information and the `smtplib` library for sending email notifications:

```python
import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Email configuration
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@gmail.com"
email_password = "your_email_password"

def send_notification(subject, message):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the message body
    body = MIMEText(message)
    message.attach(body)

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, email_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

def track_system_uptime():
    # Notify if the system uptime is greater than 24 hours
    while True:
        uptime = psutil.boot_time()
        current_time = time.time()
        uptime_hours = (current_time - uptime) / 3600

        if uptime_hours >= 24:
            subject = "System Uptime Notification"
            message = f"System has been running for {uptime_hours:.2f} hours."
            send_notification(subject, message)

        time.sleep(3600)  # Check every hour

if __name__ == "__main__":
    track_system_uptime()
```

This script checks the system uptime every hour and sends an email notification if the uptime exceeds 24 hours. Make sure to replace the placeholder email addresses and password with your actual email credentials.

Note: For security reasons, consider using environment variables or a configuration file to store sensitive information like email credentials.

Additionally, you may explore other notification mechanisms, such as sending messages via a messaging service (e.g., Telegram, Slack) or using a desktop notification library. Adjust the script according to your preferred notification method.


----
## 8. Games and Entertainment Scripts:

Games and Entertainment Scripts are dynamic applications designed to provide users with engaging and enjoyable experiences. Developed using languages such as Python or JavaScript, these scripts cover a wide range of interactive content, including text-based games, simulations, and multimedia entertainment. They often incorporate elements of graphics, sound, and user interaction to create immersive virtual environments. Whether it's a text-based adventure game, a random joke generator, or a trivia quiz, these scripts add an element of fun and amusement to users' computing experiences. Games and Entertainment Scripts cater to a diverse audience, offering a break from routine tasks and providing a source of recreational enjoyment within the digital realm.

### 8.1. Create a simple text-based game
This is a guessing game where the player needs to guess a randomly generated number:

```python
import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    while True:
        # Get the player's guess
        guess = int(input("Your guess: "))
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    guess_the_number()
```

Copy and paste this code into a Python file (e.g., `guessing_game.py`) and run it. The player will be prompted to guess the randomly generated number, and the game will provide hints if the guess is too high or too low. The game continues until the correct number is guessed.

Feel free to modify the game or add more features to make it more interesting!

---
### 8.2. Build a script to generate random jokes or facts
Here's a simple Python script that generates random jokes and facts. This example uses predefined lists of jokes and facts, and it randomly selects one each time the script is run:

```python
import random

def generate_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she should embrace her mistakes. She gave me a hug.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I used to play piano by ear, but now I use my hands and fingers.",
    ]

    return random.choice(jokes)

def generate_random_fact():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "The Eiffel Tower can be 15 cm taller during the summer, due to the expansion of the iron in the heat.",
        "Bananas are berries, but strawberries aren't.",
        "Cows have best friends and can become stressed when they are separated.",
        "A group of flamingos is called a 'flamboyance.'",
    ]

    return random.choice(facts)

if __name__ == "__main__":
    joke_or_fact = random.choice(["joke", "fact"])

    if joke_or_fact == "joke":
        print("Here's a random joke for you:")
        print(generate_random_joke())
    else:
        print("Here's a random fact for you:")
        print(generate_random_fact())
```

Copy and paste this code into a Python file (e.g., `random_joke_or_fact.py`) and run it. It will print either a random joke or a random fact each time you run the script.

Feel free to expand and customize the lists of jokes and facts to suit your preferences!

---
### 8.3. Design a quiz or trivia game
Creating a quiz or trivia game in Python can be a fun project! Here's a simple example using Python:

```python
import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question):
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the option number): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question["options"]):
            user_answer_index = int(user_answer) - 1
            if question["options"][user_answer_index] == question["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {question['answer']}\n")
        else:
            print("Invalid input. Please enter a valid option number.\n")

    def start_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            self.ask_question(question)

        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    # Define your quiz questions
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris",
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars",
        },
        # Add more questions as needed
    ]

    # Create an instance of the Quiz class
    my_quiz = Quiz(quiz_questions)

    # Start the quiz
    my_quiz.start_quiz()
```

Copy and paste this code into a Python file (e.g., `quiz_game.py`) and run it. You can customize the questions, options, and correct answers in the `quiz_questions` list. The game will shuffle the questions and ask the user to select the correct option for each question.

Feel free to expand and customize the quiz with more features, difficulty levels, or categories!

---
### 8.4. Develop a script for generating random art
Creating a script for generating random art in Python can be a creative and fun project. One approach is to use the `turtle` module, which provides a simple way to draw shapes and patterns. Here's a basic example:

```python
import turtle
import random

def random_color():
    return (random.random(), random.random(), random.random())

def draw_random_art():
    turtle.speed(2)
    turtle.bgcolor("black")

    for _ in range(50):
        turtle.color(random_color())
        draw_random_shape()

    turtle.done()

def draw_random_shape():
    shape = random.choice(["circle", "square", "triangle"])
    size = random.randint(10, 100)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    if shape == "circle":
        turtle.circle(size)
    elif shape == "square":
        for _ in range(4):
            turtle.forward(size)
            turtle.right(90)
    elif shape == "triangle":
        for _ in range(3):
            turtle.forward(size)
            turtle.right(120)

if __name__ == "__main__":
    draw_random_art()
```

This script uses the `turtle` module to draw random shapes (circles, squares, or triangles) with random colors. The `random_color` function generates a random RGB color. You can customize this script by adding more shapes, adjusting sizes, or incorporating different drawing techniques.

Run this script, and a turtle graphics window will appear, drawing random art. Feel free to experiment and enhance the script to create more complex and visually appealing artwork.

---
### 8.5. Create a script to simulate rolling dice

```python
import random

def roll_dice(num_rolls=1, num_sides=6):
    results = []
    for _ in range(num_rolls):
        result = random.randint(1, num_sides)
        results.append(result)
    return results

def main():
    num_rolls = int(input("Enter the number of times you want to roll the dice: "))
    num_sides = int(input("Enter the number of sides on the dice: "))

    results = roll_dice(num_rolls, num_sides)

    print("Results:")
    for i, result in enumerate(results, start=1):
        print(f"Roll {i}: {result}")

if __name__ == "__main__":
    main()
```

This script defines a `roll_dice` function that takes the number of rolls and the number of sides on the dice as parameters and returns a list of results. The `main` function takes user input for the number of rolls and sides, calls the `roll_dice` function, and prints the results.

To run this script, copy and paste it into a Python environment, execute it, and follow the prompts to input the number of rolls and sides on the dice. The script will then simulate rolling the dice and display the results.

---
## 9. Utility Scripts:

Utility Scripts are versatile tools developed to streamline various tasks, enhance efficiency, and automate routine processes. Crafted using programming languages like Python or Bash, these scripts address a broad spectrum of functionalities, ranging from file management and data analysis to system monitoring and automation. Utility Scripts aim to simplify complex operations, minimize manual efforts, and contribute to a smoother workflow. Whether it's automating backups, sorting files, generating strong passwords, or managing system resources, these scripts serve as handy assistants, providing users with practical solutions to common challenges. Utility Scripts are designed to be flexible and adaptable, offering a diverse set of functionalities to cater to different user needs and scenarios.

### 9.1. Calculate and convert units (e.g., currency exchange rates)
To calculate and convert units, including currency exchange rates, you can use various Python libraries. Here's a simple example using the `forex-python` library for currency conversion:

First, you need to install the library:

```bash
pip install forex-python
```

Now, you can use the following Python script:

```python
from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency code: ").upper()
    to_currency = input("Enter the target currency code: ").upper()

    result = convert_currency(amount, from_currency, to_currency)

    print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()
```

This script defines a function `convert_currency` that takes an amount, source currency, and target currency, and returns the converted amount. The `main` function takes user input for the amount and currencies and then displays the converted amount.

Feel free to adapt this script based on your specific unit conversion needs.

---
### 9.2. Create a script for generating strong passwords

```python
import random
import string

def generate_password(length=12):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the password to randomize character positions
    random.shuffle(password)

    # Convert the list of characters to a string
    return ''.join(password)

def main():
    # Set the desired password length
    password_length = 16

    # Generate a strong password
    password = generate_password(password_length)

    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
```

This script defines a function `generate_password` that creates a strong password by combining lowercase letters, uppercase letters, digits, and special characters. The `main` function sets the desired password length (you can modify it), generates a password, and prints it.

Feel free to adjust the script based on your specific requirements for password length or character sets.

---
### 9.3. Build a simple calculator

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in {'1', '2', '3', '4'}:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input. Please enter a valid number (1/2/3/4).")

if __name__ == "__main__":
    calculator()
```

This script defines basic arithmetic functions (`add`, `subtract`, `multiply`, and `divide`) and a `calculator` function that takes user input to perform the selected operation. It includes input validation to handle invalid choices or division by zero.

Run the script, and it will prompt you to select an operation and enter two numbers. It will then perform the chosen operation and display the result.

---
### 9.4. Convert between different file formats (e.g., PDF to text)
To convert a PDF to text in Python, you can use the `PyPDF2` library. First, you'll need to install the library using:

```bash
pip install PyPDF2
```

Now, you can use the following script to convert a PDF to text:

```python
import PyPDF2

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

    return text

if __name__ == "__main__":
    pdf_path = "path/to/your/file.pdf"  # Replace with the path to your PDF file
    extracted_text = pdf_to_text(pdf_path)

    print(extracted_text)
```

Replace `"path/to/your/file.pdf"` with the actual path to your PDF file. This script uses `PyPDF2` to extract text from each page of the PDF and concatenates it into a single string.

Keep in mind that the text extraction might not be perfect, especially for complex PDFs with images or non-standard fonts. For more advanced PDF processing, you might want to explore other libraries like `pdfminer` or `PyMuPDF` (MuPDF).

---
### 9.5. Implement a URL shortener
Creating a URL shortener involves generating a unique code for each URL and storing the mapping between the code and the original URL. Below is a simple example of a URL shortener using Python and the Flask web framework. You'll need to install Flask first:

```bash
pip install Flask
```

Now, you can create a basic URL shortener with the following code:

```python
from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)

# Dictionary to store the mapping between short codes and URLs
url_mapping = {}

# Function to generate a random short code
def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(6))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('url')

    # Check if the URL is already shortened
    for short_code, url in url_mapping.items():
        if url == original_url:
            return render_template('index.html', short_url=f"{request.host_url}{short_code}")

    # Generate a new short code
    short_code = generate_short_code()

    # Store the mapping
    url_mapping[short_code] = original_url

    short_url = f"{request.host_url}{short_code}"

    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_original(short_code):
    # Redirect to the original URL if the short code exists
    original_url = url_mapping.get(short_code)
    if original_url:
        return redirect(original_url)
    else:
        return render_template('index.html', error="Short URL not found")

if __name__ == '__main__':
    app.run(debug=True)
```

Save this script as `app.py`. This example uses Flask for the web application. Run the script, and the URL shortener will be available at `http://127.0.0.1:5000/`.

This is a basic implementation, and it's essential to handle issues like collisions (two URLs generating the same short code) and persistence (storing the mappings in a database for durability). For a production environment, consider using a database like SQLite or a more robust web framework.

---
## 10. Network and Internet Scripts:

Network and Internet Scripts play a crucial role in managing, optimizing, and securing online connectivity and data transfer. These scripts are developed using programming languages like Python or Perl to automate tasks related to network administration, monitoring, and interaction with web services. They can be employed for a variety of purposes, such as monitoring website availability, analyzing network traffic, performing security-related tasks like port scanning, and automating interactions with web APIs. Network and Internet Scripts empower users to efficiently handle networking operations, troubleshoot issues, and enhance the performance and security of their online activities. These scripts contribute to a more streamlined and responsive network infrastructure, ensuring reliable connectivity and effective communication between devices and services across the internet.

### 10.1. Ping multiple hosts to check their status
To ping multiple hosts and check their status using Python, you can use the `ping3` library. First, you'll need to install the library:

```bash
pip install ping3
```

Then, you can use the following Python script to ping multiple hosts:

```python
import subprocess
from ping3 import ping, verbose_ping

def ping_hosts(hosts):
    results = {}

    for host in hosts:
        try:
            response = ping(host, timeout=2)
            if response is not None:
                results[host] = "Online"
            else:
                results[host] = "Offline"
        except Exception as e:
            results[host] = f"Error: {str(e)}"

    return results

if __name__ == "__main__":
    # List of hosts to ping
    host_list = ["google.com", "example.com", "nonexistenthost123.com"]

    # Ping the hosts and get the results
    results = ping_hosts(host_list)

    # Display the results
    for host, status in results.items():
        print(f"{host}: {status}")
```

This script defines a function `ping_hosts` that takes a list of hostnames or IP addresses, pings each host, and returns a dictionary indicating whether each host is online or offline.

Note that the `ping3` library may not work on all operating systems due to differences in the availability of ICMP ping requests. If you encounter issues or limitations, you might need to consider other approaches, such as using the `subprocess` module to call the system's ping command. Keep in mind that running subprocess commands may have security implications, so make sure to validate and sanitize inputs if they come from untrusted sources.

---
### 10.2. Monitor website availability and response times
To monitor website availability and response times with Python, you can use the `requests` library to send HTTP requests and measure the time it takes to receive a response. Additionally, you can schedule these checks at regular intervals using a library like `schedule` to create a basic website monitoring script. Here's a simple example:

```python
import requests
import schedule
import time

def check_website(url):
    try:
        # Record the start time
        start_time = time.time()

        # Send a GET request to the website
        response = requests.get(url)

        # Calculate the response time
        response_time = time.time() - start_time

        # Print the results
        print(f"Website: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response_time:.2f} seconds")
        print("")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("")

def job():
    # Replace 'https://example.com' with the URL you want to monitor
    website_url = 'https://example.com'

    # Check the website
    check_website(website_url)

# Schedule the job to run every 5 minutes
schedule.every(5).minutes.do(job)

if __name__ == "__main__":
    # Run the scheduled jobs
    while True:
        schedule.run_pending()
        time.sleep(1)
```

This script defines a `check_website` function that sends a GET request to the specified URL using the `requests` library, measures the response time, and prints the results. The `job` function is scheduled to run every 5 minutes using the `schedule` library.

Replace the `website_url` variable with the URL of the website you want to monitor. Make sure to install the `requests` and `schedule` libraries if you haven't already:

```bash
pip install requests schedule
```

Run the script, and it will periodically check the specified website's availability and response times. You can customize the script further based on your specific monitoring requirements.

---
### 10.3. Retrieve and analyze website headers
To retrieve and analyze website headers with Python, you can use the `requests` library to send HTTP requests and inspect the response headers. Additionally, you can use the `http.client` library for more detailed analysis. Here's an example script:

```python
import requests
import http.client

def get_headers(url):
    try:
        # Send a HEAD request to retrieve headers only
        response = requests.head(url)

        # Print the status code
        print(f"Status Code: {response.status_code}")

        # Print the response headers
        print("\nResponse Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        # Analyze headers using http.client
        analyze_headers(response.headers)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def analyze_headers(headers):
    # Extract and analyze specific headers
    server = headers.get('server', 'N/A')
    content_type = headers.get('content-type', 'N/A')

    print("\nAnalysis:")
    print(f"Server: {server}")
    print(f"Content Type: {content_type}")

if __name__ == "__main__":
    # Replace 'https://example.com' with the URL you want to analyze
    url = 'https://example.com'

    # Retrieve and analyze headers
    get_headers(url)
```

This script defines a `get_headers` function that sends a HEAD request to the specified URL using the `requests` library. It then prints the status code and response headers. The `analyze_headers` function extracts and analyzes specific headers, such as the server and content type.

Replace the `url` variable with the URL of the website you want to analyze. Make sure to install the `requests` library if you haven't already:

```bash
pip install requests
```

Run the script, and it will retrieve and print the headers of the specified website. Adjust the analysis part based on the headers you want to inspect further.

---
### 10.4. Create a port scanner to check for open ports
To create a basic port scanner in Python, you can use the `socket` library to attempt connections to different ports on a target host. Here's a simple example of a port scanner:

```python
import socket

def scan_ports(target_host, start_port, end_port):
    print(f"Scanning ports on {target_host}...\n")

    # Loop through the specified range of ports
    for port in range(start_port, end_port + 1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt

        # Attempt to connect to the target host and port
        result = sock.connect_ex((target_host, port))

        # Check if the connection was successful
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

        # Close the socket
        sock.close()

if __name__ == "__main__":
    # Replace 'example.com' with the target host
    target_host = 'example.com'

    # Specify the range of ports to scan (e.g., from 1 to 100)
    start_port = 1
    end_port = 100

    # Perform the port scan
    scan_ports(target_host, start_port, end_port)
```

Replace the `target_host` variable with the target host's IP address or domain name. Specify the range of ports you want to scan by setting the `start_port` and `end_port` variables.

Run the script, and it will attempt to connect to each port in the specified range. If the connection is successful, it will print that the port is open; otherwise, it will indicate that the port is closed.

Keep in mind that scanning ports without permission is against the terms of service of many networks, and unauthorized port scanning may be illegal. Always ensure that you have the necessary permissions before scanning ports on a network.

---
### 10.5. Automate interactions with web APIs
To automate interactions with web APIs in Python, you can use the `requests` library. Below is a simple example demonstrating how to make a GET request to an API and handle the JSON response:

```python
import requests

def fetch_data(api_url):
    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'https://api.example.com/data' with the actual API URL
    api_url = 'https://api.example.com/data'

    # Fetch data from the API
    api_data = fetch_data(api_url)

    if api_data:
        # Process and use the retrieved data as needed
        print("API Data:")
        print(api_data)
```

Replace the `api_url` variable with the actual URL of the API you want to interact with. The `fetch_data` function sends a GET request to the specified API URL, checks if the request was successful, and then parses and returns the JSON data.

Note: Some APIs may require authentication or additional parameters in the request. In such cases, you may need to include headers, API keys, or other authentication details in the request.

Make sure to read the API documentation to understand the required parameters and any authentication mechanisms. Additionally, consider error handling and handling rate limits as part of your script.

----
## 11. Security Scripts:

Security scripts are essential tools in the realm of cybersecurity, designed to automate and enhance various aspects of digital defense. These scripts play a crucial role in safeguarding computer systems, networks, and data by automating tasks such as vulnerability scanning, penetration testing, log analysis, and intrusion detection. They contribute to the proactive identification of security weaknesses, rapid response to incidents, and enforcement of access controls and encryption. Security scripts are versatile, addressing diverse security challenges, including firewall configuration, patch management, data loss prevention, and endpoint security. As organizations face evolving cyber threats, security scripts provide a dynamic and automated line of defense, supporting the continuous improvement of security postures and compliance with regulatory standards. Responsible and ethical use of these scripts is paramount to ensure their effectiveness and alignment with legal and ethical standards.

### 11.1. Encrypt and decrypt files
To encrypt and decrypt files in Python, you can use the `cryptography` library, which provides a high-level interface for various cryptographic operations. Below is an example of how you can encrypt and decrypt a file using the Fernet symmetric key encryption scheme:

```python
from cryptography.fernet import Fernet

def generate_key():
    # Generate a key for encryption
    return Fernet.generate_key()

def write_key_to_file(key, filename="secret.key"):
    # Write the key to a file
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key_from_file(filename="secret.key"):
    # Load the key from a file
    return open(filename, "rb").read()

def encrypt_file(file_path, key):
    # Encrypt the contents of a file
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(file_path + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(encrypted_file_path, key):
    # Decrypt the contents of an encrypted file
    cipher = Fernet(key)

    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(encrypted_file_path.rstrip(".encrypted"), "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

if __name__ == "__main__":
    # Generate a key and write it to a file
    key = generate_key()
    write_key_to_file(key)

    # Encrypt a file using the generated key
    file_to_encrypt = "example.txt"
    encrypt_file(file_to_encrypt, key)
    print(f"File '{file_to_encrypt}' encrypted.")

    # Decrypt the encrypted file using the same key
    encrypted_file_to_decrypt = "example.txt.encrypted"
    decrypt_file(encrypted_file_to_decrypt, key)
    print(f"File '{encrypted_file_to_decrypt}' decrypted.")
```

In this example, the `generate_key` function generates a key, and the `write_key_to_file` and `load_key_from_file` functions handle writing and loading the key to and from a file, respectively. The `encrypt_file` and `decrypt_file` functions use Fernet to perform the encryption and decryption operations.

Make sure to keep the encryption key secure since it's necessary for both encryption and decryption. Additionally, consider using more advanced key management practices for production-level applications.

---
### 11.2. Create a simple password manager
Creating a secure and reliable password manager involves several considerations, and for production use, it's recommended to use established libraries and follow security best practices. However, for educational purposes, I can provide a simple example of a password manager using Python with basic file storage. Note that this example is not suitable for real-world use.

```python
import json
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, master_password, key_file="key.key", data_file="data.json"):
        self.key_file = key_file
        self.data_file = data_file

        # Load or generate encryption key
        self.key = self.load_key() or self.generate_key()

        # Initialize Fernet cipher with the key
        self.cipher = Fernet(self.key)

        # Unlock the password manager
        self.unlock(master_password)

    def generate_key(self):
        # Generate a key and save it to the key file
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as key_file:
            key_file.write(key)
        return key

    def load_key(self):
        try:
            # Load the key from the key file
            return open(self.key_file, "rb").read()
        except FileNotFoundError:
            return None

    def unlock(self, master_password):
        # Check if the master password is correct
        if self.encrypt(master_password.encode()) == self.load_key():
            print("Password manager unlocked.")
        else:
            raise ValueError("Incorrect master password.")

    def encrypt(self, data):
        # Encrypt data using the Fernet cipher
        return self.cipher.encrypt(data)

    def decrypt(self, data):
        # Decrypt data using the Fernet cipher
        return self.cipher.decrypt(data)

    def save_data(self, data):
        # Encrypt and save data to the data file
        encrypted_data = self.encrypt(json.dumps(data).encode())
        with open(self.data_file, "wb") as data_file:
            data_file.write(encrypted_data)
        print("Data saved.")

    def load_data(self):
        try:
            # Load and decrypt data from the data file
            with open(self.data_file, "rb") as data_file:
                encrypted_data = data_file.read()
            decrypted_data = self.decrypt(encrypted_data)
            return json.loads(decrypted_data)
        except FileNotFoundError:
            return {}

    def get_password(self, service):
        # Get the password for a specific service
        data = self.load_data()
        return data.get(service, "Service not found.")

    def set_password(self, service, password):
        # Set or update the password for a service
        data = self.load_data()
        data[service] = password
        self.save_data(data)
        print(f"Password for '{service}' set or updated.")

if __name__ == "__main__":
    # Example usage
    master_password = input("Enter your master password: ")

    # Create an instance of the PasswordManager
    password_manager = PasswordManager(master_password)

    # Set or update passwords
    password_manager.set_password("example.com", "strongpassword123")
    password_manager.set_password("another-service", "secretpassword")

    # Get passwords
    print("Password for example.com:", password_manager.get_password("example.com"))
    print("Password for non-existent service:", password_manager.get_password("non-existent-service"))
```

This script uses the `cryptography` library for Fernet encryption and handles the master password verification, password storage, and retrieval. Keep in mind that this is a simple example and lacks many security features found in professional password managers. Always use reputable password management tools for actual use.

---
### 11.3. Generate and verify digital signatures
To generate and verify digital signatures in Python, you can use the `cryptography` library, which provides a secure way to work with cryptographic operations. Below is an example of how to generate and verify digital signatures using `cryptography`:

```python
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

def generate_key_pair():
    # Generate an RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Serialize the public key to PEM format
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_key, public_key_pem

def sign_message(private_key, message):
    # Sign a message using the private key
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature

def verify_signature(public_key_pem, message, signature):
    # Deserialize the public key from PEM format
    public_key = serialization.load_pem_public_key(public_key_pem, backend=default_backend())

    try:
        # Verify the signature
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Signature is valid.")
        return True
    except Exception as e:
        print(f"Signature verification failed: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    private_key, public_key = generate_key_pair()

    # Message to be signed
    message = b"Hello, this is a signed message."

    # Sign the message
    signature = sign_message(private_key, message)

    # Verify the signature
    verify_signature(public_key, message, signature)
```

This script generates an RSA key pair, signs a message with the private key, and then verifies the signature using the corresponding public key. Note that this is a basic example, and in real-world scenarios, you should handle key storage and management securely.

---
### 11.4. Build a script for secure file deletion
To securely delete a file in Python, you can use the `shutil` library along with the `os` library. Here's a simple script that overwrites the file with random data before deleting it:

```python
import os
import shutil
import random

def secure_delete(file_path, passes=3):
    # Function to overwrite the file with random data
    def overwrite_with_random(file_path):
        with open(file_path, 'wb') as file:
            file.write(os.urandom(os.path.getsize(file_path)))

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Overwrite the file with random data multiple times
    for _ in range(passes):
        overwrite_with_random(file_path)

    # Delete the file
    os.remove(file_path)
    print(f"Securely deleted: {file_path}")

if __name__ == "__main__":
    # Example usage
    file_to_delete = "path/to/your/file.txt"

    # Specify the number of passes (default is 3)
    num_passes = 3

    # Securely delete the file
    secure_delete(file_to_delete, passes=num_passes)
```

This script defines a `secure_delete` function that overwrites the content of the file with random data multiple times before finally deleting it using `os.remove()`. The number of passes can be adjusted based on your security requirements.

Note: Keep in mind that secure deletion is a complex topic, and the effectiveness of this method may depend on various factors, including the file system and storage medium. Always be cautious when handling sensitive data and consider consulting security experts for critical applications.

---
### 11.5. Create a basic firewall rule manager
Creating a basic firewall rule manager with Python would typically involve interacting with the underlying firewall software on your system. Below is a simplified example using Python to manage iptables rules on Linux. Please note that this example assumes you have the necessary permissions to manipulate firewall rules.

```python
import subprocess

def add_firewall_rule(rule):
    # Add a new iptables rule
    subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', str(rule['port']), '-j', 'ACCEPT'])

def remove_firewall_rule(rule):
    # Remove an iptables rule
    subprocess.run(['iptables', '-D', 'INPUT', '-p', 'tcp', '--dport', str(rule['port']), '-j', 'ACCEPT'])

def display_firewall_rules():
    # Display current iptables rules
    subprocess.run(['iptables', '-L', '-n', '-v'])

if __name__ == "__main__":
    # Example usage
    rule_to_add = {'port': 80}

    # Add a new firewall rule
    add_firewall_rule(rule_to_add)

    # Display current firewall rules
    display_firewall_rules()

    # Remove the added firewall rule
    remove_firewall_rule(rule_to_add)

    # Display updated firewall rules
    display_firewall_rules()
```

In this example:
- `add_firewall_rule`: Adds a new iptables rule to allow incoming traffic on a specified port.
- `remove_firewall_rule`: Removes a specific iptables rule.
- `display_firewall_rules`: Displays the current iptables rules.

Remember that this is a basic example, and you may need to adapt it based on your specific requirements and the firewall software you are using. Additionally, manipulating firewall rules requires elevated privileges, so ensure your script is run with the appropriate permissions.

Also, keep in mind that directly manipulating firewall rules can have security implications, so use caution and consider security best practices when implementing such functionality.

---
## 12. IoT and Hardware Control Scripts:

IoT and Hardware Control Scripts are essential tools for managing and interacting with Internet of Things (IoT) devices and hardware components. These scripts, often developed using languages like Python, enable users to automate and control smart devices, sensors, and other hardware entities. They facilitate tasks such as turning lights on or off, adjusting thermostat settings, or collecting and displaying sensor data. By interfacing with microcontrollers like Arduino, these scripts empower users to program and control physical devices, extending the capabilities of IoT systems. Whether it's managing smart home devices or controlling robotics, IoT and Hardware Control Scripts provide a flexible and programmable solution to harness the full potential of interconnected devices in the physical world.

### 12.1. Build scripts to control IoT devices (e.g., lights, thermostats)
Controlling IoT devices with Python often involves interacting with the devices' APIs or using specific libraries provided by the device manufacturers. Below are general steps and an example script using the requests library to control a hypothetical smart light bulb. Note that the actual implementation may vary depending on the device and its API.

```python
import requests

class SmartLightController:
    def __init__(self, base_url):
        self.base_url = base_url

    def turn_on(self):
        endpoint = "/api/turn-on"
        response = requests.post(self.base_url + endpoint)
        return response.json()

    def turn_off(self):
        endpoint = "/api/turn-off"
        response = requests.post(self.base_url + endpoint)
        return response.json()

    def set_brightness(self, brightness_level):
        endpoint = f"/api/set-brightness/{brightness_level}"
        response = requests.post(self.base_url + endpoint)
        return response.json()

if __name__ == "__main__":
    # Example usage
    light_controller = SmartLightController("http://smart-light-api.example.com")

    # Turn on the smart light
    response = light_controller.turn_on()
    print(response)

    # Set brightness to 50%
    response = light_controller.set_brightness(50)
    print(response)

    # Turn off the smart light
    response = light_controller.turn_off()
    print(response)
```

In this example:
- `SmartLightController` is a class that communicates with the smart light API.
- `turn_on`, `turn_off`, and `set_brightness` are methods to control the smart light.

Before using this script, you would need to replace the `base_url` and adjust the API endpoints based on the documentation provided by the smart light manufacturer. Always ensure that you have the necessary authentication and authorization to control the IoT devices.

For practical use, consider using specific libraries or SDKs provided by the device manufacturer whenever available. For instance, popular smart home platforms like Philips Hue or Tuya offer Python libraries or APIs for controlling their devices.

---
### 12.2. Monitor and display sensor data (e.g., temperature, humidity)
Monitoring and displaying sensor data with Python typically involves interfacing with sensors and using libraries to visualize the data. Below is a basic example using the `matplotlib` library to plot temperature and humidity data from a hypothetical sensor.

First, you'll need to install the required library:

```bash
pip install matplotlib
```

Then, you can use the following script as a starting point:

```python
import matplotlib.pyplot as plt
import random
from datetime import datetime
import time

class Sensor:
    def __init__(self):
        # Initialize the sensor (replace with actual sensor initialization)
        pass

    def get_data(self):
        # Simulate sensor data (replace with actual data retrieval)
        temperature = random.uniform(20, 25)
        humidity = random.uniform(40, 60)
        timestamp = datetime.now()
        return temperature, humidity, timestamp

def plot_sensor_data(sensor, duration, interval):
    temperatures = []
    humidities = []
    timestamps = []

    end_time = time.time() + duration
    while time.time() < end_time:
        temperature, humidity, timestamp = sensor.get_data()

        temperatures.append(temperature)
        humidities.append(humidity)
        timestamps.append(timestamp)

        # Plot data in real-time
        plot_realtime(timestamps, temperatures, humidities)

        time.sleep(interval)

def plot_realtime(timestamps, temperatures, humidities):
    plt.plot(timestamps, temperatures, label='Temperature (°C)')
    plt.plot(timestamps, humidities, label='Humidity (%)')

    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Sensor Data')
    plt.legend()
    plt.draw()
    plt.pause(0.1)
    plt.clf()

if __name__ == "__main__":
    sensor = Sensor()
    plot_sensor_data(sensor, duration=60, interval=1)
```

In this example:
- `Sensor` is a class representing your sensor (replace it with actual sensor code).
- `get_data` simulates sensor data (replace it with actual data retrieval).
- `plot_sensor_data` continuously retrieves data and updates the plot in real-time.

This is a basic example, and you may need to adjust it based on your specific sensor and requirements. If you have a specific sensor in mind, check if there's a Python library available for interfacing with it. Popular sensor libraries include `Adafruit_CircuitPython` for various sensors.

---
### 12.3. Control a robot or drone
Controlling a robot or drone with Python often involves using specific libraries or APIs provided by the manufacturer of the robot or drone. Below, I'll provide a general overview of the process and some examples using popular platforms.

__Controlling a Drone with Python (DJI Tello)__

[DJI Tello](https://www.ryzerobotics.com/tello) is a popular and affordable drone that can be controlled using Python. You can use the `djitellopy` library for this purpose. First, you'll need to install the library:

```bash
pip install djitellopy
```

Here's a simple example script to take off, move in a square pattern, and land:

```python
from djitellopy import Tello
import time

# Connect to the drone
drone = Tello()
drone.connect()

# Take off
drone.takeoff()
time.sleep(2)

# Move in a square pattern
for _ in range(4):
    drone.move_forward(100)  # Move forward 100 cm
    drone.rotate_clockwise(90)  # Rotate 90 degrees
    time.sleep(1)

# Land
drone.land()
```

__Controlling a Robot with Python (ROS - Robot Operating System)__

[ROS (Robot Operating System)](https://www.ros.org/) is a flexible framework for writing robot software. It provides libraries and tools to help software developers create robot applications. ROS has Python bindings, and you can use it to control a wide range of robots.

Here's a simple example using ROS to control a robot:

```python
# Import ROS libraries
import rospy
from geometry_msgs.msg import Twist

# Initialize the ROS node
rospy.init_node('robot_control_node', anonymous=True)

# Create a publisher to send velocity commands
cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

# Create a Twist message to send linear and angular velocities
cmd_vel_msg = Twist()
cmd_vel_msg.linear.x = 0.2  # Set linear velocity
cmd_vel_msg.angular.z = 0.1  # Set angular velocity

# Publish the Twist message
cmd_vel_pub.publish(cmd_vel_msg)

# Sleep to allow time for the robot to move
rospy.sleep(2)

# Stop the robot
cmd_vel_msg.linear.x = 0.0
cmd_vel_msg.angular.z = 0.0
cmd_vel_pub.publish(cmd_vel_msg)
```

Please note that the examples provided are simplified, and you may need to adapt them based on the specific drone or robot you are working with. Always refer to the documentation of the hardware you're using for detailed instructions on interfacing with Python.

---
### 12.4. Capture and analyze data from webcams or cameras
To capture and analyze data from webcams or cameras using Python, you can use the OpenCV library. OpenCV is a powerful computer vision library that provides various tools for image and video analysis. Below is a basic example to get you started:


```bash
pip install opencv-python
```

__Capture Video from Webcam and Perform Basic Analysis__

```python
import cv2

# Open a connection to the webcam (0 is usually the default webcam)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Webcam Feed', frame)

    # Perform analysis on the frame (add your analysis code here)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
```

In this example:
- `cv2.VideoCapture(0)` opens a connection to the default webcam.
- `cap.read()` captures a frame from the webcam.
- `cv2.imshow()` displays the frame in a window.
- Analysis code can be added inside the loop to perform operations on the captured frames.

__Advanced Analysis: Face Detection__

As an example of more advanced analysis, let's add face detection using OpenCV's pre-trained Haarcascades classifier:

```python
import cv2

# Load the pre-trained face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
```

This example adds face detection using a Haarcascades classifier. You can customize and extend the analysis based on your specific requirements.

---
### 12.5. Create a script to interface with microcontrollers (e.g., Arduino)
To interface with microcontrollers, such as Arduino, using Python, you can use the `pyserial` library. This library allows communication with serial ports, which is commonly used for connecting to microcontrollers. Below is a simple example that demonstrates how to send and receive data between Python and Arduino over a serial connection.

```bash
pip install pyserial
```

__Python Script (Sending data to Arduino)__

```python
import serial
import time

# Specify the COM port (update this based on your Arduino configuration)
ser = serial.Serial('COM3', 9600, timeout=1)

def send_data_to_arduino(data):
    ser.write(data.encode())
    time.sleep(2)  # Allow time for Arduino to process data

# Example: Sending "Hello, Arduino!" to Arduino
send_data_to_arduino("Hello, Arduino!")

# Close the serial connection
ser.close()
```

__Arduino Sketch (Receiving data from Python)__

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readString();
    Serial.print("Received data: ");
    Serial.println(data);

    // Add your Arduino logic based on received data here
  }
}
```

In this example:
- The Python script sends data to the Arduino using `ser.write(data.encode())`.
- The Arduino sketch reads the incoming data using `Serial.readString()` and processes it accordingly.

Remember to replace `'COM3'` with the appropriate COM port to which your Arduino is connected. Also, ensure that the baud rate (`9600` in this case) matches the baud rate specified in your Arduino sketch (`Serial.begin(9600)`).

You can customize both the Python script and Arduino sketch based on the specific data and functionality you need for your project.

---
## 13. AI and Machine Learning Scripts:

AI and Machine Learning Scripts are powerful tools for implementing artificial intelligence (AI) and machine learning algorithms. These scripts, often written in languages like Python, facilitate the development, training, and deployment of machine learning models. They encompass a wide range of applications, from basic linear regression models to complex neural networks. These scripts enable tasks such as image recognition, natural language processing, and recommendation systems. By providing accessible interfaces to popular machine learning frameworks like TensorFlow or scikit-learn, these scripts empower users to explore and harness the capabilities of AI, enabling automation, prediction, and pattern recognition in diverse domains. They play a crucial role in democratizing access to machine learning technologies and fostering innovation in AI-driven applications.

### 13.1. Implement a basic machine learning model (e.g., linear regression)
Let's create a simple example of a linear regression model using Python and the popular `scikit-learn` library. In this example, we'll generate some random data and fit a linear regression model to it.


```bash
pip install scikit-learn
```

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate random data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plot the results
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Example')
plt.show()
```

In this example:
- We generate random data using `numpy`.
- The data is split into training and testing sets using `train_test_split` from `scikit-learn`.
- We train a linear regression model using the training data.
- The model makes predictions on the test set, and we evaluate its performance using mean squared error.
- Finally, we visualize the results with a scatter plot.

This is a basic example, and in a real-world scenario, you would typically work with real data and perform more thorough data preprocessing, feature engineering, and model evaluation. Adjust the code based on your specific use case and dataset.

---
### 13.2. Develop a simple chatbot using natural language processing
We can use the `nltk` library for natural language processing and the `re` library for regular expressions. For simplicity, we'll create a rule-based chatbot that responds to a few predefined patterns.

```bash
pip install nltk
```

```python
import nltk
import re
import random

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            r'hello|hi|hey': ['Hello!', 'Hi there!', 'Hey!'],
            r'how are you': ['I'm doing well, thank you!', 'I'm just a computer program, but I'm fine. How about you?'],
            r'what is your name': ['I am a simple chatbot.', 'You can call me Chatbot.'],
            r'bye|goodbye': ['Goodbye!', 'See you later!', 'Bye!']
        }

    def respond(self, user_input):
        for pattern, responses in self.responses.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                return random.choice(responses)
        return "I'm sorry, I don't understand that."

# Main loop
chatbot = SimpleChatbot()

print("Simple Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Simple Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"Simple Chatbot: {response}")
```

In this example:
- The `SimpleChatbot` class has a dictionary (`responses`) that maps patterns to possible responses.
- The `respond` method searches for a pattern in the user's input and returns a random response if a match is found.
- The main loop allows the user to input messages until they type 'bye' to exit.

Keep in mind that this is a very basic chatbot, and for more sophisticated and dynamic chatbots, you might want to explore using machine learning models, such as those provided by the `transformers` library for more advanced natural language processing tasks.

---
### 13.3. Train a model for image recognition
Training a model for image recognition involves several steps, and it often requires a large labeled dataset. In this example, I'll use the popular deep learning framework TensorFlow and its high-level API, Keras. We'll create a simple convolutional neural network (CNN) for image classification. For demonstration purposes, I'll use the CIFAR-10 dataset, which consists of 60,000 32x32 color images in 10 different classes.

```bash
pip install tensorflow
```

```python
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical

# Load and preprocess the CIFAR-10 dataset
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0  # Normalize pixel values to be between 0 and 1
train_labels, test_labels = to_categorical(train_labels), to_categorical(test_labels)

# Build the CNN model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc}")
```

This script does the following:

1. **Load and preprocess the dataset**: The CIFAR-10 dataset is loaded, and the pixel values are normalized.

2. **Build the CNN model**: A simple CNN model is created using Conv2D layers for convolution, MaxPooling2D layers for downsampling, and Dense layers for classification.

3. **Compile the model**: Specify the optimizer, loss function, and metrics for the model.

4. **Train the model**: The model is trained on the training dataset.

5. **Evaluate the model**: The model is evaluated on the test dataset, and the accuracy is printed.

Keep in mind that for real-world applications, you might need a more complex model, and you should explore techniques like transfer learning with pre-trained models on larger datasets.

---
### 13.4. Create a recommendation system
Creating a recommendation system involves various approaches, and one popular method is collaborative filtering. In this example, I'll show you how to build a simple user-based collaborative filtering recommendation system using Python and the Surprise library.

```bash
pip install scikit-surprise
```

```python
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import cross_validate, train_test_split
from surprise.accuracy import rmse

# Load the Movielens dataset (or any other dataset of your choice)
data = Dataset.load_builtin('ml-100k')

# Define the reader with the appropriate rating scale
reader = Reader(rating_scale=(1, 5))

# Load the dataset with the reader
data = Dataset.load_from_df(data.raw_ratings, reader)

# Split the dataset into training and testing sets
trainset, testset = train_test_split(data, test_size=0.2)

# Use the k-NN algorithm for collaborative filtering
sim_options = {
    'name': 'cosine',
    'user_based': True,
}

model = KNNBasic(sim_options=sim_options)

# Train the model on the training set
model.fit(trainset)

# Make predictions on the test set
predictions = model.test(testset)

# Evaluate the model using RMSE (Root Mean Squared Error)
accuracy = rmse(predictions)
print(f"RMSE: {accuracy}")

# Recommend items for a specific user (user ID 196 in this example)
user_id = str(196)
user_ratings = trainset.ur[trainset.to_inner_uid(user_id)]
items_rated_by_user = {item_id: rating for (item_id, rating) in user_ratings}
items_not_rated_by_user = set(trainset.all_items()) - set(items_rated_by_user)

# Predict ratings for items not rated by the user
item_ratings = [(item_id, model.predict(user_id, item_id).est) for item_id in items_not_rated_by_user]

# Sort the recommendations by predicted rating
sorted_ratings = sorted(item_ratings, key=lambda x: x[1], reverse=True)

# Print the top N recommendations
top_n = 5
top_recommendations = sorted_ratings[:top_n]
print(f"Top {top_n} recommendations for user {user_id}:")
for item_id, rating in top_recommendations:
    print(f"Item ID: {item_id}, Predicted Rating: {rating}")
```

This script does the following:

1. **Load the dataset**: The Movielens dataset is loaded. You can replace it with your own dataset.

2. **Split the dataset**: It is split into training and testing sets.

3. **Choose the collaborative filtering algorithm**: The k-NN algorithm is used with cosine similarity.

4. **Train the model**: The model is trained on the training set.

5. **Make predictions**: Predictions are made on the test set.

6. **Evaluate the model**: The model is evaluated using RMSE.

7. **Generate recommendations**: Recommendations are generated for a specific user (user ID 196 in this example).

This is a basic example, and for real-world scenarios, you might want to explore more advanced techniques and consider factors like item content, matrix factorization, or deep learning-based approaches.

---
### 13.5. Build a script for sentiment analysis on social media data
To perform sentiment analysis on social media data, you can use Natural Language Processing (NLP) libraries. In this example, I'll use the `TextBlob` library for simplicity. Ensure you have it installed before running the script:

```bash
pip install textblob
```

Now, you can use the following Python script for sentiment analysis:

```python
from textblob import TextBlob
import tweepy

# Set up your Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def analyze_sentiment(tweet):
    # Create a TextBlob object
    analysis = TextBlob(tweet)

    # Determine sentiment polarity (-1 to 1)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

def fetch_tweets(query, count=10):
    # Fetch tweets based on the query
    tweets = tweepy.Cursor(api.search, q=query, lang='en').items(count)

    # Analyze sentiment for each tweet
    results = []
    for tweet in tweets:
        result = {
            'text': tweet.text,
            'sentiment': analyze_sentiment(tweet.text)
        }
        results.append(result)

    return results

if __name__ == "__main__":
    # Specify the search query and the number of tweets to fetch
    search_query = 'Python'
    tweet_count = 10

    # Fetch and analyze tweets
    tweets = fetch_tweets(search_query, tweet_count)

    # Display results
    print(f"Sentiment analysis for {tweet_count} tweets with the query '{search_query}':\n")
    for index, tweet in enumerate(tweets, start=1):
        print(f"Tweet {index}:\nText: {tweet['text']}\nSentiment: {tweet['sentiment']}\n")
```

Replace `'your_consumer_key'`, `'your_consumer_secret'`, `'your_access_token'`, and `'your_access_token_secret'` with your actual Twitter API credentials.

This script defines functions to analyze sentiment using `TextBlob` and fetch tweets using the Tweepy library. It then prints the sentiment analysis results for each fetched tweet.

Note: Ensure you have the necessary access and permissions for using the Twitter API.

---
## 14. Database Scripts:

Database Scripts are instrumental in managing and manipulating data within a database system. These scripts, often written in languages like SQL or Python, execute queries and commands to interact with databases, whether for creating tables, inserting records, updating information, or retrieving specific data. They serve as a bridge between applications and databases, allowing seamless communication and efficient data handling. Database scripts are essential for tasks like data migration, backups, and ensuring the integrity of database structures. Additionally, they contribute to optimizing performance, indexing, and managing relationships between different tables. These scripts play a pivotal role in maintaining the overall health and functionality of databases in various applications, from small-scale projects to large enterprise systems.

### 14.1. Automate database backup and restore
To automate database backup and restore with Python, you can use the `subprocess` module to execute command-line operations. Below is a simple example using `mysqldump` for MySQL databases. Adjustments may be needed based on your specific database system.

Ensure you have the necessary database client tools installed, and replace placeholders such as `YOUR_DB_USER`, `YOUR_DB_PASSWORD`, `YOUR_DB_NAME`, and file paths with your actual database credentials and paths.

```python
import subprocess
import datetime
import os

def backup_database():
    # Database connection details
    db_user = 'YOUR_DB_USER'
    db_password = 'YOUR_DB_PASSWORD'
    db_name = 'YOUR_DB_NAME'

    # Backup file name with timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_file = f'database_backup_{timestamp}.sql'

    # Backup command
    command = [
        'mysqldump',
        '-u', db_user,
        '-p' + db_password,
        '--databases', db_name,
        '--result-file=' + backup_file
    ]

    try:
        # Execute backup command
        subprocess.run(command, check=True)
        print(f"Database backup successful. Backup file: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during database backup: {e}")

def restore_database(backup_file):
    # Database connection details
    db_user = 'YOUR_DB_USER'
    db_password = 'YOUR_DB_PASSWORD'
    db_name = 'YOUR_DB_NAME'

    # Restore command
    command = [
        'mysql',
        '-u', db_user,
        '-p' + db_password,
        db_name,
        '<', backup_file
    ]

    try:
        # Execute restore command
        subprocess.run(command, check=True, shell=True)
        print("Database restore successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error during database restore: {e}")

if __name__ == "__main__":
    # Perform backup
    backup_database()

    # Example: Perform restore
    # Specify the backup file to restore
    # restore_file = 'database_backup_20220101120000.sql'
    # restore_database(restore_file)
```

This script defines two functions: `backup_database` to create a database backup and `restore_database` to restore a database from a backup file. You can schedule the backup script to run periodically using a task scheduler (e.g., cron on Unix-like systems or Task Scheduler on Windows). Adjust the commands and paths based on your specific database and system requirements.

---
### 14.2. Generate and execute SQL queries
To generate and execute SQL queries with Python, you can use a database connector library such as `sqlite3` (for SQLite), `psycopg2` (for PostgreSQL), `mysql-connector-python` (for MySQL), or other libraries depending on your database system. Below is a basic example using the `sqlite3` library for SQLite. Make sure to install the appropriate library based on your database system.

Here's an example script that connects to an SQLite database, creates a table, inserts data, and executes a query:

```python
import sqlite3

def create_connection(db_file):
    """Create a database connection to an SQLite database."""
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return None

def execute_query(connection, query):
    """Execute an SQL query."""
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully.")
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")

def main():
    # Connect to the SQLite database (create it if not exists)
    database_file = "example.db"
    connection = create_connection(database_file)

    # Define an SQL query to create a table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """

    # Execute the table creation query
    execute_query(connection, create_table_query)

    # Insert some sample data into the table
    insert_data_query = """
    INSERT INTO users (username, email)
    VALUES
        ('john_doe', 'john@example.com'),
        ('jane_doe', 'jane@example.com');
    """

    # Execute the data insertion query
    execute_query(connection, insert_data_query)

    # Select all rows from the users table
    select_query = "SELECT * FROM users;"

    # Execute the select query and print the results
    cursor = connection.cursor()
    cursor.execute(select_query)
    rows = cursor.fetchall()

    print("Users:")
    for row in rows:
        print(row)

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
```

In this example, the script connects to an SQLite database (`example.db`), creates a table named `users`, inserts sample data, and then selects and prints all rows from the `users` table. Modify the queries according to your database schema and requirements.

---
### 14.3. Build a script for database migration
Database migration scripts are typically specific to the database management system (DBMS) you are using. Below is an example using Flask-Migrate for migrating a SQLite database in a Flask application. Adjustments would be needed for different DBMS or frameworks.

1. Install necessary libraries:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

2. Create a Flask application with SQLAlchemy and Flask-Migrate:

```python
# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Add more models and relationships as needed

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

3. Initialize migrations:

```bash
python app.py db init
```

This creates a `migrations` directory.

4. Create an initial migration:

```bash
python app.py db migrate -m "initial migration"
```

This generates an initial migration script in the `migrations` directory.

5. Apply the initial migration to the database:

```bash
python app.py db upgrade
```

Now, your database is set up.

6. Suppose you make changes to your models. Create a new migration:

```bash
python app.py db migrate -m "description of changes"
```

7. Apply the new migration:

```bash
python app.py db upgrade
```

This process allows you to version control your database schema and apply changes in a structured manner.

Remember to customize the example according to your project's structure and requirements. If you are using a different framework or DBMS, the process might be a bit different.

---
### 14.4. Extract data from databases to CSV or Excel files
You can use the `pandas` library in Python to easily extract data from databases and save it to CSV or Excel files. Here's a simple example using `pandas` and the `sqlite3` module for SQLite databases:

```python
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('example.db')  # Replace 'example.db' with your database file

# Query to select data from a table (replace 'your_table' and 'your_columns' accordingly)
query = "SELECT * FROM your_table"

# Use pandas to read the data from the database into a DataFrame
df = pd.read_sql_query(query, conn)

# Save DataFrame to CSV
df.to_csv('output.csv', index=False)  # Replace 'output.csv' with your desired CSV file name

# Save DataFrame to Excel
df.to_excel('output.xlsx', index=False)  # Replace 'output.xlsx' with your desired Excel file name

# Close the database connection
conn.close()
```

Make sure to replace `'example.db'`, `'your_table'`, and `'your_columns'` with your specific database file, table, and column names. Also, customize the output file names as needed.

If you're using a different database system (e.g., MySQL, PostgreSQL), you may need to install additional libraries (like `mysql-connector` or `psycopg2`) and adjust the connection code accordingly. The basic process of using `pandas` for reading from a database and saving to CSV or Excel remains the same.

---
### 14.5. Create a basic CRUD application
Creating a basic CRUD (Create, Read, Update, Delete) application typically involves using a web framework. Flask is a lightweight web framework for Python that is well-suited for building small to medium-sized web applications. Here's a simple example of a CRUD application using Flask and SQLite as the database:

1. First, install Flask:

   ```bash
   pip install Flask
   ```

2. Create a file named `app.py` and add the following code:

   ```python
   from flask import Flask, render_template, request, redirect, url_for
   from flask_sqlalchemy import SQLAlchemy

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'  # Use SQLite for simplicity
   db = SQLAlchemy(app)

   class Item(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(50), nullable=False)

   @app.route('/')
   def index():
       items = Item.query.all()
       return render_template('index.html', items=items)

   @app.route('/add', methods=['POST'])
   def add():
       name = request.form['name']
       new_item = Item(name=name)
       db.session.add(new_item)
       db.session.commit()
       return redirect(url_for('index'))

   @app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
   def edit(item_id):
       item = Item.query.get(item_id)
       if request.method == 'POST':
           item.name = request.form['name']
           db.session.commit()
           return redirect(url_for('index'))
       return render_template('edit.html', item=item)

   @app.route('/delete/<int:item_id>')
   def delete(item_id):
       item = Item.query.get(item_id)
       db.session.delete(item)
       db.session.commit()
       return redirect(url_for('index'))

   if __name__ == '__main__':
       db.create_all()
       app.run(debug=True)
   ```

3. Create two HTML templates in a folder named `templates`:

   - `templates/index.html`:

     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta http-equiv="X-UA-Compatible" content="IE=edge">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>CRUD App</title>
     </head>
     <body>
         <h1>Items</h1>
         <ul>
             {% for item in items %}
                 <li>{{ item.name }} - <a href="{{ url_for('edit', item_id=item.id) }}">Edit</a> | <a href="{{ url_for('delete', item_id=item.id) }}">Delete</a></li>
             {% endfor %}
         </ul>
         <form action="{{ url_for('add') }}" method="post">
             <label for="name">Item Name:</label>
             <input type="text" id="name" name="name" required>
             <button type="submit">Add Item</button>
         </form>
     </body>
     </html>
     ```

   - `templates/edit.html`:

     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta http-equiv="X-UA-Compatible" content="IE=edge">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Edit Item</title>
     </head>
     <body>
         <h1>Edit Item</h1>
         <form action="{{ url_for('edit', item_id=item.id) }}" method="post">
             <label for="name">Item Name:</label>
             <input type="text" id="name" name="name" value="{{ item.name }}" required>
             <button type="submit">Save Changes</button>
         </form>
     </body>
     </html>
     ```

4. Run your Flask application:

   ```bash
   python app.py
   ```

   Visit http://127.0.0.1:5000/ in your browser to see and interact with the CRUD application.

This is a simple example, and you can extend it based on your needs. Remember to handle security aspects such as input validation, error handling, and authentication in a real-world application.

---
## 15. Education and Learning Scripts:

Education and Learning Scripts play a vital role in enhancing the educational experience through automation and interactive tools. These scripts encompass a wide range of applications, from creating flashcards and math problem generators to spelling and vocabulary quizzes. They facilitate the development of educational games, language learning tools, and even timer-based productivity aids. Through these scripts, students can access dynamic and personalized learning resources, fostering engagement and comprehension. Additionally, educational scripts often include language processing functionalities, enabling the creation of chatbots for tutoring or language learning apps. Whether for creating timers for focused study sessions or generating quizzes for testing knowledge, these scripts contribute to the evolution of modern, technology-driven education, making learning more accessible and enjoyable.

### 15.1. Create flashcards for studying
Creating a simple flashcard program in Python involves handling questions and answers, and then allowing the user to review them. Here's a basic example:

```python
import random

class Flashcards:
    def __init__(self):
        self.cards = {}

    def add_card(self, question, answer):
        self.cards[question] = answer

    def review_cards(self):
        questions = list(self.cards.keys())
        random.shuffle(questions)

        for question in questions:
            user_answer = input(f"Question: {question}\nYour Answer: ")
            correct_answer = self.cards[question]

            if user_answer.lower() == correct_answer.lower():
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer is: {correct_answer}\n")

if __name__ == "__main__":
    flashcards = Flashcards()

    # Add flashcards
    flashcards.add_card("What is the capital of France?", "Paris")
    flashcards.add_card("What is the largest mammal?", "Blue whale")
    flashcards.add_card("Who wrote 'Romeo and Juliet'?", "William Shakespeare")

    # Review flashcards
    flashcards.review_cards()
```

This script defines a `Flashcards` class with methods to add flashcards and review them. You can customize the questions and answers based on your study materials. To run this script, save it to a file (e.g., `flashcards.py`) and execute it using Python:

```bash
python flashcards.py
```

Feel free to expand this script with additional features, such as saving and loading flashcards from a file, implementing a scoring system, or creating a more interactive user interface.

---
### 15.2. Build a script for math problem generation
This script generates addition and subtraction problems with random numbers:

```python
import random

class MathProblemGenerator:
    def generate_addition_problem(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        return f"{num1} + {num2}", num1 + num2

    def generate_subtraction_problem(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, min(num1, 20))
        return f"{num1} - {num2}", num1 - num2

    def generate_math_problem(self):
        if random.choice([True, False]):  # Randomly choose addition or subtraction
            return self.generate_addition_problem()
        else:
            return self.generate_subtraction_problem()

if __name__ == "__main__":
    problem_generator = MathProblemGenerator()

    for _ in range(5):  # Generate 5 math problems
        problem, solution = problem_generator.generate_math_problem()
        user_answer = input(f"Solve: {problem} = ")

        if user_answer.isdigit() and int(user_answer) == solution:
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is: {solution}\n")
```

This script defines a `MathProblemGenerator` class with methods for generating addition and subtraction problems. The `generate_math_problem` method randomly selects between addition and subtraction. The user is prompted to solve the generated problems, and feedback is provided.

You can customize the script to include other types of math problems or extend it with additional features based on your requirements.

---
### 15.3. Develop a spelling or vocabulary quiz
Below is a simple Python script for a spelling or vocabulary quiz. This script uses a dictionary to store words and their correct spellings. The user is prompted with a word, and they need to enter the correct spelling.

```python
import random

class SpellingQuiz:
    def __init__(self, word_dict):
        self.word_dict = word_dict

    def run_quiz(self, num_questions):
        correct_count = 0

        for _ in range(num_questions):
            random_word = random.choice(list(self.word_dict.keys()))
            correct_spelling = self.word_dict[random_word]

            user_input = input(f"How do you spell '{random_word}'? ").strip().lower()

            if user_input == correct_spelling.lower():
                print("Correct!\n")
                correct_count += 1
            else:
                print(f"Wrong! The correct spelling is '{correct_spelling}'.\n")

        print(f"You got {correct_count} out of {num_questions} correct.")

if __name__ == "__main__":
    # Dictionary of words and their correct spellings
    word_dictionary = {
        "python": "Python",
        "programming": "Programming",
        "challenge": "Challenge",
        "coding": "Coding",
        "algorithm": "Algorithm"
    }

    spelling_quiz = SpellingQuiz(word_dictionary)
    spelling_quiz.run_quiz(num_questions=5)
```

You can customize the `word_dictionary` with your own set of words and correct spellings. The `run_quiz` method runs the quiz, asking the user to spell random words from the dictionary. After completing the quiz, it provides the user with the number of correct answers.

Feel free to modify the script to suit your needs or add more features to enhance the quiz experience.

---
### 15.4. Implement a script for learning a new language
Creating a script for learning a new language can involve various activities such as flashcards, quizzes, and vocabulary exercises. Here's a simple Python script that implements a basic language learning quiz. This script focuses on translating words from English to another language.

```python
import random

class LanguageLearningQuiz:
    def __init__(self, word_dict):
        self.word_dict = word_dict

    def run_quiz(self, num_questions):
        correct_count = 0

        for _ in range(num_questions):
            random_word = random.choice(list(self.word_dict.keys()))
            correct_translation = self.word_dict[random_word]

            user_input = input(f"What is the translation of '{random_word}'? ").strip().lower()

            if user_input == correct_translation.lower():
                print("Correct!\n")
                correct_count += 1
            else:
                print(f"Wrong! The correct translation is '{correct_translation}'.\n")

        print(f"You got {correct_count} out of {num_questions} correct.")

if __name__ == "__main__":
    # Dictionary of English words and their translations
    language_dictionary = {
        "hello": "hola",
        "goodbye": "adiós",
        "thank you": "gracias",
        "yes": "sí",
        "no": "no"
    }

    learning_quiz = LanguageLearningQuiz(language_dictionary)
    learning_quiz.run_quiz(num_questions=5)
```

In this script:
- The `language_dictionary` contains English words as keys and their translations as values.
- The `run_quiz` method prompts the user to translate random English words and checks the correctness of the input.
- After completing the quiz, the script prints the number of correct answers.

You can extend this script by adding more features like different languages, more complex sentence structures, or incorporating multimedia elements to make the learning experience more interactive.

---
### 15.5. Create a timer for productivity and focus
Here's a simple Python script to create a timer for productivity and focus. This script uses the `time` module to implement a countdown timer. It will notify you when the time is up.

```python
import time
import os
import platform

def clear_terminal():
    # Clear terminal screen based on the operating system
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def countdown_timer(minutes):
    seconds = minutes * 60

    for remaining_time in range(seconds, 0, -1):
        minutes, seconds = divmod(remaining_time, 60)
        timer_display = f"{minutes:02d}:{seconds:02d}"

        clear_terminal()
        print(f"Timer: {timer_display}")

        time.sleep(1)

    clear_terminal()
    print("Time's up! 🎉")

if __name__ == "__main__":
    try:
        # Set the timer duration in minutes
        timer_duration = int(input("Enter the timer duration in minutes: "))
        countdown_timer(timer_duration)
    except ValueError:
        print("Invalid input. Please enter a valid number of minutes.")
```

In this script:
- The `countdown_timer` function takes the duration in minutes and counts down to 0.
- The `clear_terminal` function clears the terminal screen to update the timer display dynamically.
- The timer will display in the format MM:SS.
- Once the timer reaches 0, it prints a message indicating that the time is up.

You can customize this script further by adding sound notifications or integrating it with GUI libraries for a more user-friendly experience.

---

I want to congratulate you on finishing this in-depth guide on one hundred Python scripts that are quite useful. You have experimented with a variety of scripts, all of which are intended to improve the efficiency of your coding pursuits by automating workflows, streamlining processes, or both. Each script is a demonstration of the tremendous adaptability and practicality of Python, ranging from file administration to data analysis, system monitoring to applications of artificial intelligence. Keep in mind that these scripts are not simply pieces of code, but rather tools that can motivate and direct you as you make your way through the world of Python programming. As you come to the end of this book, allow the information you've gleaned to serve as the springboard for your own coding experiences. Embrace the limitless opportunities that Python provides, and do not stop experimenting, exploring, or paving your own way in the ever-changing world of programming.
