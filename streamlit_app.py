import streamlit as st
import os
import logging
from main import research_company, generate_use_cases, collect_resources

# Debug toggle (set to True to enable logging, False to disable)
DEBUG = False

# Configure backend logging
logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Debug logging function (logs only if DEBUG is True)
def log_debug(message):
    if DEBUG:
        logger.debug(message)

# Streamlit app
st.title("InnovateEasy: AI Solutions Explorer for Businesses")

# Input field and button
company_name = st.text_input("Enter Company Name (e.g., HCL Technologies):", value="HCL Technologies")
if st.button("Analyze Company"):
    if not company_name:
        st.error("Please enter a company name.")
    else:
        with st.spinner(f"Analyzing {company_name}..."):
            try:
                # Set working directory to script's directory
                os.chdir(os.path.dirname(os.path.abspath(__file__)))
                log_debug(f"Working directory set to: {os.getcwd()}")

                # Step 1: Run Research Agent
                log_debug("Running Research Agent...")
                company_research = research_company(company_name)
                log_debug(f"Research Agent output (first 200 chars): {company_research[:200]}...")

                # Step 2: Run Use Case Agent
                log_debug("Running Use Case Agent...")
                use_cases = generate_use_cases(company_name, company_research)
                log_debug(f"Use Case Agent output (first 200 chars): {use_cases[:200]}...")

                # Step 3: Run Resource Agent
                log_debug("Running Resource Agent...")
                resources = collect_resources(company_name, use_cases)
                log_debug(f"Resource Agent output (first 200 chars): {resources[:200]}...")

                # Display results
                st.markdown(f"## Analysis for {company_name}")
                st.markdown("---")

                # Company Research Section
                st.markdown("### Company Research")
                file_path = os.path.join(os.getcwd(), "company_research.md")
                log_debug(f"Checking for file: {file_path}")
                if os.path.exists(file_path):
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            md_content = f.read()
                        if md_content.strip():
                            st.markdown(md_content, unsafe_allow_html=True)
                        else:
                            st.warning("Company research data is empty.")
                    except Exception as e:
                        st.error(f"Failed to read company_research.md: {str(e)}")
                        log_debug(f"Error reading company_research.md: {str(e)}")
                else:
                    st.error(f"company_research.md not found at {file_path}.")
                    log_debug(f"company_research.md not found at {file_path}")
                st.markdown("---")

                # AI Use Cases Section
                st.markdown("### AI Use Cases")
                file_path = os.path.join(os.getcwd(), "use_cases.md")
                log_debug(f"Checking for file: {file_path}")
                if os.path.exists(file_path):
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            md_content = f.read()
                        if md_content.strip():
                            st.markdown(md_content, unsafe_allow_html=True)
                        else:
                            st.warning("AI use cases data is empty.")
                    except Exception as e:
                        st.error(f"Failed to read use_cases.md: {str(e)}")
                        log_debug(f"Error reading use_cases.md: {str(e)}")
                else:
                    st.error(f"use_cases.md not found at {file_path}.")
                    log_debug(f"use_cases.md not found at {file_path}")
                st.markdown("---")

                # Resources Section
                st.markdown("### Resources for AI Implementation")
                file_path = os.path.join(os.getcwd(), "resources.md")
                log_debug(f"Checking for file: {file_path}")
                if os.path.exists(file_path):
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            md_content = f.read()
                        if md_content.strip():
                            st.markdown(md_content, unsafe_allow_html=True)
                        else:
                            st.warning("Resources data is empty.")
                    except Exception as e:
                        st.error(f"Failed to read resources.md: {str(e)}")
                        log_debug(f"Error reading resources.md: {str(e)}")
                else:
                    st.error(f"resources.md not found at {file_path}.")
                    log_debug(f"resources.md not found at {file_path}")
                st.markdown("---")

            except Exception as e:
                st.error(f"Error running analysis: {str(e)}")
                log_debug(f"Full error: {str(e)}")

# Instructions
st.markdown("---")
st.markdown("""
### Instructions
1. **Enter a Company Name**: Provide the exact company name (e.g., HCL Technologies) for accurate results.  
2. **Run Analysis**: Click "Analyze Company" to generate research, AI use cases, and resources.  
3. **View Results**: Scroll down to see the detailed outputs for each section.  
4. **Troubleshooting**: Ensure the company name is specific. Contact support if issues persist.
""")

# Footer
st.markdown("---")
st.markdown("InstaResz AI Assignment | Powered by Streamlit")