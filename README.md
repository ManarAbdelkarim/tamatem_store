# 🎮 Tamatem Store - Backend API

This is a Django REST API for managing digital game items and handling basic purchase flows.

---

## 🚀 Features

- JWT Authentication (using SimpleJWT)
- Product listing with pagination and optional filtering by location (JO/SA)
- Product detail view
- Purchase endpoint with order creation
- API documentation via Swagger
- Dockerized setup for easy deployment

---

## 🧑‍💻 Getting Started

### 🔄 Clone the Repository

To clone the project to your local machine, run:

   ```
   git clone https://github.com/ManarAbdelkarim/tamatem_store.git
   cd tamatem_store
   ````

### 📄 Create .env file Following .env.Example


### ✅ Option 1: Run Locally (without Docker)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ManarAbdelkarim/tamatem_store.git
   cd tamatam_store
   
2. **Create a virtual environment:**

    ```
   python3 -m venv env
   source env/bin/activate
   ```
3. **Install dependencies:**
    ```
   pip install -r requirements.txt
    ```
4. **Apply migrations:**
    ```
   python manage.py makemigrations
   python manage.py migrate

   ```
5. **Create superuser:**
    ```
   python manage.py createsuperuser

   ```
   
6. **Run the server:**
    ```
   python manage.py runserver
   ```

### ✅  Option 2: Run with Docker 🐳:

1. **Build and run the containers:**
   ```
   docker compose up --build
   ```
2. **run these inside the container:**
   ```
   docker-compose exec web bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
### API Docs will be available at:

http://localhost:8000/swagger/


Method | Endpoint              | Description
-------|-----------------------|---------------------------------------
POST   | /api/token/         | Get access & refresh token
GET    | /api/products/      | List products (with optional ?location=JO/SA)
GET    | /api/products/<id>/ | Product details
POST   | /api/products/<id>/buy/ | Purchase product


###  CSV Import 📥

```
python manage.py import_products items.csv
```
### Test 🧪

   ```
    python manage.py test
   ```

## Author 👩‍💻

**Manar Abdelkarim**

**GitHub: @ManarAbdelkarim**
