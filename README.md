# # 🚀 Flask CI/CD Pipeline using GitHub Actions

## 📌 Project Overview

This project demonstrates a complete **CI/CD pipeline** for a Flask application using **GitHub Actions**.

The pipeline automates:

* ✅ Code build and testing
* ✅ Docker image creation
* ✅ Deployment to Staging environment
* ✅ Deployment to Production environment

---

## 🏗️ Tech Stack

* Python 3.12
* Flask
* Pytest
* Docker
* GitHub Actions (CI/CD)

---

## 🌿 Branch Strategy

| Branch    | Purpose                |
| --------- | ---------------------- |
| `main`    | Production-ready code  |
| `staging` | Pre-production testing |

---

## ⚙️ CI/CD Workflow

The pipeline is defined in:

```
.github/workflows/ci-cd.yml
```

---

## 🔄 Pipeline Flow

### 1️⃣ Build & Test

* Install dependencies
* Run test cases using `pytest`

```bash
pip install -r requirements.txt
pytest -v
```

---

### 2️⃣ Build Docker Image

* Build Docker image using commit SHA
* Store image as artifact

---

### 3️⃣ Deploy to Staging

Triggered when code is pushed to:

```
staging branch
```

Steps:

* Connect to staging server via SSH
* Pull latest code / load Docker image
* Stop old container
* Start new container

---

### 4️⃣ Deploy to Production

Triggered when:

```
GitHub Release is created
```

Steps:

* Connect to production server
* Deploy latest stable version

---

## 🔐 GitHub Secrets Configuration

Go to:

```
GitHub Repo → Settings → Secrets → Actions
```

Add the following secrets:

### 🔸 Staging

```
STAGING_HOST=<your-server-ip>
STAGING_USER=ubuntu
STAGING_SSH_KEY=<private-ssh-key>
```

### 🔸 Production

```
PROD_HOST=<your-server-ip>
PROD_USER=ubuntu
PROD_SSH_KEY=<private-ssh-key>
```

---

## 🔑 SSH Setup (Important)

1. Generate SSH key:

```bash
ssh-keygen -t ed25519
```

2. Copy public key to server:

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub ubuntu@server-ip
```

3. Add private key to GitHub Secrets

---

## 🐳 Docker Setup

### Build Image Locally

```bash
docker build -t flask-app .
```

### Run Container

```bash
docker run -d -p 5000:5000 flask-app
```

---

## 🌐 Access Application

After deployment:

```
http://<server-ip>:5000
```

---

## 🧪 Running Tests Locally

```bash
pip install -r requirements.txt
pytest -v
```

---

## 📸 Screenshots (Submission)

Include the following:

* ✅ GitHub Actions pipeline success
* ✅ Build & test logs
* ✅ Staging deployment logs
* ✅ Production deployment logs
* ✅ Application running in browser

---

## 🚨 Troubleshooting

### ❌ SSH Error: Permission denied (publickey)

Fix:

* Ensure correct private key in GitHub Secrets
* Ensure public key is in server `~/.ssh/authorized_keys`
* Check permissions:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

---

### ❌ Docker not found

```bash
sudo apt install docker.io docker-compose -y
```

---

## 🚀 Future Improvements

* Add HTTPS with Nginx
* Implement Zero-Downtime Deployment
* Add Monitoring & Logging
* Use Docker Hub for image storage
* Kubernetes deployment

---

## 👨‍💻 Author

**Santhosh Sharma**

---

## 📜 License

This project is for educational purposes.
