# GoogleMathGenius

This Python project named GoogleMathGenius utilizes Google Cloud Vision API for image text detection, Google Cloud Translation API for text translation, and Google's generative AI for solving textual problems.

## Description

This project is designed to demonstrate the integration of various Google Cloud services to process and interpret image data. It uses separate modules to handle the functionalities of detecting text in an image, translating it, and solving problems described in the text.

## Prerequisites

Before running this project, ensure you have the following:

- Python 3.8 or higher installed
- A Google Cloud account
- API keys for the Google Cloud Vision and Google's generative AI services
- Enabled APIs in the Google Cloud Console
- A gcpKeys.json file with your Google Cloud service account key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-repository/project-name.git
   cd project-name
   ```
   
2. Setup a virtual environment (recommended):
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
    ```
   
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
   
4. Configure environment variables:
    - Create a .env file in the project root.
    - Add the following content:
    ```
    GOOGLE_API_KEY='your_api_key_here'
    ```

5. Set up Google Cloud credentials:

- Ensure the `gcpKeys.json` is in the root or specify its path in your application.

## Running the Application
To run the application, execute the following command:

```
python Main.py
```

This will process an image to detect text, translate the detected text, and attempt to solve a problem based on the text.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your suggestions.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contact
For questions or assistance, please contact [Your Name] at rajkarne@pdx.edu
