from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        "name": "JASUR ABILKHAIROV",
        "role": "Programmer | Student (AI & Software Development)",
        "summary": "Ambitious student programmer from Bukhara, Uzbekistan. I build beginner-to-intermediate projects in Python with a strong interest in Artificial Intelligence and web development. I’m disciplined, curious, and consistent in daily learning. My goal is to enter a top university in China and pursue a degree in Computer Science.",

        "contacts": [
            "+998 50 515 51 88",
            "ggameryt380@gmail.com",
            "Bukhara, Uzbekistan",
            "github.com/JasurCodeAI",
            "t.me/j10032008"
        ],

        "skills": [
            "Python",
            "Machine Learning",
            "Deep Learning Basics",
            "Data Processing",
            "Git & GitHub",
            "Flask Basics",
            "AI Projects",
            "Problem Solving"
        ],

        "languages": [
            ("English", "Advanced C1"),
            ("Russian", "Native/Fluent"),
            ("Uzbek", "Advanced"),
            ("Chinese", "Beginner")
        ],

        "achievements": [
            "AI digit recognition project",
            "IELTS Band 7",
            "Olympiad achievements",
            "Open-source projects",
            "CSCA Physics 95% / Math 87.5%"
        ],

        "experience": [
            {
                "title": "Self Projects | Student Developer",
                "date": "2024 - Present",
                "desc": "Developing AI and Python projects, experimenting with ML models and improving coding skills daily."
            },
            {
                "title": "Volunteering & School Tech Community",
                "date": "2024 - Present",
                "desc": "Helping with technical tasks, supporting community tech activities and improving teamwork skills."
            }
        ],

        "education": [
            "High School — Focus on Math, Physics, Computer Science (Goal: CS degree in China)"
        ]
    }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
