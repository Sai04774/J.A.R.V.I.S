# J.A.R.V.I.S Desktop Python Assistant

# Features
- **Voice Commands**: Recognizes and executes voice commands.
- **Play Music**: Plays music from YouTube.
- **Web Search**: Conducts quick searches on Google.
- **Tell Jokes & Fun Facts**: Shares random jokes and interesting fun facts.
- **Application Control**: Opens applications like Notepad, Command Prompt, and Visual Studio Code.
- **Quick Info**: Provides current time and date information.
- **Fallback Text Command**: Accepts typed commands as a fallback.

# Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/jarvis-assistant.git
    ```
2. Navigate to the project directory:
    ```sh
    cd jarvis-assistant
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

# Running in PyCharm
1. **Open PyCharm**:
    - Launch PyCharm.

2. **Create a New Project**:
    - Click on "Create New Project" from the welcome screen.
    - Set the location for your project and choose the appropriate Python interpreter. Click "Create".

3. **Add Your Python File**:
    - In the Project Explorer on the left, right-click the project folder and select "New" -> "Python File".
    - Name the file (e.g., `jarvis.py`) and click "OK".

4. **Paste Your Code**:
    - Copy your Python code and paste it into the newly created Python file.

5. **Install Dependencies**:
    - Open the terminal in PyCharm (usually at the bottom of the window) and install the required packages using `pip`. For example:
      ```sh
      pip install speechrecognition pyttsx3 pywhatkit wikipedia requests smtplib colorama beautifulsoup4
      ```

6. **Run the Code**:
    - Right-click on the Python file in the Project Explorer and select "Run 'jarvis'".
    - Alternatively, click on the green play button at the top right of the window.

# Technologies Used
- Python
- speech_recognition
- pyttsx3
- pywhatkit
- datetime
- wikipedia
- requests
- smtplib
- random
- os
- webbrowser
- BeautifulSoup
- colorama


