# 🗺️ Google Maps Business Scraper  

A web scraper using **Playwright** to extract business details from **Google Maps**, including business names, addresses, websites, and phone numbers.  

## 📌 Features  
✅ Extracts business details like Name, Address, Website, and Phone Number  
✅ Saves data in **Excel (.xlsx)** and **CSV (.csv)** formats  
✅ Supports command-line arguments for flexible searches  
✅ Automates **Google Maps** search using **Playwright**  

---

## 🚀 Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/google-maps-scraper.git
cd google-map-scraping

pip install -r requirements.txt
playwright install

python main.py -l "Bangalore" -s "IT Companies"
python main.py -l "San Francisco" -s "Coffee Shops" -t 5



📂 google-maps-scraper/
│── 📄 main.py          # Main Python script
│── 📄 requirements.txt # Required dependencies
│── 📄 README.md        # Project documentation
│── 📂 output/          # Folder where scraped data is stored

