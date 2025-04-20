from django.core.management.base import BaseCommand
from skills.models import Skills

class Command(BaseCommand):
    help = "Seed the database with predefined skills and categories"

    def handle(self, *args, **kwargs):
        skills_data = {
            "Web Development": [
                ("HTML", "Markup language for creating web pages"),
                ("CSS", "Stylesheet language used to describe the presentation of a document"),
                ("JavaScript", "Scripting language for web development"),
                ("React", "JavaScript library for building user interfaces"),
                ("Vue.js", "Progressive JavaScript framework"),
                ("Angular", "TypeScript-based open-source web application framework"),
                ("TypeScript", "Typed superset of JavaScript"),
                ("Tailwind CSS", "Utility-first CSS framework"),
                ("Bootstrap", "Front-end toolkit for developing responsive web projects"),
                ("Next.js", "React framework with server-side rendering")
            ],
            "Backend Development": [
                ("Python", "High-level, general-purpose programming language"),
                ("Django", "Python web framework for rapid development"),
                ("Node.js", "JavaScript runtime for backend"),
                ("Express.js", "Minimalist Node.js framework"),
                ("Flask", "Lightweight Python web framework"),
                ("Ruby on Rails", "Server-side web app framework written in Ruby"),
                ("PHP", "Server scripting language for web development"),
                ("Laravel", "PHP web application framework"),
                ("Go", "Statically typed, compiled programming language by Google"),
                ("Java", "High-level, object-oriented programming language")
            ],
            "Mobile Development": [
                ("Flutter", "UI toolkit for building cross-platform apps"),
                ("React Native", "JavaScript framework for writing real, natively rendering mobile apps"),
                ("Swift", "Programming language for iOS development"),
                ("Kotlin", "Modern programming language for Android"),
                ("Java (Android)", "Used for Android app development"),
                ("Dart", "Language used with Flutter"),
                ("Objective-C", "Older language for iOS development"),
                ("Xamarin", "Microsoft’s framework for cross-platform mobile apps"),
                ("Ionic", "Open-source SDK for hybrid mobile app development"),
                ("Cordova", "Mobile development framework using HTML, CSS and JavaScript")
            ],
            "Data Science": [
                ("Pandas", "Python library for data analysis"),
                ("NumPy", "Library for numerical computing in Python"),
                ("Matplotlib", "Library for creating static visualizations"),
                ("Seaborn", "Data visualization library based on matplotlib"),
                ("Scikit-learn", "Machine learning library in Python"),
                ("TensorFlow", "Open-source platform for machine learning"),
                ("PyTorch", "Machine learning framework developed by Facebook"),
                ("R", "Statistical computing language"),
                ("SQL", "Language for managing and querying databases"),
                ("Excel", "Spreadsheet tool used in data analysis")
            ],
            "DevOps": [
                ("Docker", "Platform for containerizing applications"),
                ("Kubernetes", "Orchestration tool for containers"),
                ("CI/CD", "Continuous integration and delivery/deployment"),
                ("Jenkins", "Automation server for building pipelines"),
                ("GitHub Actions", "CI/CD tool integrated with GitHub"),
                ("Terraform", "Infrastructure as code tool"),
                ("Ansible", "IT automation tool"),
                ("AWS", "Amazon Web Services cloud platform"),
                ("Azure", "Microsoft cloud computing platform"),
                ("GCP", "Google Cloud Platform")
            ],
            "AI / Machine Learning": [
                ("Machine Learning", "Field of study that gives computers the ability to learn"),
                ("Deep Learning", "Subset of ML using neural networks"),
                ("Natural Language Processing", "Ability of computers to understand human language"),
                ("Computer Vision", "Enabling machines to interpret visual data"),
                ("OpenCV", "Computer vision library"),
                ("Keras", "Deep learning API in Python"),
                ("Transformers", "Models that use self-attention mechanisms"),
                ("GPT", "Generative Pre-trained Transformer models"),
                ("Reinforcement Learning", "Type of ML based on reward systems"),
                ("Scikit-learn", "Used for implementing ML algorithms")
            ],
            "Cybersecurity": [
                ("Network Security", "Protecting network infrastructure"),
                ("Penetration Testing", "Simulated attack to evaluate security"),
                ("Cryptography", "Securing data through encoding"),
                ("Firewalls", "Systems to block unauthorized access"),
                ("Ethical Hacking", "Authorized attempt to gain access"),
                ("Malware Analysis", "Study of malicious software"),
                ("Wireshark", "Network protocol analyzer"),
                ("Kali Linux", "Linux distro for security auditing"),
                ("SIEM", "Security Information and Event Management"),
                ("Security+ Certification", "Basic certification in cybersecurity")
            ],
            "Database Management": [
                ("MySQL", "Relational database management system"),
                ("PostgreSQL", "Open-source relational database"),
                ("MongoDB", "NoSQL document-based database"),
                ("SQLite", "Lightweight SQL database"),
                ("Redis", "In-memory data structure store"),
                ("Oracle", "Enterprise-grade RDBMS"),
                ("MariaDB", "Community-developed fork of MySQL"),
                ("Cassandra", "Distributed NoSQL database"),
                ("Firebase Realtime DB", "NoSQL cloud-hosted database"),
                ("Elasticsearch", "Search and analytics engine")
            ],
            "Cloud Computing": [
                ("AWS EC2", "Virtual servers on AWS"),
                ("AWS S3", "Object storage service"),
                ("Google Cloud Functions", "Event-driven serverless compute"),
                ("Azure Functions", "Serverless compute service by Azure"),
                ("Heroku", "PaaS for deploying apps"),
                ("DigitalOcean", "Cloud infrastructure provider"),
                ("Cloudflare", "Web performance and security company"),
                ("Firebase Hosting", "Web app hosting platform"),
                ("Netlify", "Hosting for static websites"),
                ("Vercel", "Platform for frontend frameworks and static sites")
            ],
            "Soft Skills": [
                ("Communication", "Ability to effectively share ideas"),
                ("Teamwork", "Work well with others in a group"),
                ("Problem Solving", "Find solutions under constraints"),
                ("Adaptability", "Ability to adjust to change"),
                ("Leadership", "Guide individuals or teams"),
                ("Time Management", "Efficiently manage time and priorities"),
                ("Critical Thinking", "Objective analysis and evaluation"),
                ("Creativity", "Generate unique and original ideas"),
                ("Conflict Resolution", "Manage disputes diplomatically"),
                ("Emotional Intelligence", "Recognize and manage emotions")
            ]
        }

        created_count = 0

        for category, skills in skills_data.items():
            for skill_name, description in skills:
                obj, created = Skills.objects.get_or_create(
                    name=skill_name,
                    defaults={
                        "category": category,
                        "knowledge_level": "E",  # default to Elementary
                        "description": description
                    }
                )
                if created:
                    created_count += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {created_count} skills with descriptions."))
