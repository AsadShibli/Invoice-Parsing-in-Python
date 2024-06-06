# Receipt and Invoice Parsing in Python
This project automates the process of parsing receipts and invoices using Optical Character Recognition (OCR) in Python. The system utilizes an external API for OCR processing and extracts relevant data from the receipts and invoices, which is then saved into a CSV file for further analysis.

## Project Structure:
```arduino
├── main.py
├── process.py
└── data
    ├── p1.png
    ├── p2.png
    ├── p3.png
```

## Files Description

- `main.py`: This script sends an image of a receipt or invoice to the OCR API and saves the response in JSON format.
- `process.py`: This script processes the JSON response, extracts relevant information, and saves it into a CSV file.
- `data`: Directory containing images of receipts or invoices to be processed.

## Requirements

- Python 3.x
- Requests library
- JSON library
- CSV library

You can install the required Python packages using pip:

```bash
pip install requests
```
## Usage
### 1. Setup OCR API
Replace the API key in main.py with your own key:
```python
'api-key':'YOUR_API_KEY'
```
### 2. Running the OCR Process
Run the `main.py` script to send an image to the OCR API and save the response in a JSON file:
```python
python main.py
```
### 3. Processing the JSON Response
Run the `process.py` script to process the JSON response and save the extracted data into a CSV file:
```python
python process.py
```
## Contributing
Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.
## Acknowledgements
[Asprise OCR API](https://asprise.com/) for providing the OCR capabilities.

  
