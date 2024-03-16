# Interactive API with Flask and Dash

## Project Overview

This project showcases an interactive web API that integrates Flask for backend operations and Dash for frontend data visualization. It's designed to offer a comprehensive user experience, with features ranging from image conversion to dynamic data presentation.

### Features

- **Flask App**:

  - An index route that provides usage instructions for the app's functionalities.
  - A `convert` route that utilizes Pillow to convert images from one format to another.
  - A custom data generation route leveraging Faker to create and download datasets.

- **Dash App**:
  - Visualizes data from the City of Winnipeg's Open Data Portal using interactive tables and graphs.
  - Demonstrates the use of Plotly for data visualization

## Getting Started

### Prerequisites

Ensure you have Python installed on your system to run the Flask and Dash apps. The Python version used for development is recommended.

### Installation

1. Clone the repository:
   ```bash
   git clone <repo>
   ```
2. Navigate to the project's root directory:
   ```bash
   cd interactive-api-flask-dash
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Flask App

Navigate to the `app` directory and run the Flask app:

```bash
cd app
python app.py
```

Access the Flask app at `http://localhost:5000/` to see the usage instructions and interact with the provided routes.

### Dash App

In the same `app` directory, run the Dash app:

```bash
python dash_app.py
```

Access the Dash app at `http://localhost:8050/` to explore the data visualization features.

## Data

The data used in this project is stored in the `Data` folder, sourced from the City of Winnipeg Open Data Portal.

To include the Jupyter Notebook script that demonstrates consuming your Flask app's API in the README, you can add a new section that briefly explains the script and how to run it. Here's an updated segment for the README.md including this information:

## Consume this Flask API from Jupyter Notebook

A Jupyter Notebook (`interactiveAPIendpoint-Shah.ipynb`) is included in the repository to demonstrate how to consume the Flask app's APIs for image conversion and data generation.

### Features Demonstrated

- **Image Conversion**: Shows the Flask app's `/convert` endpoint to convert it to a specified format and save the converted image.
- **Data Generation**: Utilizes the `/generate_data` endpoint to generate fake data based on the specified dataset and quantity, displaying the generated data within the notebook.

### Running the Example

To run the Jupyter Notebook example:

1. Ensure you have Jupyter installed. If not, you can install it using pip:
   ```bash
   pip install notebook
   ```
2. Start the Flask app as described in the [Usage](#usage) section.
3. Navigate to the directory containing `interactiveAPIendpoint-Shah.ipynb` and launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
4. Open the `interactiveAPIendpoint-Shah.ipynb` file in the Jupyter interface.
5. Run the notebook cells in sequence to see the API consumption in action.

Please ensure the Flask app is running at `http://127.0.0.1:5000` as the notebook is configured to send requests to this URL.
