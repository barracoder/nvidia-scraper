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