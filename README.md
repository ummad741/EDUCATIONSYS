# EDUCATIONSYS

ONLINE COURSE PLATFORM

## 1. PostgreSQL Installing and SetUp

### 1. Installing

- ON UBUNTU
  Type the following command in the terminal:

  ```bash
  psql --version

  <!-- If not installed -->

  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```

- ON WINDOWS

  [Download Postgresql](https://www.postgresql.org/download/windows/)

### 2. Create a PostgreSQL user and database

Enter the postgresql via terminal:

```bash
sudo -u postgres psql
```

```sql
-- Create new User
CREATE USER yourUSER WITH PASSWORD 'yourPASSWORD';

-- Create new database
CREATE DATABASE yourDATABASE OWNER yourUSER;

-- give permissions
GRANT ALL PRIVILEGES ON DATABASE yourDATABASE TO
YOURUSER;
```

### 3. Checking the creations via psql

```sql
    show user
    \du
    show database
    \l
    show grants
    \l+
```

### 4. Connection

- DNS

  "postgresql://yourUser:YourPassword@yourHost/yourBase"

### 5. DDL Table Structure

  - users
  - courses
  - lessons
  - assignments
  - submissions
  - enrollments
  - payments
  - messages
  - course_reviews

## 2.
