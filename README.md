InnovateEasy: AI Solutions Explorer for Businesses
Live Demo: https://innovateeasy.onrender.com
Overview
InnovateEasy is a multi-agent AI system designed to help businesses explore AI-driven solutions. It researches a specified company, generates tailored AI use cases, and suggests relevant datasets and tools for implementation. Built with Python, Streamlit, and Groq, the app leverages DuckDuckGo for real-time data and presents results in a user-friendly, markdown-formatted interface.
This project showcases skills in backend development (multi-agent AI logic), frontend development (Streamlit UI), and cloud deployment (GitHub and Render). It demonstrates an end-to-end workflow, from data processing to production deployment.
Features

Company Research: Analyzes a company’s industry, products/services, and strategic focus using AI and web search.
AI Use Cases: Generates 3-5 relevant AI use cases aligned with the company’s goals.
Resource Suggestions: Recommends datasets, models, or tools from platforms like Kaggle, HuggingFace, and GitHub.
Interactive UI: Provides a clean, Streamlit-based interface for users to input company names and view results.
Secure Deployment: Uses environment variables to protect sensitive API keys and a robust CI/CD pipeline.

Tech Stack

Backend: Python, Groq API, phi (multi-agent framework), DuckDuckGo Search
Frontend: Streamlit
Deployment: GitHub, Render
Utilities: python-dotenv (environment variable management)
Version Control: Git

Prerequisites

Python 3.9
Conda (for local environment management)
Groq API key (sign up at https://x.ai/api)
Git installed

Setup Instructions

Clone the Repository:
git clone https://github.com/your-username/Multi-Agent-Use-Case.git
cd Multi-Agent-Use-Case


Create a Conda Environment:
conda create -n innovate-easy python=3.9
conda activate innovate-easy


Install Dependencies:
pip install -r requirements.txt


Set Up Environment Variables:

Create a .env file in the project root:echo Groq_API_Key=your-api-key > .env

Replace your-api-key with your actual Groq API key.


Run the App Locally:
streamlit run streamlit_app.py


Open the provided URL (usually http://localhost:8501) in your browser.



Usage

Open the app (locally or at https://innovateeasy.onrender.com).
Enter a company name (e.g., "HCL Technologies") in the input field.
Click Analyze Company to generate:
Company Research: Industry, products/services, and strategic focus.
AI Use Cases: 3-5 AI-driven solutions tailored to the company.
Resources: Suggested datasets/tools for implementation.


Results are saved as markdown files (company_research.md, use_cases.md, resources.md) locally.

Project Structure
Multi-Agent-Use-Case/
├── .env                # Environment variables (excluded via .gitignore)
├── .gitignore          # Git ignore file
├── main.py             # Core logic for research, use cases, and resources
├── streamlit_app.py    # Streamlit frontend
├── requirements.txt    # Dependencies
├── Procfile            # Render deployment configuration
├── render.yaml         # Render blueprint for deployment
├── README.md           # This file
├── company_research.md # Generated research output (excluded)
├── use_cases.md        # Generated use cases (excluded)
├── resources.md        # Generated resources (excluded)
├── debug.log           # Debug logs (excluded)

Deployment
The app is deployed on Render with the following configuration:

Repository: https://github.com/your-username/Multi-Agent-Use-Case
Platform: Render (free tier)
Build Command: pip install --upgrade pip && pip install -r requirements.txt
Start Command: streamlit run streamlit_app.py --server.port $PORT
Environment Variables:
PYTHON_VERSION=3.9
Groq_API_Key=<your-api-key>


Live URL: https://innovateeasy.onrender.com

To deploy your own instance:

Push the repository to GitHub.
Create a Render web service, connect to your repository, and configure as above.
Add the Groq_API_Key environment variable in Render.

Troubleshooting

API Errors: Ensure your Groq API key is valid and correctly set in .env or Render.
Dependency Issues: Verify requirements.txt versions match the specified ones.
Render Deployment: Check Render logs for build/start errors and adjust PYTHON_VERSION or dependencies if needed.
Local Run Fails: Confirm Python 3.9 and all dependencies are installed in your Conda environment.

Future Improvements

Add support for multiple company inputs in a single session.
Enhance UI with custom CSS and interactive charts.
Integrate additional AI models for deeper analysis.
Optimize performance for faster research and use case generation.

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

xAI: For providing the Groq API.
Streamlit: For the intuitive web app framework.
Render: For seamless cloud deployment.

Contact
For questions or feedback, reach out via LinkedIn or open an issue on GitHub.

Built with 💻 and ☕ by [Your Name]
