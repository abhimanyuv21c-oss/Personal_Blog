# Personal_Blog
Creating a new Blog using Flask(web application)

text
# Personal Blog

A simple personal blog web application built using Flask (Python). The blog supports a guest section for viewing articles and an admin section for managing (adding, editing, deleting) articles. Articles are stored as JSON files on the filesystem.

## Features

- **Guest Section**
  - Home page listing all published articles with titles and dates.
  - Article page showing full content and publication date.

- **Admin Section**
  - Secure login for admin access.
  - Dashboard with list of articles and options to add, edit, or delete.
  - Forms for creating new articles or updating existing ones.

## Technology Stack

- Python 3
- Flask web framework
- JSON file-based storage for articles
- HTML/CSS for frontend templating (no JavaScript)

## Project Structure

myblog/
│
├── articles/ # Article files stored as JSON
├── templates/ # Jinja2 HTML templates
├── static/ # CSS and static assets
├── venv/ # Python virtual environment (ignored in repo)
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules

text

## Setup and Installation

1. Clone the repository:
git clone https://github.com/abhimanyuv21c-oss/Personal_Blog.git
cd Personal_Blog

text

2. Create and activate a virtual environment:
- On Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

3. Install dependencies:
pip install -r requirements.txt

text

4. Run the Flask application:
python app.py

text

5. Open your browser at `http://localhost:5000` to view the blog.

## Usage

- Visit the home page to browse articles.
- Admin login is at `/admin/login` with hardcoded credentials in `app.py` (`admin` / `password123` by default).
- After login, manage articles from the dashboard.

## Notes

- Articles are stored as JSON files inside the `articles/` folder.
- The blog does not use a database, making it simple and portable.
- Basic authentication is hardcoded; for production, implement proper user management.

## Project Repository
Project link : https://github.com/abhimanyuv21c-oss/Personal_Blog

## Project URL 
Anytime you can create your own project using the below project URL
Project URL: https://roadmap.sh/projects/personal-blog
