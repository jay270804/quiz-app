class TestConfig:
    """Config class for quiz/tests.py"""

    TEST_DATA = {
        "question_text": "What is the name of the programming language developed by James Gosling at Sun Microsystems and named after the type of coffee from Indonesia",
        "options": {"A": "Java", "B": "Python", "C": "C++", "D": "Ruby"},
        "correct_option": "A",
    }

    TEST_ANSWER = "A"


class SeedConfig:
    """Config class for custom seed_questions command"""

    SEED_DATA = [
        {
            "question_text": "What does HTML stand for?",
            "options": {
                "A": "Hyperlinks and Text Markup Language",
                "B": "Home Tool Markup Language",
                "C": "Hyper Text Markup Language",
                "D": "Hyper Text Making Language",
            },
            "correct_option": "C",
        },
        {
            "question_text": "Which programming language is primarily used for iOS development?",
            "options": {"A": "Swift", "B": "Kotlin", "C": "Java", "D": "C#"},
            "correct_option": "A",
        },
        {
            "question_text": "What is the main purpose of a database management system (DBMS)?",
            "options": {
                "A": "Data Storage and Retrieval",
                "B": "Designing Websites",
                "C": "Compiling Code",
                "D": "Graphic Design",
            },
            "correct_option": "A",
        },
        {
            "question_text": "What is the name of the software development process where requirements and solutions evolve through collaboration between self-organizing cross-functional teams?",
            "options": {
                "A": "Agile",
                "B": "Waterfall",
                "C": "V-Model",
                "D": "Prototype",
            },
            "correct_option": "A",
        },
        {
            "question_text": "Which company created the JavaScript programming language?",
            "options": {
                "A": "Microsoft",
                "B": "Sun Microsystems",
                "C": "Netscape",
                "D": "Google",
            },
            "correct_option": "C",
        },
        {
            "question_text": "In computer networks, what does the abbreviation DNS stand for?",
            "options": {
                "A": "Digital Network Service",
                "B": "Domain Name System",
                "C": "Data Name System",
                "D": "Directory Navigation System",
            },
            "correct_option": "B",
        },
        {
            "question_text": "What does the acronym 'SQL' stand for?",
            "options": {
                "A": "Sequential Query Language",
                "B": "Standard Query Language",
                "C": "Structured Query Language",
                "D": "Simplified Query Language",
            },
            "correct_option": "C",
        },
        {
            "question_text": "Which Python framework is known for its simplicity and is widely used for web development?",
            "options": {"A": "Flask", "B": "Django", "C": "Pyramid", "D": "Bottle"},
            "correct_option": "B",
        },
        {
            "question_text": "What is the core language used for building Android applications?",
            "options": {"A": "Kotlin", "B": "Swift", "C": "Python", "D": "Ruby"},
            "correct_option": "A",
        },
        {
            "question_text": "What is the name of the data structure that follows the Last In, First Out (LIFO) principle?",
            "options": {"A": "Queue", "B": "Stack", "C": "Heap", "D": "Linked List"},
            "correct_option": "B",
        },
    ]
