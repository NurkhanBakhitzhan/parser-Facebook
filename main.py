import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def login_to_facebook(username, password):
    # Используем Selenium для автоматизации входа
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    
    email_element = driver.find_element(By.ID, "email")
    pass_element = driver.find_element(By.ID, "pass")
    email_element.send_keys(username)
    pass_element.send_keys(password)
    pass_element.send_keys(Keys.RETURN)
    
    time.sleep(5)  # Подождать, пока страница загрузится
    return driver

def open_group(driver, group_url):
    driver.get(group_url)
    time.sleep(5)  # Подождать, пока страница загрузится

def get_subscribed_users(driver):
    # Логика для получения списка пользователей (нужно прокручивать страницу, чтобы загрузить всех пользователей)
    user_links = []
    # Здесь должна быть логика для получения всех пользователей
    return user_links

def analyze_user_profile(driver, user_profile_url):
    driver.get(user_profile_url)
    time.sleep(5)  # Подождать, пока страница загрузится
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        name = soup.find("title").text
        relationship_status = soup.find(text="Семейное положение").find_next('span').text
    except AttributeError:
        name = ""
        relationship_status = ""
    
    return {"Имя": name, "Семейное положение": relationship_status}

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def parse_group(username, password, group_url, limit, hours):
    driver = login_to_facebook(username, password)
    open_group(driver, group_url)
    users = get_subscribed_users(driver)
    
    data = []
    start_time = time.time()
    profiles_parsed = 0
    interval = (hours * 3600) / limit

    for user in users:
        if profiles_parsed >= limit:
            break
        if time.time() - start_time >= hours * 3600:
            break

        profile_data = analyze_user_profile(driver, user)
        if profile_data:
            data.append(profile_data)
            profiles_parsed += 1

        time.sleep(interval)

    save_to_csv(data, "parsed_data.csv")
    driver.quit()

# Пример использования
# parse_group("your_email", "your_password", "group_url", 500, 24)
