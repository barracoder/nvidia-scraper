import time
import requests
from bs4 import BeautifulSoup
import argparse

def check_gpu_availability(model_name):
    url = "https://marketplace.nvidia.com/en-gb/consumer/graphics-cards/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find all product listings
        product_listings = soup.find_all("div", class_="product-card")
        
        for product in product_listings:
            title = product.find("h2", class_="product-title")
            status = product.find("div", class_="stock-status")
            
            if title and model_name in title.text and status and "Out of Stock" not in status.text:
                print(f"ALERT: {model_name} is available!")
                return
        
        print(f"{model_name} is out of stock.")
    
    except requests.RequestException as e:
        print(f"Error checking NVIDIA marketplace: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check GPU stock availability.")
    parser.add_argument("model_name", type=str, help="GPU model name to check, e.g., 'RTX 5090'")
    parser.add_argument("--interval", type=int, default=600, help="Time interval between checks in seconds (default: 600s)")
    
    args = parser.parse_args()
    
    while True:
        check_gpu_availability(args.model_name)
        time.sleep(args.interval)