# Django KPA Project

This project implements two APIs from the provided Postman collection using Django and Django REST Framework. The APIs manage wheel specifications for a given area.

## Tech Stack
- **Backend Framework**: Django, Django REST Framework
- **Database**: SQLite (default; compatible with PostgreSQL)
- **Testing Tool**: Postman

## Setup Instructions
Follow these steps to set up and run the project locally:

### Prerequisites
- Python 3.8+
- Virtualenv (recommended)

### Installation
1. **Clone the Repository** (or unzip the project folder):
   ```bash
   git clone https://github.com/KratiP23/Django_Kpa_project.git
   cd django_kpa_project
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Server**:
   ```bash
   python manage.py runserver
   ```
   The server will run at `http://127.0.0.1:8000`.

### Configuration
- **Database**: Uses SQLite by default. For PostgreSQL, update `settings.py` with your DB credentials and install `psycopg2`.
- **Environment Variables**: (Optional) Add a `.env` file for sensitive settings (e.g., DB credentials) using `django-environ`.

## Implemented APIs

### 1. POST /api/forces/{area}/specifications
- **Description**: Creates a new wheel specification for the specified area.
- **Request**:
  - Method: POST
  - URL: `http://127.0.0.1:8000/api/forces/{area}/specifications`
  - Body: JSON (e.g., `{"formNumber": "WHEEL-2025-000", "fields": [{"fieldName": "Size", "value": "800-1000"}]}`)
- **Response**:
  - Status: 201 Created
  - Body: `{"success": true, "message": "Wheel specification submitted successfully", "data": {...}}`

### 2. GET /api/forces/{area}/specifications
- **Description**: Retrieves wheel specifications for the specified area with optional filters.
- **Request**:
  - Method: GET
  - URL: `http://127.0.0.1:8000/api/forces/{area}/specifications`
  - Query Params: `formnumber`, `submittedby`, `submitteddate` (optional)
- **Response**:
  - Status: 200 OK
  - Body: `{"success": true, "message": "Filtered wheel specification forms fetched successfully", "data": [...]}`

## Limitations and Assumptions
- `{area}` is assumed to be a string identifier.
- Minimal input validation is implemented; production use would require more robust checks.
- SQLite is used for simplicity; switch to PostgreSQL for scalability.

## Testing
- Import `updated_kpa_collection.json` into Postman.
- Start the server and test the endpoints with sample requests.
