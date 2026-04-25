# FastAPI + React + PostgreSQL Product App 🚀

## 📌 Project Overview
This is a full-stack web application built using FastAPI (backend) and React (frontend).  
It uses PostgreSQL as the database to store and manage product data with full CRUD operations.

---

## 🛠 Tech Stack
- Backend: FastAPI (Python)
- Frontend: React (JavaScript)
- Database: PostgreSQL
- ORM: SQLAlchemy
- API Calls: Axios

---

## ✨ Features
- Create new products
- Read all products
- Update product details
- Delete products
- Search and filter functionality
- Sorting products

---

## ⚙️ Setup Instructions

#frontend
cd frontend
npm install
npm start

#backend
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn sqlalchemy psycopg2-binary
uvicorn main:app --reload
