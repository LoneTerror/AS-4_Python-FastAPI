# Employee Recognition & Rewards Platform (Backend)

## 📋 Project Overview
This is the backend service for the **Employee Recognition & Rewards Platform**, a system designed to boost organizational engagement through peer-to-peer recognition, automated celebrations, and measurable impact analytics.

The platform enables employees to send points-based appreciation, redeem rewards from a catalog, and integrates seamlessly with workplace tools like Slack and Microsoft Teams.

## 🛠 Tech Stack

### Core Application
**Framework:** FastAPI (Python 3.10+)
**ORM:** Prisma Client Python (Database Access)
**Database:** PostgreSQL (Transactional Data) 
**Caching & Rate Limiting:** Redis 
**Authentication:** OAuth2 / OIDC (Keycloak or Internal Auth)

### Infrastructure & DevOps
**Containerization:** Docker & Kubernetes (Helm) [cite: 53]
**Infrastructure as Code:** Terraform (AWS/Azure/GCP agnostic) [cite: 54]
**Background Workers:** Celery + RabbitMQ (for notifications/async tasks) [cite: 50]
**Storage:** AWS S3 (for image/video attachments) [cite: 51]
**CI/CD:** GitHub Actions [cite: 55]

## ✨ Key Features
1. **Recognition Engine:** Peer-to-peer recognition with point values, hashtags (e.g., #collaboration), and rich media attachments.
2. **Rewards Catalog:** Inventory management for gift cards, swag, and redemption workflows.
3. **Automations:** Scheduled milestone celebrations (birthdays, work anniversaries).
4. **Integrations:** Webhooks and APIs for Slack/Teams bots and HRIS synchronization.
5.  **Analytics:** Manager dashboards for tracking participation trends and budget usage.

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* Node.js (Required for Prisma CLI)
* Docker & Docker Compose (for local DB/Redis)

### 1. Environment Configuration
Create a `.env` file in the root directory:
```ini
# Application
PROJECT_NAME="Employee R&R API"
DEBUG=True
SECRET_KEY=change_this_secret_key

# Database (Prisma)
DATABASE_URL="postgresql://user:password@localhost:5432/rr_db?schema=public"
# 1. Add DATABASE_URL to .env
# 2. Pull schema from DB
prisma db pull

# 3. Generate Prisma client
prisma generate

# 4. Start backend
uvicorn main:app --reload

# Caching
REDIS_URL="redis://localhost:6379/0"

# External Services
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
S3_BUCKET_NAME=rr-attachments