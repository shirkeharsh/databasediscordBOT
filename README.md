# Discord User Information Bot

A Discord bot that retrieves and displays user information from a MySQL database. Users can query the bot with a name to get details such as full name, phone number, email, and course. The bot handles multiple results and provides formatted responses, making it easy to access and display user data.

## Features

- **User Query**: Users can query the bot with a name, and the bot will return user details such as full name, phone, email, and course.
- **Multiple Results Handling**: If multiple users have the same name, the bot will display all matching entries.
- **Formatted Output**: Information is returned in a clean, formatted message.

## Tech Stack

- **Discord.py**: Python library to interact with Discord's API.
- **MySQL**: Database to store user information.
- **Python**: The programming language used to build the bot.

## Installation (Linux)

Follow the steps below to install and run the bot on your Linux machine:

### 1. Install Dependencies

Ensure Python 3 and pip are installed. Then, install the required Python libraries:

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install discord mysql-connector-python python-dotenv
