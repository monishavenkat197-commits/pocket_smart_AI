# Phase 3 – Project Design

## 1. System Architecture

PocketSmart AI is designed as a web-based application.

The system consists of the following main layers:

- Frontend – HTML, CSS and JavaScript
- Backend – Python FastAPI
- Database – SQLite with SQLAlchemy
- AI Service – Gemini AI API
- Recommendation Services – Budget and catalog based recommendation logic

## 2. Main Modules

The application contains the following modules:

1. User Authentication
2. Dashboard
3. Home Interior Planner
4. Party Planner
5. Jewelry Planner
6. Recommendation System
7. Budget Allocation
8. History Management

## 3. Application Workflow

The basic workflow is:

User Registration/Login
        ↓
Dashboard
        ↓
Select Planner
        ↓
Enter Requirements
        ↓
Generate Recommendations
        ↓
Display Budget Allocation
        ↓
Save Recommendation
        ↓
View History

## 4. Home Interior Design

The Home Interior Planner accepts the user's budget, room type, style and required items.

The system processes these requirements and generates suitable products, estimated prices and budget allocation.

## 5. Party Planner Design

The Party Planner accepts the budget, event type, number of guests, city and party requirements.

The system generates recommendations for catering, decoration, venue and other expenses.

## 6. Jewelry Planner Design

The Jewelry Planner accepts the budget, occasion, outfit style, metal preference and jewelry style.

The system generates suitable jewelry recommendations according to the user's requirements and budget.

## 7. Database Design

The application uses SQLite for storing application data.

The database stores:

- User information
- Recommendation history
- Planner details
- Generated recommendation details

## 8. User Interface Design

The application provides simple web