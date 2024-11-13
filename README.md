# Stock-Analysis-Chatbot
This project is a stock analysis chatbot assistant built using OpenAI API, Streamlit, yfinance, pandas, and matplotlib. The app allows you to analyze stock data with various technical indicators and visualizations.

## Features

- Get the latest stock price for a given company.
- Calculate the **Simple Moving Average (SMA)** for a given stock ticker and a window.
- Calculate the **Exponential Moving Average (EMA)** for a given stock ticker and a window.
- Calculate the **Relative Strength Index (RSI)** for a given stock ticker.
- Calculate the **Moving Average Convergence Divergence (MACD)** for a given stock ticker.
- Plot the **stock price** for the last year, given the ticker symbol of a company.

## Requirements

- Python 3.x
- OpenAI API Key (for accessing the OpenAI GPT API)
- Streamlit
- yfinance
- pandas
- matplotlib

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mgjim101/stock-analysis-chatbot.git
    ```

2. Navigate to the project directory:
    ```bash
    cd stock-analysis-chatbot
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a file named `API_KEY` in the project root directory and add your OpenAI API key there.

## Usage

1. Run the app:
    ```bash
    streamlit run main.py
    ```

2. Provide any prompt to retrive any kind of the previously stated data, and the assistant will provide the stock analysis with the requested technical indicators and visualizations.

## Testing the API

To test the functionality, make sure you have your OpenAI API key in the `API_KEY` file. Then, you can run the tests by using the following command:

```bash
python test.py
