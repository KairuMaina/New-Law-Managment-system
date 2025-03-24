# Law Case Management System

## Overview
The **Law Case Management System** is a command-line application designed to help law firms and legal practitioners efficiently manage cases. It allows users to add new cases, view existing cases, and assign lawyers to cases using a structured database system powered by **SQLAlchemy** and **SQLite**.

## Features
- **Add Case** – Create new legal cases with a title, description, and status.
- **View Cases** – Retrieve and display a list of all cases.
- **Assign Lawyer** – Associate a lawyer with a specific case.
- **Database Integration** – Uses SQLite for persistent data storage.

## Technologies Used
- Python 3
- SQLite
- SQLAlchemy
- Alembic (for database migrations)

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3
- SQLite
- Git

### Clone the Repository
```bash
git clone <your-github-repo-url>
cd New-Law-Managment-system
```

### Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Database Migrations
```bash
alembic upgrade head
```

## Usage
Run the application:
```bash
python cli.py
```

Follow the on-screen prompts to interact with the system.

## Database Schema
- **cases** (id, title, description, status, lawyer_id)
- **lawyers** (id, name, specialization)

## Contributing
Feel free to submit issues or pull requests to enhance the system.

## License
This project is licensed under the MIT License.

## Author
**George Maina Kairu**

