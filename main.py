from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import filedialog

print("Was möchtest du suchen?")
userSearch = input()
googleSearch = userSearch.replace(" ", "+")

# Set path to ChromeDriver (Replace this with the correct path)
CHROMEDRIVER_PATH = "C:\\chromedriver-win64\\chromedriver.exe"  # Change this to match your file location

# Initialize WebDriver with Service
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Set window size
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=service, options=options)

# Open Google Search URL
search_url = f"https://www.google.com/search?q={googleSearch}&oq={googleSearch}"
driver.get(search_url)

# Wait for the page to load
time.sleep(2)

page_html = driver.page_source
soup = BeautifulSoup(page_html, 'html.parser')

# Find search results container
allDataContainer = soup.find("div", {"class": "dURPMd"})
allData = allDataContainer.find_all("div", {"class": "Ww4FFb"}) if allDataContainer else []

print(f"{len(allData)} Ergebnisse gefunden.")

l = []
for item in allData:
    obj = {}
    obj["title"] = item.find("h3").text if item.find("h3") else None
    obj["link"] = item.find("a")["href"] if item.find("a") else None
    obj["description"] = item.find("div", {"class": "VwiC3b"}).text if item.find("div", {"class": "VwiC3b"}) else None
    l.append(obj)

print("Suche abgeschlossen. CSV-Datei wird erstellt...")
driver.quit() # Close the browser
# Tkinter Dialog für Speicherort
root = tk.Tk()
root.withdraw()  # Versteckt das Hauptfenster
root.lift()  # Bringt Tkinter-Fenster in den Vordergrund
root.attributes('-topmost', True)  # Erzwingt, dass das Fenster im Vordergrund ist

print("Wähle einen Speicherort für die CSV-Datei")
userPath = filedialog.askdirectory(title="Wähle einen Speicherort")

if not userPath:
    print("Speicherort wurde nicht ausgewählt. Programm wird beendet.")
    driver.quit()
    exit()

root.destroy()  # Schließt Tkinter sauber

# Sanitize userSearch for file naming
userSearch = userSearch.replace(" ", "_").replace('"', "").replace("'", "")
dateipfad = f"{userPath}/{userSearch}.csv"

# Create DataFrame and save to CSV
df = pd.DataFrame(l)
if not df.empty:
    df.to_csv(dateipfad, index=False, encoding="utf-8-sig")
    print(f"Datei wurde erfolgreich gespeichert unter: {dateipfad}")
else:
    print("Keine Daten gefunden. Datei wurde nicht erstellt.")