# Deepseek Chat Application

This project is a web-based chatting application that utilizes the Deepseek API for chat functionalities. The application is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend.

## Project Structure

```
deepseek-chat-app
├── backend
│   ├── app.py               # Main entry point for the Flask application
│   ├── requirements.txt      # Dependencies for the backend
│   └── templates
│       └── index.html       # HTML structure for the chat application
├── frontend
│   ├── css
│   │   └── styles.css       # CSS styles for the frontend
│   ├── js
│   │   └── app.js           # JavaScript code for user interactions
│   └── README.md            # Documentation for the frontend
└── README.md                # Overall documentation for the project
```

## Features

- Real-time chat functionality using the Deepseek API.
- User-friendly interface for sending and receiving messages.
- Responsive design for various screen sizes.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/deepseek-chat-app.git
   cd deepseek-chat-app
   ```

2. Navigate to the backend directory and install the required dependencies:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000` to access the chat application.

## Usage

- Enter your message in the input field and press "Send" to communicate with the chat.
- Messages will be displayed in the chat window as they are sent and received.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.