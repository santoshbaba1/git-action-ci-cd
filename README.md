#  Flask CI/CD Pipeline using GitHub Actions

## Objective

This project demonstrates how to implement a complete **CI/CD pipeline** for a Python Flask application using GitHub Actions.

The pipeline automates:

* Build & dependency installation
* Automated testing using pytest
* Application packaging (Docker)
* Deployment to Staging environment
* Deployment to Production environment

---

##  Sample Application Repository

This project is based on a Flask application. You can use:

* https://github.com/pallets/flask/tree/main/examples/tutorial

<img width="1348" height="759" alt="git action-2 merge" src="https://github.com/user-attachments/assets/dc635f1c-bc72-455b-94bc-bce844ef6ce2" />

---

##  Branch Strategy

| Branch    | Purpose                  |
| --------- | ------------------------ |
| `main`    | Production environment   |
| `staging` | Pre-production / testing |



  - <img width="1303" height="672" alt="ec2" src="https://github.com/user-attachments/assets/3054bdf4-dd7e-43df-aff9-5f80df9bf2f2" />

---

## ⚙️ GitHub Actions Workflow

The workflow is defined in:

```bash
.github/workflows/ci-cd.yml
```

---

## 🔄 CI/CD Pipeline Flow
  - <img width="1536" height="1024" alt="ChatGPT Image Apr 24, 2026, 01_53_30 PM" src="https://github.com/user-attachments/assets/4ae6851e-7708-4e97-bfa8-c25bf40ec9f2" />
### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Tests

```bash
pytest -v
```

✔<img width="1348" height="759" alt="git action-2 merge" src="https://github.com/user-attachments/assets/e55b2232-8f9a-47b7-aa2e-a56b7691fba0" />
 Ensures code quality before deployment

---

### Build Application

* Docker image is created after successful tests
* Image is tagged using commit SHA

---

### Deploy to Staging

Triggered when:

```text
Code is pushed to staging branch
```

Steps:

* SSH into staging server
* Pull latest code / load Docker image
* Restart application container

<img width="674" height="726" alt="staging-key" src="https://github.com/user-attachments/assets/fd13c61c-4d9c-4e62-92b3-46d4cdf9a671" />

---

### Deploy to Production

Triggered when:

```text
A GitHub Release is created
```

Steps:

* SSH into production server
* Deploy stable version of application

<img width="432" height="715" alt="pro-key" src="https://github.com/user-attachments/assets/39da5b8a-da8c-479d-993a-6b9e917a74aa" />

---

## Environment Secrets

Secrets are configured in:

```text
GitHub → Settings → Secrets → Actions
```

<img width="1313" height="672" alt="git env" src="https://github.com/user-attachments/assets/afdf68b5-aa5a-4651-a5cc-a1981517275c" />

### 🔸 Staging Secrets

```text
STAGING_HOST = 13.201.9.73
STAGING_USER = ubuntu
STAGING_SSH_KEY = <private-ssh-key>
```
  - <img width="1362" height="386" alt="stging" src="https://github.com/user-attachments/assets/235a8ad4-47b8-4619-be27-e59831a77dac" />

---

### 🔸 Production Secrets

```text
PROD_HOST = 3.110.187.241
PROD_USER = ubuntu
PROD_SSH_KEY = <private-ssh-key>
```

  - <img width="1361" height="422" alt="prod" src="https://github.com/user-attachments/assets/a81cbeb6-ee70-4a52-b1fd-abcb416ea338" />

---

## SSH Setup (Important)

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

## Docker Setup
<img width="1362" height="386" alt="stging" src="https://github.com/user-attachments/assets/77fb107e-8f20-4649-b804-17888e5a85cb" />
<img width="1365" height="767" alt="stage-flask-1" src="https://github.com/user-attachments/assets/110e2e5a-7798-477e-b2ee-cac6a5a8ad19" />




### Build Image

```bash
docker build -t flask-app .
```

<img width="1365" height="767" alt="stage-flask-1" src="https://github.com/user-attachments/assets/b04f86e5-ad11-4f5e-9d22-e34714c0c54e" />

---

### Run Container

```bash
docker run -d -p 5000:5000 flask-app
```

---

## Access Application

After deployment:

```text
http://<server-ip>:5000
```

---

## Running Tests Locally

```bash
pip install -r requirements.txt
pytest -v
```

---

## 📸 Screenshots (Submission Requirement)

Include the following screenshots:

* ✅ GitHub Actions pipeline success
* ✅ Build and test logs
* ✅ Staging deployment logs
* ✅ Production deployment logs
* ✅ Application running in browser

---

## Troubleshooting

### SSH Error: Permission denied (publickey)

Solution:

* Ensure correct private key in GitHub Secrets
* Ensure public key is added to `~/.ssh/authorized_keys` on server
* Check permissions:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

---

###  Pipeline Not Triggering

* Verify branch name (`staging` or `main`)
* Check workflow conditions in YAML

---

##  Future Improvements

* Add HTTPS using Nginx
* Implement Zero Downtime Deployment
* Integrate Docker Hub
* Add monitoring and logging
* Kubernetes deployment

---

Author

Santosh Kumar Sharma (12394), Batch-15

DevOps & Cloud Enthusiast

