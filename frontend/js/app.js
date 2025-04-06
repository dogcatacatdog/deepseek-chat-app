document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const chatBox = document.getElementById('chat-box');

    // Form submission event listener
    chatForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const message = messageInput.value.trim(); // Trim whitespace
        if (message) {
            displayMessage(`나: ${message}`, 'user'); // Display user message first
            sendMessage(message); // Send message to backend
            messageInput.value = ''; // Clear input field
        }
    });

    // Keydown event listener for Enter key
    messageInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') { // Check if the pressed key is Enter
            event.preventDefault(); // Prevent default form submission
            const message = messageInput.value.trim(); // Trim whitespace
            if (message) {
                displayMessage(`나: ${message}`, 'user'); // Display user message first
                sendMessage(message); // Send message to backend
                messageInput.value = ''; // Clear input field
            }
        }
    });

    // Function to send a message to the backend
    function sendMessage(message) {
        fetch('http://127.0.0.1:5000/api/chat', { // Ensure the correct backend URL
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.reply) {
                displayMessage(`사자: ${data.reply}`, 'bot'); // Display bot response
            } else if (data.error) {
                displayMessage(`사자: ${data.error}`, 'bot'); // Display error from backend
            }
        })
        .catch(error => {
            console.error('Error:', error);
            displayMessage('Error: Unable to communicate with the server.', 'error'); // Display communication error
        });
    }

    // Function to display a message in the chat box
    function displayMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.textContent = message;
        messageElement.classList.add('message', sender); // Add both 'message' and sender-specific class
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the bottom
    }
});