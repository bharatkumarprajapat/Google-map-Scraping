from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict, field
import pandas as pd
import argparse
import os

@dataclass
class Business:
    name: str = None
    address: str = None
    website: str = None
    phone_number: str = None

@dataclass
class BusinessList:
    business_list: list[Business] = field(default_factory=list)
    save_at = 'output'
    
    def dataframe(self):
        return pd.json_normalize((asdict(business) for business in self.business_list), sep="_")
        
    def save_to_excel(self, filename):
        if not os.path.exists(self.save_at):
            os.makedirs(self.save_at)
        self.dataframe().to_excel(f"{self.save_at}/{filename}.xlsx", index=False)
        
    def save_to_csv(self, filename):
        if not os.path.exists(self.save_at):
            os.makedirs(self.save_at)
        self.dataframe().to_csv(f"{self.save_at}/{filename}.csv", index=False)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        print("Opening Google Maps...")
        page.goto('https://www.google.com/maps', timeout=60000)
        page.wait_for_selector('//input[@id="searchboxinput"]', timeout=10000)

        print(f"Searching for: {search_for}")
        search_box = page.locator('//input[@id="searchboxinput"]')
        search_box.fill(search_for)
        search_box.press('Enter')

        page.wait_for_selector('//div[contains(@class, "Nv2PK")]', timeout=15000)

        listings = page.locator('//div[contains(@class, "Nv2PK")]').all()
        print(f"Found {len(listings)} listings")

        if len(listings) == 0:
            print("No results found. Check XPath or search term.")
            return

        business_List = BusinessList()
        
        for listing in listings[:5]:
            listing.click()
            page.wait_for_timeout(5000)

            name_xpath = '//h1[contains(@class, "DUwDvf")]'
            address_xpath = '//button[contains(@data-item-id, "address")]//div[contains(@class, "fontBodyMedium")]'
            website_xpath = '//a[contains(@data-item-id, "authority")]//div[contains(@class, "fontBodyMedium")]'
            phone_number_xpath = '//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]'

            business = Business()
            try:
                business.name = page.locator(name_xpath).inner_text()
            except:
                business.name = "N/A"
            
            try:
                business.address = page.locator(address_xpath).inner_text()
            except:
                business.address = "N/A"
            
            try:
                business.website = page.locator(website_xpath).inner_text()
            except:
                business.website = "N/A"
            
            try:
                business.phone_number = page.locator(phone_number_xpath).inner_text()
            except:
                business.phone_number = "N/A"
            
            business_List.business_list.append(business)

        business_List.save_to_excel('google_maps_data')
        business_List.save_to_csv('google_maps_data')

        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--location", type=str, help="Location to search in")
    parser.add_argument("-s", "--search", type=str, help="Business category to search for")
    parser.add_argument("-t", "--total", type=int, help="Total number of businesses to scrape")

    args = parser.parse_args()

    if args.location and args.search:
        search_for = f'{args.search} {args.location}'
    else:
        search_for = 'Medical in Bangalore'

    main()
