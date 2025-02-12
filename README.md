# GPU Stock Checker

This Python script periodically checks the NVIDIA Marketplace for the availability of a specified GPU model and prints an alert if the card is in stock.

## Features
- Monitors NVIDIA's official marketplace.
- Checks for stock availability of any specified GPU model.
- Allows users to set a custom check interval.
- Uses `requests` and `BeautifulSoup` for web scraping.

## Prerequisites
Ensure you have Python installed. You can check by running:
```sh
python --version
```

You also need to install the required dependencies:
```sh
pip install requests beautifulsoup4
```

## Usage
Run the script with the following command:
```sh
python gpu_stock_checker.py "GPU_MODEL" --interval SECONDS
```

### Example
To check for an RTX 5090 every 5 minutes (300 seconds):
```sh
python gpu_stock_checker.py "RTX 5090" --interval 300
```

## Parameters
- `GPU_MODEL` (required): The name of the GPU model to check.
- `--interval SECONDS` (optional): Time interval between checks in seconds (default: 600 seconds).

## Notes
- The script runs indefinitely and checks for stock availability at the specified interval.
- If an error occurs while fetching data, it will print an error message and continue running.

## License
This project is open-source. Feel free to modify and use it as needed.

## Contributions
Pull requests and improvements are welcome!

