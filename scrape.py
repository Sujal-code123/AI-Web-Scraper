from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching Chrome browser...")

    chrome_driver_path = "./chromedriver.exe"  # Make sure this path is correct
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded. Waiting for content...")

        # Wait for body tag to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        time.sleep(5)  # Optional: allow more time for JS content to load
        html = driver.page_source
        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]


if __name__ == "__main__":
    website = "https://www.example.com"  # ✅ Replace with your target site

    html = scrape_website(website)
    print("\n=== RAW HTML ===")
    print(html[:1000])  # Print part of raw HTML

    body = extract_body_content(html)
    print("\n=== BODY CONTENT ===")
    print(body[:500])  # Print part of body

    cleaned = clean_body_content(body)
    print("\n=== CLEANED TEXT ===")
    print(cleaned[:500])  # Print part of cleaned text

    chunks = split_dom_content(cleaned)
    for i, chunk in enumerate(chunks):
        print(f"\n--- CHUNK {i + 1} ---")
        print(chunk[:500])
