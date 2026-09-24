Phase 5 – Project Development

1. Development Overview

PocketSmart AI was developed as a web-based budget and recommendation assistant.

The application was developed using Python, FastAPI, HTML, CSS, JavaScript, SQLAlchemy, and SQLite.

2. Project Structure

The main project structure contains:

- "app/" – Main application package
- "app/routes/" – Web and API routes
- "app/services/" – Recommendation and catalog services
- "app/templates/" – HTML templates
- "app/static/" – CSS and JavaScript files
- "requirements.txt" – Python dependencies
- ".env" – Local environment configuration

3. Backend Development

The backend was developed using FastAPI.

The backend handles:

- User registration
- User login
- Authentication
- Planner requests
- Recommendation generation
- History management
- API requests

4. Database Development

SQLite was used as the database.

SQLAlchemy was used for database interaction.

The database stores:

- User information
- Recommendation history
- Budget details
- Generated recommendation results

5. Authentication Development

Authentication functionality was implemented to protect user-specific pages.

The system includes:

- User registration
- Password hashing
- Login
- Access token
- Protected pages
- Logout

6. Home Interior Planner

The Home Interior Planner accepts:

- Budget
- Room type
- Style
- Required items

The system generates recommendations and budget allocation based on the provided requirements.

7. Party Planner

The Party Planner accepts:

- Budget
- Event type
- Number of guests
- City
- Preferences

The system generates suitable party recommendations and budget allocation.

8. Jewelry Planner

The Jewelry Planner accepts:

- Budget
- Occasion
- Outfit style
- Metal preference
- Additional notes

The system generates suitable jewelry recommendations based on the user's requirements and budget.

9. History Development

The History section stores previously generated recommendations.

Users can view their previous planning results from the History page.

10. Frontend Development

The frontend contains:

- Login page
- Register page
- Dashboard
- Home Planner
- Party Planner
- Jewelry Planner
- History page

HTML and Jinja2 templates were used for page rendering.

CSS was used for styling and JavaScript was used for client-side functionality.

11. Recommendation Service

The recommendation service processes user requirements and generates recommendation results.

Each recommendation can contain:

- Title
- Description
- Estimated price
- Platform
- URL
- Reason

The result also includes budget allocation and useful tips.

12. Environment Configuration

Sensitive configuration such as API keys is maintained locally using environment variables.

The ".env" file is not included in the public GitHub repository.

13. Development Outcome

The PocketSmart AI application was successfully developed and tested locally.

The application provides three main planners:

1. Home Interior Planner
2. Party Planner
3. Jewelry Planner

The application also provides authentication, recommendation generation, budget allocation, and recommendation history.