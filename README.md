# Stock and Financial Information Agent

This project is designed to provide real-time stock and financial information using an OpenAI-powered agent with access to the Polygon API. The agent can fetch data such as the latest stock quotes, financials, news, and aggregates for a specified stock ticker. The application is built using Streamlit and LangChain, allowing users to query financial information interactively.

![Image Description](/ui.png)


## Prerequisites

Before running the application, ensure you have the following installed:

- [Conda](https://docs.conda.io/projects/conda/en/latest/index.html)
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)

## Installation

### Step 1: Set up the environment

1. **Create and activate the Conda environment**:

```bash
conda create -n langgraph python=3.11
conda activate langgraph
```

2. **Set up API keys**:
   
   - Obtain your [OpenAI API key](https://platform.openai.com/account/api-keys) and [Polygon API key](https://polygon.io/) and export them as environment variables:

```bash
export OPENAI_API_KEY="your_openai_api_key"
export POLYGON_API_KEY="your_polygon_api_key"
```

3. **Install required dependencies**:

```bash
pip install streamlit langgraph langchain_community langchain langchain_openai langchainhub polygon-api-client
```

### Step 2: Run the Streamlit Application

1. Clone or download the repository to your local machine.

2. Navigate to the directory containing the `app.py` file.

3. Run the Streamlit application:

```bash
streamlit run app.py
```

This will launch the Streamlit app in your default browser.

## How It Works

The application uses several tools provided by the LangChain framework to gather and display financial information:

1. **Polygon API Wrapper**: The Polygon API is used to fetch stock quotes, financials, news, and aggregate data.
   
2. **LangChain Agent**: The LangChain agent uses a pre-trained OpenAI model (`gpt-4-turbo-preview`) to understand and process natural language queries and interact with the Polygon API.

3. **Streamlit UI**: The user interacts with the app via an input field where they can enter financial queries (e.g., "What is ABNB's daily closing price?"). The result is displayed on the web page.

### The app follows these key steps:

- **Step 1: Define Tools**: Polygon API tools are initialized and set up for querying stock data (last quote, ticker news, financials, and aggregates).
- **Step 2: Define the Agent**: The OpenAI-powered agent interprets user queries and determines which tools to invoke.
- **Step 3: Define LangGraph**: The LangGraph workflow orchestrates the agent's behavior, ensuring that the tools are executed in the correct order.
- **Step 4: Streamlit UI**: The app's frontend accepts user queries, processes them, and displays the results.

## Features

- Query stock quotes, financials, news, and aggregates for a given ticker.
- User-friendly interface using Streamlit.
- Seamless integration of OpenAI's GPT model with Polygon API to fetch financial data.

## Example Queries

- "What is ABNB's daily closing price between March 7, 2024, and March 14, 2024?"
- "Give me the latest news for Apple (AAPL)."
- "What are the financials for Tesla (TSLA)?"

## Contributing

Feel free to fork the repository, submit issues, or create pull requests. Contributions are welcome!

## License

This project is open-source and available under the MIT License.

---

For any issues or feature requests, please open an issue on the repository or contact [shailxiitm@gmail.com](mailto:shailxiitm@gmail.com).


### Explanation:
- **Prerequisites and Installation**: This section covers the steps to create a Conda environment, set the necessary API keys, and install dependencies.
- **Running the Application**: Clear instructions to get the app running with the `streamlit run app.py` command.
- **How It Works**: Describes the flow of the app, including how the tools are defined, the LangChain agent works, and how the app uses Streamlit to display results.
- **Example Queries**: Provides users with a few sample queries they can try in the app.
- **Contributing and License**: Encourages contributions and provides contact details for issues.
