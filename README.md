
# Devi: Healthcare Chatbot

This is a simple healthcare chatbot, Devi, built with Python and Tkinter. The chatbot can answer basic user queries, provide information about healthcare services and doctor availability, and book appointments based on user input.

## Features

- **Greeting and Farewell Messages**: Responds to greetings and farewells with friendly, conversational replies.
- **Bot Introduction**: Introduces itself and describes its role as a healthcare assistant.
- **Doctor Information**: Provides information about available doctors and their specialties.
- **Appointment Booking**: Users can select services, enter appointment dates, and choose a time slot for booking appointments.
- **Text-to-Speech Responses**: The bot uses `pyttsx3` to convert text responses into speech, enhancing user interaction.
- **GUI Interface**: Built with Tkinter, the interface includes input fields and displays bot responses interactively.

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then install required packages:
   ```bash
   pip install pyttsx3
   ```

3. **Run the Application**
   Start the application by running:
   ```bash
   python <script_name>.py
   ```

## Usage

1. **Open the Application**: After running the script, a Tkinter window will open with input fields and a chatbot interface.
2. **Interact with Devi**: 
   - **Greetings**: Try saying "hi," "hello," or similar phrases.
   - **Inquire About Doctors**: Ask for "doctor information" to learn about available specialists.
   - **Book an Appointment**: Type "book an appointment" or similar queries to start the appointment booking process.
   - **Thank the Bot**: Say "thanks" to receive a polite reply.
   - **Farewell**: Type "bye" or "goodbye" to end the conversation.

3. **Text-to-Speech**: Devi will respond with voice output for all interactions, enhancing the chatbot experience.

## Files and Code Structure

- **main script**: Contains the Tkinter GUI setup, chatbot logic, and response handling.
- **chat() function**: Processes user inputs and generates bot responses based on keywords and categories.

## Customization

To add more conversational responses:
- Modify the response lists (`hello`, `howare`, `doctors`, etc.) within the code.
- Add more elif statements within the `chat()` function to handle additional user queries or responses.

## Requirements

- Python 3.x
- `pyttsx3` library (for text-to-speech)
- `Tkinter` (included with most Python installations)
