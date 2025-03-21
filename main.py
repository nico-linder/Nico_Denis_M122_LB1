from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import filedialog



print("Was möchtest du suchen?")
userSearch = input()
googleSearch = userSearch.replace(" ", "+")


# Set path to ChromeDriver (Replace this with the correct path)
CHROMEDRIVER_PATH = "C:\chromedriver-win64\chromedriver.exe"  # Change this to match your file location

# Initialize WebDriver with Service
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()


options.add_argument("--window-size=1920,1080")  # Set window size
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=service, options=options)

# Open Google Search URL
<<<<<<< HEAD
search_url = "https://www.google.com/search?q="+ googleSearch + "&oq=" + googleSearch
=======
<<<<<<< HEAD
search_url = "https://www.google.com/search?q=sigma+haarschampoo&oq=sigma+haarschampoo&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCQgDECEYChigATIJCAQQIRgKGKAB0gEIMzMyMmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8"
=======
search_url = "https://www.google.com/search?q="+ googleSearch + "&oq=" + googleSearch
>>>>>>> 8bf7881 (Commit submodule changes)
>>>>>>> 860ca84 (Update Submodul)

driver.get(search_url)

# Wait for the page to load
time.sleep(2)

page_html = driver.page_source

soup = BeautifulSoup(page_html,'html.parser')
obj={}
l=[]
allData = soup.find("div",{"class":"dURPMd"}).find_all("div",{"class":"Ww4FFb"})
print(len(allData))
for i in range(0,len(allData)):
    try:
        obj["title"]=allData[i].find("h3").text
    except:
        obj["title"]=None

    try:
        obj["link"]=allData[i].find("a").get('href')
    except:
        obj["link"]=None

    try:
        obj["description"]=allData[i].find("div",{"class":"VwiC3b"}).text
    except:
        obj["description"]=None

    l.append(obj)
    obj={}
userSearch = userSearch.replace(" ", "_")
userSearch = userSearch.replace('"', "")
driver.quit()

root = tk.Tk()
root.withdraw() 

userPath = ""

while userPath == "":  
    print("Wähle einen Speicherort für die CSV-Datei")
    ordnerpfad = filedialog.askdirectory(title="Wähle einen Speicherort")

    if ordnerpfad:  
        userPath = ordnerpfad 
    else:
        print("Kein Ordner ausgewählt. Bitte erneut versuchen.")


df = pd.DataFrame(l)
df.to_csv(userPath, index=False, encoding='utf-8')

print(l)