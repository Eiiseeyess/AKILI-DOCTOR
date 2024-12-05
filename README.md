# Faraja Backend

Welcome to the Faraja Backend repository. This backend powers the **Faraja AI Psychiatrist** system, leveraging Django and Rasa to deliver a culturally contextualized mental health chatbot experience. Below is a comprehensive guide to setting up, running, and contributing to this project.

---

## Requirements

### Python Version
To ensure compatibility and separate project concerns, the backend requires **Python 3.9** for creating the virtual environment.

---

## Setting Up the Environment

### Creating a Virtual Environment

#### On Linux/MacOS:
1. Open your terminal and navigate to the project root directory.
2. Run the following commands:
   ```bash
   python3.9 -m venv env
   source env/bin/activate
   ```

On Windows:
    Open Command Prompt or PowerShell.
    Navigate to the project root directory.
    Run the following commands:
```cmd
python3.9 -m venv env
env\Scripts\activate
```


Once activated, your terminal will reflect the virtual environment (e.g., (env)).

## Installing Dependencies

After activating the virtual environment, install the required dependencies from the requirements.txt file located at akili_doctor/requirements.txt:

```bash
pip install -r akili_doctor/requirements.txt
```

## Database Setup
### Running Migrations for Django Apps

The backend includes two primary Django apps: Accounts and Articles. To initialize the database:

- Navigate to the akili_doctor directory:

```bash
cd akili_doctor
```

Apply database migrations:
```bash
    python manage.py makemigrations Account articles
    python manage.py migrate
```

## Rasa Overview

Rasa is an open-source machine learning framework for building conversational AI and contextual chatbots. It uses natural language understanding (NLU) to classify intents, extract entities, and respond to user inputs.

Key Rasa Components:

   - Stories: Define how the chatbot should handle conversations based on user inputs and context.
   - Rules: Specify strict conversation patterns for the bot.
   - Domain: Configure intents, responses, and actions available to the bot.

Changes to the stories.yml, rules.yml, or domain.yml files can significantly alter the behavior of the chatbot. For instance:

- Updating the stories.yml file can improve conversation flow.
- Modifying the domain.yml file adds or updates intents and responses.
- Adjusting rules.yml can introduce or fine-tune strict interaction patterns.

### Training the Rasa Model

To train the chatbot model:

- Navigate to the akili_doctor/chatbot directory:
```bash
cd akili_doctor/chatbot
```

Train the model:
```bash
rasa train
```

The trained model will be saved in the models directory(akili_doctor/chatbot/models). After training, it is crucial to regularly prompt the bot to refine responses and improve its overall accuracy.

## Running the Servers
### Running the Django Backend

Navigate to the akili_doctor directory:
```bash
cd akili_doctor
```

Start the Django server:
```bash
python manage.py runserver
```

The backend server will be available at http://127.0.0.1:8000.
 - The api enpoints will now be available for usage from the backend except the chatbot end.

### Running the Rasa Server

Open a new terminal and activate the virtual environment (as explained earlier).

- Navigate to the akili_doctor/chatbot directory:

```bash
cd akili_doctor/chatbot
```

Start the Rasa server:
```bash
rasa run --enable-api
```

The Rasa server will run on http://localhost:5005 and respond to chatbot endpoints configured in the Django backend.

## Testing the Chatbot
### Interacting with the Chatbot in the Terminal

To prompt the chatbot and test responses:

   - Navigate to the akili_doctor/chatbot directory:

```bash
cd akili_doctor/chatbot
```

Run the following command:

```bash
rasa shell
```
- You can reference the akili_doctor/chatbot/data/nlu.yml file fo questions to ask the model initially.

- This allows you to interact with the bot directly and refine its conversational behavior.

### Training the Chatbot for Better Responses

You can retrain the chatbot by running:

```bash
rasa train
```

in the akili_doctor/chatbot directory. This incorporates any updates to the nlu.yml, stories.yml, rules.yml, or domain.yml files to enhance the model.

## Contributing to Faraja Backend

We welcome contributions to improve this project. To contribute:

- Fork the repository on GitHub.
- Create a feature branch:
```bash
git checkout -b feature-name
```

Make your changes and commit:
```bash
git commit -m "Description of changes"
```

Push to your forked repository:
```bash
    git push origin feature-name
```

- Open a pull request on the original repository.

### Contact and Support

For any questions or issues, please open an issue on GitHub or contact clivesasaka@gmail.com.

Thank you for contributing to Faraja Backend!
