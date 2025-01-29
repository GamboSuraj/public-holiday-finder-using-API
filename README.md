# Public Holiday Finder Using API

This project is a Python-based application that allows users to find public holidays for a specific country and year using an API. Developed by **Suraj**, this project demonstrates how to fetch and display public holiday data using REST APIs.

## Features

- Retrieve public holidays for any country.
- Supports multiple countries via country codes.
- Input year to fetch holidays for a specific period.
- Simple and user-friendly command-line interface.

## Requirements

- Python 3.7+
- `requests` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/suraj/public-holiday-finder.git
   cd public-holiday-finder
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```bash
   python holiday_finder.py
   ```

2. Enter the country code (e.g., `US` for the United States) and the year to fetch public holidays.

## Example Output

```plaintext
Enter country code (e.g., US, IN): US
Enter year (e.g., 2025): 2025
Fetching public holidays for US in 2025...

1. New Year's Day - 2025-01-01
2. Martin Luther King Jr. Day - 2025-01-20
3. Independence Day - 2025-07-04
...
```

## API Used

This project uses the [Abstract Public Holiday API](https://www.abstractapi.com/holiday-api) (or any similar API) to fetch public holiday data.

### API Setup

1. Sign up at [Abstract API](https://www.abstractapi.com/) and obtain an API key.
2. Replace the placeholder `API_KEY` in the script with your actual API key:

   ```python
   API_KEY = "your_api_key_here"
   ```

## File Structure

```plaintext
public-holiday-finder/
├── holiday_finder.py    # Main script for fetching holidays
├── README.md            # Project documentation
└── requirements.txt     # Required Python libraries
```

## Technologies Used

- Python
- REST API

## Author

Developed by **Suraj**.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy Coding! 🚀
