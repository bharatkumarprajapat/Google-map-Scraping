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

📌 Code Overview
🔹 Business Data Model (Dataclasses)
python
Copy
Edit
@dataclass
class Business:
    name: str = None
    address: str = None
    website: str = None
    phone_number: str = None
🔹 Extracting Business Details
python
Copy
Edit
name_xpath = '//h1[contains(@class, "DUwDvf")]'
address_xpath = '//button[contains(@data-item-id, "address")]//div[contains(@class, "fontBodyMedium")]'
website_xpath = '//a[contains(@data-item-id, "authority")]//div[contains(@class, "fontBodyMedium")]'
phone_number_xpath = '//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]'
🔹 Saving Data to Excel and CSV
python
Copy
Edit
def save_to_excel(self, filename):
    self.dataframe().to_excel(f"output/{filename}.xlsx", index=False)

def save_to_csv(self, filename):
    self.dataframe().to_csv(f"output/{filename}.csv", index=False)
📌 Example Output
📁 Saved Files

lua
Copy
Edit
📂 output/
│── 📄 google_maps_data.xlsx
│── 📄 google_maps_data.csv
💡 Sample Data Extracted

Name	Address	Website	Phone Number
XYZ Restaurant	123 Main St, NY	xyz.com	+1 234 567 890
ABC Cafe	456 Elm St, SF	abccafe.com	+1 987 654 321
🛠️ Future Improvements
✅ Add headless mode for faster execution
✅ Extract ratings & reviews
✅ Improve error handling
