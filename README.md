# BTG Transaction Progress Tracker

## Overview

The **BTG Transaction Progress Tracker** is a Python3 tool designed to track the real-time progress of a Bitcoin Gold (BTG) transaction towards a configurable target number of confirmations. It estimates the time to reach a specified confirmation count (default: 300), provides real-time updates, and supports inputs via terminal or web form.

## Key Features

### 1. User Interfaces

-   **CLI Terminal Interface**: A command-line interface that allows users to input transaction details (Transaction ID, start time, confirmation targets) and view progress updates directly in the terminal.
-   **Web Form Interface**: A lightweight web application built with Flask, enabling users to input transaction data through a user-friendly form and display progress visually.

### 2. Dynamic Configuration

-   **Flexible Input Options**: Users can provide transaction details, including Transaction ID and start time, through both CLI and web interfaces.
-   **Default and Fallback Mechanisms**: If required data is not provided by the user, default values are set or fetched automatically from the BTG blockchain insights API, ensuring seamless operation.

### 3. Real-Time Data Fetching

-   **Blockchain Explorer Integration**: Integrates with the BTG blockchain explorer via the [Insights API](https://github.com/BTCGPU/insight-api.git) to fetch the current number of confirmations for specified transactions.
-   **Automatic Data Updates**: Continuously retrieves and updates confirmation counts in real-time, providing users with the most accurate information available.

### 4. Time Estimation

-   **Confirmation Time Estimation**: Accurately estimates the time required to reach a specified number of confirmations (default is 300) based on current confirmation data and other relevant information from the insights API.
-   **Dynamic Adjustments**: Adjusts time estimates in real-time as new confirmation data is fetched, ensuring users receive timely updates.

### 5. Progress Visualization

-   **Real-Time Progress Tracking**: Displays progress bars in both CLI and web interfaces using `tqdm`, allowing users to monitor confirmation status visually.
-   **Engaging User Experience**: Provides clear visual feedback on transaction progress, enhancing user engagement and understanding.

### 6. Comprehensive Error Handling

-   **Input Validation**: Ensures that user inputs are validated for accuracy, reducing errors during data entry.
-   **Fallback Mechanisms for Missing Data**: Automatically retrieves missing information from the API or sets defaults to maintain functionality without user intervention.

## Project Structure

```bash
btg-confirmations-tracker/
├── src/
│   ├── apps/
│   │   ├── cli.py
│   │   ├── web.py
│   │   └── __init__.py
│   ├── btg/
│   │   ├── estimator.py
│   │   ├── fetcher.py
│   │   ├── forms.py
│   │   ├── progress.py
│   │   └── __init__.py
│   ├── config.py
│   ├── main.py
│   └── templates/
│       ├── form.html
│       └── form-tailwind.html
├── tests/
│   ├── test_cli.py
│   ├── test_fetcher.py
│   ├── test_main.py
│   ├── test_progress.py
│   └── test_web.py
├── pyproject.toml            # Project configuration for dependencies and tools
├── setup.py                  # Setup script for dependency installation
├── setup_venv.py             # Script for setting up virtual environment
├── LICENSE                   # License file (MIT)
└── README.md                 # Project documentation
```

## Getting Started

1. Clone the Repository

```bash
git clone --recurse-submodules https://github.com/freddiedfre/btg-confirmations-tracker.git
cd btg-confirmations-tracker

```

2. Setup and Configuration

-   **a. Virtual Environment - Initial Python Setup:** Create and activate the virtual environment:

```bash
python setup_venv.py btg-confirmations-tracker

```

-   **b. Install Dependencies:** Install all required dependencies:

```bash
python setup.py

```

-   **c. Environment Variables:** Set the following environment variables as needed:

```bash
BTG_INSIGHT_API_ENDPOINT: URL of the BTG blockchain explorer API (default: http://localhost:3001/api).
POLLING_INTERVAL: Time in seconds between API calls for confirmation updates (default: 60 seconds).
```

3. Setup the BTG Insight API

The BTG Insight API is included as a submodule. It must be installed and run locally:

On a new terminal windw, navigate to the btg_insight_api submodule:

```bash
cd btg_insight_api
npm install -g bitcore-node@latest
bitcore-node create mynode
cd mynode
bitcore-node install insight-api
bitcore-node start
```

The API will be accessible at http://localhost:3001/ or your configured BTG_INSIGHT_API_ENDPOINT.

## Usage

### Terminal Interface

1. Run the program and input the transaction details when prompted:

```bash
python main.py
```

2. Provide the following inputs:

-   Transaction ID: The transaction ID you want to track.
-   Start Time: The time the transaction was first confirmed (optional, auto-fetched if not provided).
-   Target Confirmations: The number of confirmations to track (default: 300).

3. The progress will update in real-time as confirmations are retrieved from the BTG explorer API.

### Web Form Interface

1. Start the web server:

```bash
python src/main.py --web

```

2. Open the following URL in your web browser:

```bash
http://localhost:5000
```

3. Fill in the transaction details using the web form and submit. The tool will begin tracking and displaying progress.

## Development Setup

### Running Tests

1. To run unit tests, use:

```bash
pytest tests/
```

2. Now you can run tests with coverage using:

:

```bash
pytest --cov=src --cov-report=term-missing
```

This will run all the test files under the tests/ directory, ensuring that the functionality of the tracker is thoroughly validated.

### Linting and Code Formatting

This project uses Black for code formatting. You can ensure code adheres to the formatting guidelines by running:

```bash
black .
```

```bash
flake8 .

```

## License

This project is licensed under the MIT License. See the [LICENSE file](./LICENSE) for more details.
