# Personal Portfolio | Python & Flask

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.3-black?logo=flask)
![HTML5](https://img.shields.io/badge/HTML5-orange?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-blue?logo=css3&logoColor=white)
![Deployment](https://img.shields.io/badge/Deployment-PythonAnywhere-brightgreen)

## Overview

Welcome to my personal portfolio!

This project is a web application developed with **Python, Flask, HTML5, and CSS3**, designed to showcase my professional background, technical skills, and software development projects.

The website is based on the **Read Only** template by HTML5 UP, customized and integrated with a Python Flask backend.

It represents part of my journey as a Mechatronics Engineer transitioning into professional software development, with a focus on Python, automation, data analysis, and artificial intelligence.

## Live Demo

**[View My Portfolio](https://divad20002015.pythonanywhere.com)**

The application is hosted on PythonAnywhere.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Backend programming |
| Flask 3.0.3 | Web framework and routing |
| HTML5 | Website structure |
| CSS3 | Styling and responsive layout |
| JavaScript | Frontend interactions provided by the template |
| Jinja2 | HTML template rendering |
| smtplib | SMTP email integration |
| PythonAnywhere | Application hosting and deployment |
| Git & GitHub | Version control and source code hosting |

## Features

**Personal Portfolio**

- Professional introduction and background
- Technical skills presentation
- Project showcase
- Responsive web interface based on HTML5 UP

**Flask Backend**

- URL routing using Flask
- Dynamic HTML rendering with `render_template()`
- Contact form processing using POST requests
- Integration with Python's built-in `smtplib` module
- Environment variable support for email credentials

**Deployment**

- Public hosting on PythonAnywhere
- WSGI configuration for production hosting
- Linux-based deployment environment

**Note:** The contact form's SMTP functionality requires valid environment variables and a supported outgoing email connection. Email delivery must be configured and tested separately on the hosting platform.

## Project Structure

```text
personal-portfolio/
├── main.py
├── static/
│   ├── assets/
│   └── images/
├── templates/
│   ├── David´s portfolio.html
│   └── index.html
├── .gitignore
├── README.md
└── LICENSE.txt
```

The directory structure may include additional files from the original HTML5 UP template.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace the repository URL with the actual GitHub repository address.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install Flask==3.0.3
```

### 5. Configure environment variables

The contact form uses the following environment variables:

```text
MY_EMAIL
MY_PASSWORD
```

For local development, configure them securely in your operating system or development environment.

Never commit email passwords, API keys, or other credentials to GitHub.

### 6. Run the application

```bash
python main.py
```

Open your browser and navigate to:

`http://127.0.0.1:5000`

## How the Application Works

The application uses Flask to handle HTTP requests and render HTML templates.

**Homepage**

```python
@app.route("/")
def hello():
    return render_template("David´s portfolio.html")
```

This route renders the main portfolio page.

**Contact Form**

```python
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")
```

The contact endpoint receives submitted form data and uses Python's SMTP functionality to attempt email delivery.

Email credentials are read from environment variables instead of being hardcoded into the application.

## Deployment

The portfolio is deployed using **PythonAnywhere**.

The deployment process included:

1. Preparing the Flask application for hosting.
2. Uploading the project files to the Linux server.
3. Configuring the WSGI entry point.
4. Importing the Flask application into the hosting environment.
5. Reloading the web application and verifying that the homepage is accessible.

The deployed application uses Flask through a WSGI configuration rather than running the built-in development server.

## Future Improvements

- [ ] Configure and verify email delivery in production
- [ ] Add server-side form validation and error handling
- [ ] Add automated tests using pytest
- [ ] Improve accessibility and user experience
- [ ] Expand the project showcase with Python and AI applications
- [ ] Improve deployment documentation
- [ ] Add a custom domain

## Template Credits & License

This portfolio is based on **Read Only**, a responsive website template created by **HTML5 UP**, designed by AJ (@ajlkn).

- **Original template:** [Read Only — HTML5 UP](https://html5up.net/read-only)
- **Template creator:** [HTML5 UP](https://html5up.net/)
- **Original license:** [Creative Commons Attribution 3.0 (CC BY 3.0)](https://html5up.net/license)

The original template is distributed under the Creative Commons Attribution 3.0 license, which permits modification and reuse with appropriate attribution.

The original design and template assets remain credited to HTML5 UP and their respective creators.

I customized the template for my personal portfolio and integrated a Python Flask backend, including server-side routing and contact form processing.

The original template's license notices and required attributions should be retained when redistributing its files.

## About Me

I am **David González**, a Mechatronics Engineer with an academic background in Artificial Intelligence and experience in technology education, programming, and engineering projects.

My technical interests include:

- Python development
- Backend web development
- Process automation
- Data analysis
- Machine learning and artificial intelligence
- Robotics and computer vision

My goal is to build practical software solutions that solve real-world problems while continuing to grow as a developer.

## Contact

**David González**

**Portfolio:** [divad20002015.pythonanywhere.com](https://divad20002015.pythonanywhere.com)

**GitHub:** https://github.com/DavidGR20002025

---

*Developed with Python and Flask. Website design based on Read Only by HTML5 UP.*