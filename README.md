Flask URL Shortener
This is a basic URL shortener implemented using Flask. It allows users to submit a URL, and the application generates a shortened version of the URL.

Getting Started
Clone the repository:

bash
Copy code
git clone <repository-url>
Install the required dependencies:

bash
Copy code
pip install Flask
Run the application:

bash
Copy code
python app.py
The application will be accessible at http://127.0.0.1:5000/ in your web browser.

Usage
Open the application in your web browser.

Enter the URL you want to shorten in the input field.

Click on the "Shorten URL" button.

The shortened URL will be displayed along with a copy link icon.

You can use the shortened URL to redirect to the original long URL.

Features
URL Shortening: Quickly generate a shortened version of any URL.
Redirection: Access the original URL by using the generated shortened URL.
Random Shortened URL Generation: Uses a combination of letters and digits for short URL uniqueness.
Technologies Used
Flask: Web framework for Python.
HTML/CSS: Frontend templates and styling.
Random and String Libraries: Used for generating random short URLs.
