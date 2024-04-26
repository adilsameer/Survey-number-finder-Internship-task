import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

print("Program speed depends on website loading speed please wait..")
# Website is loaded using selenium webdriver
URL = "https://dharani.telangana.gov.in/knowLandStatus"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
# Each input is filled according to user input
print("Enter exact same name with native language to find District Mandal and village (eg:Adilabad|ఆదిలాబాద్)\n")
district = input("Enter district (eg:Adilabad|ఆదిలాబాద్) ")
district_element = driver.find_element(By.NAME, "districtID")
select_district = Select(district_element)
try:
    select_district.select_by_visible_text(district)
except NoSuchElementException:
    print(f"Option '{district}' not found in the dropdown.")


mandal = input("Enter Mandal  (eg:Adilabad (Rural)|ఆదిలాబాద్ (రూరల్)) ")
mandal_element = driver.find_element(By.NAME, "mandalID")
select_mandal = Select(mandal_element)
try:
    select_mandal.select_by_visible_text(mandal)
except NoSuchElementException:
    print(f"Option '{mandal}' not found in the dropdown.")

village = input("Enter Village (eg:Ankapoor|అంకాపూర్) ")
village_element = driver.find_element(By.NAME, "villageId")
select_village = Select(village_element)
try:
    select_village.select_by_visible_text(village)
except NoSuchElementException:
    print(f"Option '{village}' not found in the dropdown.")

# It files and print all values on console
time.sleep(2)
survey_element = driver.find_element(By.CSS_SELECTOR, "#surveyIdselect")
time.sleep(5)

survey_select = Select(survey_element)

for option in survey_select.options[1:]:
    print(option.text)
driver.quit()

