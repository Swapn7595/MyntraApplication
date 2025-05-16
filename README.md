# Myntra Selenium + Pytest Automation Framework

This project is a robust, maintainable test automation framework for the Myntra web application, built using Python, Selenium WebDriver, and Pytest. It features dynamic environment selection, detailed logging, Excel and Allure reporting, and a clean, scalable project structure.

## Features

- **Selenium WebDriver** for browser automation
- **Pytest** for test execution and fixtures
- **Dynamic environment selection** (QA, Staging, Production, etc.)
- **Excel reporting**: Auto-incremented test case IDs, dynamic test titles, steps, status, error messages, and execution time
- **Allure reporting** for rich, interactive test reports
- **Robust logging** with prevention of duplicate/incorrect log entries
- **Page Object Model (POM)** for maintainable, reusable test code
- **.gitignore** tailored to ignore logs, reports, venv, screenshots, and other generated files

## Project Structure

```
MyntraApplication/
├── assets/                 # Static assets (e.g., CSS)
├── data/                   # Test data (e.g., test_data.json)
├── logs/                   # Log files
├── pages/                  # Page Object Model classes
├── reports/                # Test reports (Excel, Allure)
├── tests/                  # Test scripts and conftest.py
├── utils/                  # Utilities (config, data loader)
├── requirements.txt        # Python dependencies
├── main.py                 # Script to run tests and generate reports
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.8+
- ChromeDriver or compatible WebDriver in PATH
- Git (for version control)

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Swapn7595/MyntraApplication.git
   cd MyntraApplication
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running Tests
- To run all tests and generate Excel and Allure reports:
  ```sh
  pytest --alluredir=reports/allure-results
  ```
- To view the Allure report:
  ```sh
  allure serve reports/allure-results
  ```
- The Excel report will be generated at `reports/test_report.xlsx`.

### Configuration
- Environments and URLs are managed in `utils/config.py`.
- Test data is stored in `data/test_data.json`.

### Project Highlights
- **No duplicate or incorrect log entries**
- **Test case IDs and titles** are always meaningful in reports
- **Excel report** is robust and never contains duplicate records
- **Allure reporting** is fully integrated
- **Clean .gitignore** ensures only relevant files are tracked

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

---

For any questions or issues, please contact the project maintainer.
