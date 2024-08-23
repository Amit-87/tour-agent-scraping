from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def insert_into_db(name, address, website, phone, rating, reviews):
    cursor = db_connection.cursor()
    insert_query = "INSERT INTO agent(name, address, website, phone_number, Rating, Reviews) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (name, address, website, phone, rating, reviews)
    try:
        cursor.execute(insert_query, data)
        db_connection.commit()
        print("Data inserted successfully into MySQL")
    except mysql.connector.Error as error:
        print(f"Failed to insert data into MySQL table: {error}")
    finally:
        cursor.close()  

db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="12345",
    database="tour"
)

if db_connection.is_connected():
    print("Connected to MySQL database")

chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get('https://www.google.com')

print("tour agents in delhi")
input = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
input.send_keys("tour agents in delhi")

search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "btnK"))
    )
search_button.click()
    
time.sleep(2)


more_places = driver.find_element(By.PARTIAL_LINK_TEXT,"More places")
more_places.click()
time.sleep(10)

for i in range(2,6,2):
    try:
        main_element = driver.find_element('xpath','/html/body/div[2]/div/div[8]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[3]/div[{0}]/div[2]/div/div/a[1]'.format(i))
        main_element.click()
        time.sleep(1)
    except:
        continue
        print("") 

    try:       
        name_element=driver.find_element('xpath','/html/body/div[2]/div/div[8]/div[2]/div/div[2]/async-local-kp/div/div/div[1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[1]/div/div/h2/span')
        name=name_element.text
        print(name)
    except:
        name=""
        print("")

    try:   
        address = driver.find_element(By.CLASS_NAME,"Z1hOCe").text
        if "Address: " in address:
            address = address.replace("Address: ", "")
        print(address)
    except: 
        address=""
        print("")

    try:
        website_link=driver.find_element(By.CSS_SELECTOR,'a.n1obkb')
        website=website_link.get_attribute('href')
        print(website)
    except:
        website="" 
        print("") 

    try:
        phone_link=driver.find_element(By.CSS_SELECTOR,'a[data-phone-number]')     
        phone=phone_link.get_attribute('data-phone-number')
        print(phone)
    except:  
        phone=""
        print("")           

    try:
        rating=driver.find_element('xpath','/html/body/div[2]/div/div[8]/div[2]/div/div[2]/async-local-kp/div/div/div[1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/span/span[1]').text
        print("rating",rating)
    except:
        rating=""
        print("") 

    try:
        reviews=driver.find_element('xpath','/html/body/div[2]/div/div[8]/div[2]/div/div[2]/async-local-kp/div/div/div[1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/span/span[3]').text
        reviews = reviews.replace("(","").replace(")","")
        print(reviews)
    except:
        reviews=""
        print("")  

    insert_into_db(name, address, website, phone, rating, reviews)         
    time.sleep(3)


for i in range(10,44,2):

    try:
        main_element = driver.find_element('xpath','/html/body/div[2]/div/div[8]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[3]/div[{0}]/div[2]/div/div/a[1]'.format(i))
        main_element.click()
        time.sleep(3)
    except:
        continue
        print("")

    try:        
        name_element=driver.find_element('xpath','/html/body/div[2]/div/div[8]/div[2]/div/div[2]/async-local-kp/div/div/div[1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[1]/div/div/h2/span')
        name=name_element.text
        print(name)
    except:
        print("")

    try:   
        address = driver.find_element(By.CLASS_NAME,"Z1hOCe").text
        if "Address: " in address:
            address = address.replace("Address: ", "")
        print(address)
    except: 
        address=""
        print("")

    try:
        website_link=driver.find_element(By.CSS_SELECTOR,'a.n1obkb')
        website=website_link.get_attribute('href')
        print(website)
    except:
        print("")    

    try:
        phone_link=driver.find_element(By.CSS_SELECTOR,'a[data-phone-number]')     
        phone=phone_link.get_attribute('data-phone-number')
        print(phone)
    except:
        print("")       

    try:
        rating=driver.find_element('xpath','/html/body/div[2]/div/div[8]/div[2]/div/div[2]/async-local-kp/div/div/div[1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/span/span[1]').text
        print("rating",rating)
    except:
        print("") 

    try:
        reviews=driver.find_element('xpath','/html/body/div[2]/div/div[8]/div[2]/div/div[2]/async-local-kp/div/div/div[1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/span/span[3]').text
        reviews = reviews.replace("(","").replace(")","")
        print(reviews)
    except:
        print("")         

    insert_into_db(name,address,website,phone,rating,reviews)    
    time.sleep(3)


next_page_element = driver.find_element(By.ID, 'pnnext')
next_page=next_page_element.click()
time.sleep(3)


for page_num in range(2,500):

    for i in range(4,42,2):
        try:
            main_element = driver.find_element('xpath','/html/body/div[2]/div/div[8]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[{0}]/div[2]/div/div/a[1]'.format(i))     
            main_element.click()
            time.sleep(2)
        except NoSuchElementException:
            continue

        try:        
            name_element=driver.find_element('xpath','/html/body/div[2]/div/div[8]/div[2]/div/div[2]/async-local-kp/div/div/div[1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[1]/div/div/h2/span')
            name=name_element.text
            print(name)
        except NoSuchElementException:
            name =""
            print("") 

        try:   
            address = driver.find_element(By.CLASS_NAME,"Z1hOCe").text
            if "Address: " in address:
                address = address.replace("Address: ", "")
            print(address)
        except: 
            address=""
            print("")

        try:
            website_link=driver.find_element(By.CSS_SELECTOR,'a.n1obkb')
            website=website_link.get_attribute('href')
            print(website)
        except NoSuchElementException:
            website = ""
            print("")

        try:
            phone_link=driver.find_element(By.CSS_SELECTOR,'a[data-phone-number]')     
            phone=phone_link.get_attribute('data-phone-number')
            print(phone)
        except NoSuchElementException:
            phone = ""
            print("")  

        try:
            rating=driver.find_element('xpath','/html/body/div[3]/div/div[8]/div[2]/div/div[2]/async-local-kp/div/div/div[1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/span/span[1]').text
            print("rating",rating)
        except NoSuchElementException:
            rating = ""
            print("")

        try:
            reviews=driver.find_element('xpath','/html/body/div[3]/div/div[8]/div[2]/div/div[2]/async-local-kp/div/div/div[1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/span/span[3]').text
            reviews = reviews.replace("(","").replace(")","")
            print(reviews)
        except NoSuchElementException:
            reviews = ""
            print("")    

        insert_into_db(name,address,website,phone,rating,reviews)       

        time.sleep(3)


    try:
        time.sleep(2)
        # next_page_element=driver.find_element('xpath','/html/body/div[2]/div/div[8]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[12]/a')
        next_page_element = driver.find_element(By.ID, 'pnnext')
        next_page=next_page_element.click()
        time.sleep(3)
        
    except NoSuchElementException:
        print("Scraping Successful")
        db_connection.commit()
        break
    
    except Exception as e:
        db_connection.commit()
        print(f"Exception occurred: {str(e)}")
        break


            
driver.quit()
db_connection.close()