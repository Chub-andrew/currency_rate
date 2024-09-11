from flask import Flask, request, jsonify, render_template
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Access to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("rate").sheet1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_rates', methods=['GET'])
def update_rates():
    start_date = request.args.get('start', default='20230901', type=str)
    end_date = request.args.get('end', default='20230910', type=str)
    valcode = request.args.get('valcode', default='', type=str)
    sort = request.args.get('sort', default='exchangedate', type=str)
    order = request.args.get('order', default='desc', type=str)

    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={valcode}&sort={sort}&order={order}&json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Clearing the form
        sheet.clear()

        # Headers
        headers = ["Exchange Date", "Currency Code", "Rate"]
        sheet.append_row(headers)

        # Data
        for item in data:
            row = [
                item.get("exchangedate", ""),
                item.get("cc", ""),
                item.get("rate", "")
            ]
            sheet.append_row(row)

        return jsonify({"message": "Data successfully updated, check you document"}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch data from the API: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
