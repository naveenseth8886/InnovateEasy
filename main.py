from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

api_key = os.getenv("Groq_API_Key")

# --- Research Agent ---
def research_company(company_name):
    research_agent = Agent(
        name="CompanyResearchAgent",
        model=Groq(
            id="llama-3.3-70b-versatile",
            api_key=api_key
        ),
        tools=[DuckDuckGo()],
        instructions=[
            "You are a research agent tasked with gathering information about a specified company.",
            "Use DuckDuckGo to search for the company's industry, key products/services, and strategic focus areas.",
            "Organize the findings in a clear, structured markdown format with the following sections: Overview, Industry, Products and Services, Strategic Focus Areas, and Sources.",
            "Use bullet points for each section (except Overview) to enhance readability.",
            "Provide at least 2-3 clickable source links in the Sources section.",
            "If no information is found, provide a brief explanation under Overview.",
            "Ensure the output is concise, professional, and well-formatted with proper spacing."
        ],
        show_tool_calls=True,
        markdown=True,
    )
    
    query = f"Research {company_name}. Provide details about its industry, products/services, and strategic focus areas."
    try:
        print(f"Running research query for {company_name}...")
        response = research_agent.run(query, stream=False)
        response_content = response.content if hasattr(response, 'content') else str(response)
        
        # Filter out tool call outputs
        lines = response_content.splitlines()
        clean_content = "\n".join(line for line in lines if not line.startswith("<function=duckduckgo_search"))
        
        # Check if content is empty and provide fallback
        if not clean_content.strip():
            clean_content = f"**Overview**\nNo research data found for {company_name}. Possible issues: limited search results or ambiguous company name. Try specifying the full name (e.g., HCL Technologies).\n\n**Industry**\n- Not available\n\n**Products and Services**\n- Not available\n\n**Strategic Focus Areas**\n- Not available\n\n**Sources**\n- None"
        
        print(f"\nResearch Results for {company_name}:\n")
        print(clean_content)
        
        with open("company_research.md", "w", encoding="utf-8") as f:
            f.write(clean_content)
        
        return clean_content
    except Exception as e:
        error_msg = f"**Overview**\nError in Research Agent for {company_name}: {str(e)}\n\n**Industry**\n- Not available\n\n**Products and Services**\n- Not available\n\n**Strategic Focus Areas**\n- Not available\n\n**Sources**\n- None"
        print(error_msg)
        with open("company_research.md", "w", encoding="utf-8") as f:
            f.write(error_msg)
        return error_msg

# --- Use Case Agent ---
def generate_use_cases(company_name, company_research):
    use_case_agent = Agent(
        name="UseCaseAgent",
        model=Groq(
            id="llama-3.3-70b-versatile",
            api_key=api_key
        ),
        tools=[DuckDuckGo()],
        instructions=[
            "You are an AI use case generation agent.",
            "Use the provided company research to understand the company's industry and strategic focus areas.",
            "Search for AI, Machine Learning, and Generative AI trends in the company's industry using DuckDuckGo.",
            "Generate 3-5 relevant AI use cases that align with the company's goals.",
            "Format the output as follows:",
            "- Use a section titled 'AI Use Cases' with each use case numbered (e.g., '1. AI Use Case Title').",
            "- For each use case, provide a description and a clickable source link in the format: 'Source: [Link Text](URL)'.",
            "- Add a 'Sources' section at the end listing all referenced links in bullet points.",
            "Use bullet points for clarity and ensure proper spacing between sections."
        ],
        show_tool_calls=True,
        markdown=True,
    )
    
    query = f"Based on the following company research, generate 3-5 AI use cases for {company_name}:\n\n{company_research}"
    try:
        print(f"Running use case query for {company_name}...")
        response = use_case_agent.run(query, stream=False)
        response_content = response.content if hasattr(response, 'content') else str(response)
        
        # Filter out tool call outputs
        lines = response_content.splitlines()
        clean_content = "\n".join(line for line in lines if not line.startswith("<function=duckduckgo_search"))
        
        # Check if content is empty
        if not clean_content.strip():
            clean_content = f"**AI Use Cases**\nNo use cases generated for {company_name}. Possible issues: limited research data or API failure.\n\n**Sources**\n- None"
        
        print(f"\nAI Use Cases for {company_name}:\n")
        print(clean_content)
        
        with open("use_cases.md", "w", encoding="utf-8") as f:
            f.write(clean_content)
        
        return clean_content
    except Exception as e:
        error_msg = f"**AI Use Cases**\nError in Use Case Agent for {company_name}: {str(e)}\n\n**Sources**\n- None"
        print(error_msg)
        with open("use_cases.md", "w", encoding="utf-8") as f:
            f.write(error_msg)
        return error_msg

