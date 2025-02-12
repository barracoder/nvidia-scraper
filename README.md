# GPU Stock Checker

This script checks the availability of a specified GPU model on the NVIDIA marketplace using Selenium.

## Prerequisites

- Python 3.x
- Selenium
- ChromeDriver

### Installing Dependencies

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install Selenium using pip:

    ```sh
    pip install selenium
    ```

3. Either install Chrome or download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it is in your PATH.

## Usage

1. Clone the repository:

    ```sh
    git clone https://github.com/barracoder/nvidia-scraper.git
    cd nvidia-scraper
    ```

2. Run the script with the desired GPU model name and interval:

    ```sh
    python gpu_stock_checker_browser.py "RTX 3080" --interval 300
    ```

    - [model_name](http://_vscodecontentref_/1): The model name of the GPU to check for availability (e.g., "RTX 3080").
    - `interval`: Time interval between checks in seconds (default: 600 seconds).

## Example

To check the availability of the "RTX 3080" every 5 minutes:

```sh
python gpu_stock_checker_browser.py "RTX 3080" --interval 300