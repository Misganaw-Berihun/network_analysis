
# Slack data Analysis

slack data alalysis is a project whose aim is to extract valuable insights from an anonymized slack messages.


## Table of Content

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Features
- Performs Explanatory Data Analysis to answer the following question
    - Who are the top and bottom 10 users by
        - Reply count?
        - Mention?
        - Message count?
        - Reaction count?
    - What are the top 10 messages by
        - Replies?
        - Reactions?
        - mentions?
    - Which channel has the highest activity?
    - Which fraction of messages are replied within the first 5mins?
- Classifies messages and comments into two tags *Technical* and *Non-Technical*
- Topic modeling and sentiment analysis
- Predictive modeling and analysis
- Network Analysis


## Getting Started

#### Using Conda

If you prefer Conda as your package manager:

1. Open your terminal or command prompt.

2. Navigate to your project directory.

3. Run the following command to create a new Conda environment:

    ```bash
    conda create --name your_env_name python=3.12
    ```
    Replace `your_env_name` with the desired name for your environment e.g. myenv and `3.12` with your preferred Python version.

4. Activate the environment:

    ```bash
    conda activate your_env_name
    ```

#### Using Virtualenv

If you prefer using `venv`, Python's built-in virtual environment module:

1. Open your terminal or command prompt.

2. Navigate to your project directory.

3. Run the following command to create a new virtual environment:

    ```bash
    python -m venv your_env_name
    ```

    Replace `your_env_name` with the desired name for your environment.

4. Activate the environment:

    - On Windows:

    ```bash
    .\your_env_name\scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source your_env_name/bin/activate
    ```

Now, your virtual environment is created and activated. You can install packages and run your Python scripts within this isolated environment. Don't forget to install required packages using `pip` or `conda` once the environment is activated.

### Clone this package

To install the `network_analysis` package, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/network_analysis.git
    ```
2. Navigate to the project directory:
    ```bash
    cd network_analysis
    ```
 
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
### Configuration
Configure the package by modifying the `src/config.py` file. Adjust parameters such as file paths, API keys, or any other configuration settings relevant to your use case.

### Data Loading
The package provides a data loader module (`loader.py`) in the src directory. Use this module to load your network data into a format suitable for analysis.

Example:

```python
from src.loader import DataLoader

# Initialize DataLoader
data_loader = DataLoader()

# Load data from a Slack channel
slack_data = data_loader.load_slack_data("path/to/slack_channel_data")
```