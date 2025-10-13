## Social Media API – Django & DRF

This project is a backend API for a social media platform built using Django and Django REST Framework. It supports user authentication, profile management, and lays the foundation for posts, comments, likes, follows, and notifications.

---

###  Features Implemented (Task 0)
-  Custom user model with bio, profile picture, and followers
-  Token-based authentication using DRF
-  Endpoints for user registration, login, and profile management



### 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/social_media_api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the server**
   ```bash
   python manage.py runserver
   ```

---

### 🔐 Authentication Endpoints

| Endpoint         | Method | Description                  |
|------------------|--------|------------------------------|
| `/api/register/` | POST   | Register a new user          |
| `/api/login/`    | POST   | Log in and receive token     |
| `/api/profile/`  | GET    | View logged-in user's profile |

✅ All endpoints return or require a token for secure access.

---

### 👤 Custom User Model

The `CustomUser` model extends Django’s `AbstractUser` and includes:

- `bio`: Text field for user bio
- `profile_picture`: Optional image upload
- `followers`: Many-to-many relationship with other users

---

### 🧪 How to Test

Use **Postman** or **curl** to test:

- **Register**:
  ```http
  POST /api/register/
  {
    "username": "pascal",
    "password": "securepass123",
    "email": "pascal@email.com",
    "bio": "Backend engineer in training"
  }
  ```

- **Login**:
  ```http
  POST /api/login/
  {
    "username": "pascal",
    "password": "securepass123"
  }
  ```

- **Profile**:
  ```http
  GET /api/profile/
  Authorization: Token <your_token_here>
  ```

---

### 📂 Project Structure

```
social_media_api/
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
├── social_media_api/
│   ├── settings.py
│   ├── urls.py
```
