# Simple Flask Server for Currency Exchange Rates

This project demonstrates how to create a simple Flask server that retrieves currency exchange rates from the National Bank of Ukraine (NBU) and writes them to Google Sheets. The project uses the Google Sheets API and handles requests to fetch currency data within a specified date range.


![Screenshot 2024-09-11 120842](img_example/Screenshot%202024-09-11%20120842.png)
![Screenshot 2024-09-11 120907](img_example/Screenshot%202024-09-11%20120907.png)
![Screenshot 2024-09-11 120921](img_example/Screenshot%202024-09-11%20120921.png)
![Screenshot 2024-09-11 121221](img_example/Screenshot%202024-09-11%20121221.png)

## Requirements

1. Python 3.x
2. Flask
3. Google API Client
4. Requests
5. Python-dotenv

## Installation

1. Clone the repository or download the project files:

    ```bash
    git clone <repo_url>
    cd <repo_directory>
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. Install the required libraries:

    ```bash
    pip install flask google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client requests python-dotenv
    ```

4. Create a `.env` file in the root directory of the project and add the following variables:

    ```plaintext
    SHEET_ID=<your_google_sheet_id>
    SECRET_KEY=<your_flask_secret_key>
    ```

5. Download the `credentials.json` file from the Google API Console and place it in the root directory of the project.

## Setting Up Google Sheets API

1. Go to the [Google API Console](https://console.developers.google.com/).
2. Create a new project or use an existing one.
3. Enable the Google Sheets API and Google Drive API for your project.
4. Create OAuth 2.0 credentials and download the `credentials.json` file.
5. Share your Google Sheet with the email address found in the `credentials.json` file.

## Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. The server will be running at `http://localhost:5000`.

3. Make a GET request to update the exchange rates:

    ```http
    GET http://localhost:5000/update_rates?update_from=YYYY-MM-DD&update_to=YYYY-MM-DD
    ```

    - `update_from` (optional): Start date in `YYYY-MM-DD` format.
    - `update_to` (optional): End date in `YYYY-MM-DD` format.

    If `update_from` and `update_to` are not provided, the current date will be used as the default.

## Code Overview

- `app.py`: The main Flask application file.
- `utils.py`: Contains utility functions for interacting with Google Sheets and fetching currency data.

## Deployment

You can deploy the Flask server to a hosting platform like [PythonAnywhere](https://www.pythonanywhere.com/) or any other cloud service that supports Python applications.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The [National Bank of Ukraine API](https://bank.gov.ua/NBU_Exchange/exchange_site) for currency exchange rates.
- [Google Sheets API](https://developers.google.com/sheets/api) for managing Google Sheets.
