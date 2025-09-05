# AI-Web-Scraper
AI Web Scraper with LLM Summarization. Developed a Streamlit-based app to extract and summarize website content using Selenium and BeautifulSoup.
A smart AI Web Scraper that extracts structured data from websites — all driven by powerful LLMs and fully interactive via a web app UI.
# 📌 Features

- 🌐 Automates browser interactions using **Selenium**
- 🔍 Parses HTML content with **BeautifulSoup**
- 🧠 Optional AI parsing layer for intelligent data understanding
- 📄 Extracts specific elements (text, images, links, etc.)
- 💾 Saves results to files (TXT, CSV, or JSON)
- 🔧 Easy-to-configure script for custom scraping tasks
# 🧠 Key Features: 
Built with Python, Streamlit, and Selenium for live website scraping
Integrated Mistral-7B-Instruct model via Together.ai for natural language instruction-following
Supports flexible prompts like:
“Extract all blog titles in a table”
“List all properties and prices from this page”
Renders AI output into real, interactive tables using pandas and Markdown processing
Handles long pages by splitting and parsing DOM chunks, sending them sequentially to the LLM
# Tech Stack:
Selenium + BeautifulSoup for scraping and cleaning HTML content
Together.ai API to run mistralai/Mistral-7B-Instruct-v0.1
Pandas + io to parse Markdown tables from LLM into clean dataframes
Streamlit frontend for real-time, browser-based interaction
## 💡 Use Cases
- Scraping product data from e-commerce sites
- Gathering news headlines
- Extracting academic or research content
- Intelligent parsing of unstructured text

 ## LLM Exploration Journey:

During development, I explored multiple open-source models and platforms:

- ✅ DeepSeek-VL for image-based understanding (screenshots & OCR-like tasks)  
- ✅ DeepSeek-LLM via Hugging Face and Together APIs  
- ✅ FLAN-T5 models for offline usage  
- ✅ Finally selected Mistral 7B for its performance + free hosted API on Together.ai

### 🔍 I learned how to work around common LLM output issues like:
Repetitive or broken Markdown
Rate limits
Table rendering mismatches
Model compatibility with APIs
## 👤 Author

**Sujal Bondarde**  
📧 aumdhavale@gmail.com  
🔗 [GitHub](https://github.com/Sujal-code123) | [LinkedIn](https://www.linkedin.com/in/sujal-bondarde-5352a024b/)

---
