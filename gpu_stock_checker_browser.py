import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import argparse
import threading

def check_gpu_availability(model_name, url):
    driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed and in your PATH
    driver.get(url)
    
    try:
        product_listings = driver.find_elements(By.CLASS_NAME, "nv-productTile")
        
        for product in product_listings:
            title = product.find_element(By.CLASS_NAME, "nv-productTitle").get_attribute("data-producttitle")
            status = product.find_element(By.CLASS_NAME, "nv-productTitle").get_attribute("data-ctatype")
            pid = product.find_element(By.CLASS_NAME, "nv-productTitle").get_attribute("data-pid-code")
            
            if model_name in title:
                if "buy_now" in status:
                    # Find the first parent element with an href attribute
                    parent_with_href = product.find_element(By.XPATH, ".//ancestor::*[@href][1]")
                    href = parent_with_href.get_attribute("href")
                    print(f"\033[92mALERT: {title} is available!\033[0m")  # Print in green
                    print(f"Nvidia Marketplace: {href}")

                    # Find the product section by ID
                    product_section = driver.find_element(By.ID, pid).get_attribute("innerHTML")
                
                    # Parse the JSON array
                    product_section_json = json.loads(product_section)

                    print(f"Product ID: {pid}")
                    if product_section_json:
                        print(f"Direct purchase links:")
                        for section in product_section_json:
                            print(f"Url: {section['directPurchaseLink']}")
                            print(f"Price: {section['salePrice']}")
                    else:
                        print(f"Direct purchase links: Not available")
                    print()
                else:
                    print(f"{title} is not available to buy.")
    
    except Exception as e:
        print(f"Error checking NVIDIA marketplace: {e}")
    
    driver.quit()

def wait_for_enter_key(stop_event):
    input("Press Enter to stop the script...\n")
    stop_event.set()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check GPU stock availability.")
    parser.add_argument("model_name", type=str, help="GPU model name to check, e.g., 'RTX 5090'")
    parser.add_argument("--interval", type=int, default=600, help="Time interval between checks in seconds (default: 600s)")
    parser.add_argument("--url", type=str, default="https://marketplace.nvidia.com/en-gb/consumer/graphics-cards/", help="URL to check for GPU availability (default: NVIDIA marketplace)")
    
    args = parser.parse_args()
    
    stop_event = threading.Event()
    enter_thread = threading.Thread(target=wait_for_enter_key, args=(stop_event,))
    enter_thread.start()
    
    try:
        while not stop_event.is_set():
            check_gpu_availability(args.model_name, args.url)
            for _ in range(args.interval):
                if stop_event.is_set():
                    break
                time.sleep(1)
    except KeyboardInterrupt:
        print("Script stopped by user.")
    
    print("Script stopped.")