# --- Resource Agent ---
def collect_resources(company_name, use_cases):
    resource_agent = Agent(
        name="ResourceAgent",
        model=Groq(
            id="llama-3.3-70b-versatile",
            api_key=api_key
        ),
        tools=[DuckDuckGo()],
        instructions=[
            "You are a resource collection agent tasked with finding datasets and tools for AI use cases.",
            "Use the provided AI use cases to identify relevant resources.",
            "Search for datasets, models, or tools on Kaggle, HuggingFace, and GitHub using DuckDuckGo.",
            "For each use case, suggest at least one resource with the format: 'Resource: [Resource Name](URL) - Description'.",
            "Format the output with a section for each use case, using bullet points for clarity.",
            "Add a 'Sources' section at the end listing all referenced platforms in bullet points.",
            "If no suitable resource is found, suggest a manual search on the platform.",
            "Ensure proper spacing and consistent formatting."
        ],
        show_tool_calls=True,
        markdown=True,
    )
    
    query = f"For the following AI use cases for {company_name}, suggest one dataset, model, or tool per use case from Kaggle, HuggingFace, or GitHub:\n\n{use_cases}"
    try:
        print(f"Running resource query for {company_name}...")
        response = resource_agent.run(query, stream=False)
        response_content = response.content if hasattr(response, 'content') else str(response)
        
        # Filter out tool call outputs
        lines = response_content.splitlines()
        clean_content = "\n".join(line for line in lines if not line.startswith("<function=duckduckgo_search"))
        
        # Check if content is empty
        if not clean_content.strip():
            clean_content = f"**Resources for AI Use Cases**\nNo resources found for {company_name}. Possible issues: limited search results or API failure.\n\n**Sources**\n- None"
        
        print(f"\nResources for {company_name}'s AI Use Cases:\n")
        print(clean_content)
        
        with open("resources.md", "w", encoding="utf-8") as f:
            f.write(clean_content)
        
        return clean_content
    except Exception as e:
        error_msg = f"**Resources for AI Use Cases**\nError in Resource Agent for {company_name}: {str(e)}\n\n**Sources**\n- None"
        print(error_msg)
        with open("resources.md", "w", encoding="utf-8") as f:
            f.write(error_msg)
        return error_msg

# --- Main Execution ---
if __name__ == "__main__":
    company = "HCL Technologies"
    
    print(f"Starting Multi-Agent System for {company}...")
    
    # Step 1: Run Research Agent
    print("\nRunning Research Agent...")
    company_research = research_company(company)
    
    # Step 2: Run Use Case Agent
    print("\nRunning Use Case Agent...")
    if "Error" not in company_research:
        use_cases = generate_use_cases(company, company_research)
    else:
        print(company_research)
        use_cases = None
    
    # Step 3: Run Resource Agent
    print("\nRunning Resource Agent...")
    if use_cases and "Error" not in use_cases:
        collect_resources(company, use_cases)
    else:
        print("Error: Cannot run Resource Agent without valid use cases.")
    
    print("\nMulti-Agent System completed. Outputs saved to 'company_research.md', 'use_cases.md', and 'resources.md'.")