# Automated IT Helpdesk Ticketing System

## Project Overview
This project is an Automated IT Helpdesk Ticketing System built using Python, Flask, SQLite, and Jinja2. It allows users to submit hardware or software issues, while IT administrators can manage, categorize, assign, and track ticket status.

## Features
- Submit hardware and software issues
- Create helpdesk tickets
- Categorize tickets
- Assign tickets to IT administrators
- Track ticket status
- Store ticket information in database

## Technologies Used
- Python
- Flask
- SQLite
- Jinja2
- HTML

## Project Structure

```text
IT-Helpdesk-System/
│── app.py
│── tickets.db
│── requirements.txt
│── README.md
│── templates/
│    ├── index.html
│    ├── create_ticket.html
│    ├── admin_dashboard.html
│── static/
```

## Installation

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run the application

```bash
python app.py
```

3. Open browser

```text
http://127.0.0.1:5000
```

## Features in Real Life
A user can submit an IT issue (for example: laptop not connecting to Wi-Fi). The IT admin can review the issue, categorize it, assign it, and update its status.

## Learning Outcome
This project helped me understand:
- Web development using Flask
- Database management using SQLite
- Ticket tracking systems
- CRUD operations
- Basic IT support workflow

## Future Improvements
- Login system
- Email notifications
- Ticket priority levels
- File uploads/screenshots
- Search tickets
- Dark mode
- AI chatbot support
- Ticket assignment to employees
