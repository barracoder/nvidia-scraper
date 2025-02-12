from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import argparse

def check_gpu_availability(model_name):
    url = "https://marketplace.nvidia.com/en-gb/consumer/graphics-cards/"
    
    driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed and in your PATH
    driver.get(url)
    
    try:
        product_listings = driver.find_elements(By.CLASS_NAME, "nv-productTile")
        
        for product in product_listings:
            title = product.find_element(By.CLASS_NAME, "nv-productTitle").get_attribute("title")
            status = product.find_element(By.CLASS_NAME, "nv-productTitle").get_attribute("data-ctatype")
            
            if model_name in title and "buy_now" in status:
                print(f"\033[92mALERT: {model_name} is available!\033[0m")  # Print in green
                driver.quit()
                return
        
        print(f"{model_name} is not available to buy.")
    
    except Exception as e:
        print(f"Error checking NVIDIA marketplace: {e}")
    
    driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check GPU stock availability.")
    parser.add_argument("model_name", type=str, help="GPU model name to check, e.g., 'RTX 5090'")
    parser.add_argument("--interval", type=int, default=600, help="Time interval between checks in seconds (default: 600s)")
    
    args = parser.parse_args()
    
    while True:
        check_gpu_availability(args.model_name)
        time.sleep(args.interval)