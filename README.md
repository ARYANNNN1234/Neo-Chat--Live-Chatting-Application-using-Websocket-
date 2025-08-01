# NeoChat

NeoChat is a simple, real-time web-based chat application built with Flask and Socket.IO. It allows users to join a chat room, send messages, and see who else is currently typing.

---

## Features

- **Real-time Messaging:** Instant message delivery using WebSockets.
- **User Join/Leave Notifications:** System messages inform users when someone joins or leaves the chat.
- **Typing Indicator:** See who is currently typing a message.
- **Local Storage:** Messages are persisted in the browser's local storage, so they remain even if you refresh the page.
- **Responsive Design:** A clean and simple UI that adapts to different screen sizes.

---

## Technologies Used

**Backend:**
- Flask: Lightweight Python web framework.
- Flask-SocketIO: Integrates Socket.IO with Flask for real-time communication.

**Frontend:**
- HTML5: Web page structure.
- CSS3: Modern responsive chat interface styling.
- JavaScript: Client-side logic for Socket.IO and UI management.
- Socket.IO Client Library: Enables WebSocket communication in the browser.

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have the following installed:
- Python 3.x ([Download Python](https://www.python.org/downloads/))
- pip (Python package installer; usually comes with Python)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/NeoChat.git
   cd NeoChat
   ```
   _(Replace `yourusername` and `NeoChat` as appropriate.)_

2. **Create a virtual environment (recommended):**
   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**  
     ```
     .\venv\Scripts\activate
     ```
   - **macOS/Linux:**  
     ```
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```sh
   pip install Flask Flask-SocketIO
   ```

### Running the Application

1. **Save the provided code:**
   - Save the Python backend as `app.py` in the project root.
   - Save the HTML frontend as `index.html` inside a new folder called `templates` in the project root.

   ```
   NeoChat/
   ├── venv/
   ├── app.py
   └── templates/
       └── index.html
   ```

2. **Run the Flask application:**
   ```sh
   python app.py
   ```

3. **Access the application:**  
   Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## How to Use

- **Enter your Username:** Upon opening the page, enter your desired name and click "Set Username".
- **Start Chatting:** The message input will become active. Type your message and press Enter or click "Send".
- **Typing Indicator:** When other users are typing, you'll see a `[username] is typing...` message at the bottom of the chat area.
- **System Messages:** Receive notifications when users join or leave the chat.
- **Local Storage:** Your chat history is saved locally in your browser. Refreshing the page will not delete your messages.

---

## Project Structure

- `app.py`: The main Flask application, handling routes and Socket.IO events.
- `templates/index.html`: The frontend structure, styling, and JavaScript logic.

---

## Future Enhancements (Ideas)

- **User List:** Display a list of all active users in the chat.
- **Private Messaging:** Allow users to send direct messages to each other.
- **Emoji Support:** Add an option to include emojis in messages.
- **Persistent Storage:** Implement a database (e.g., SQLite, PostgreSQL) to store chat messages permanently on the server.
- **User Authentication:** Add user login/registration for secure and personalized chat experiences.
- **Room Functionality:** Allow users to create and join different chat rooms.

---
