import streamlit as st
import openai

# Set up page configuration
st.set_page_config(
    page_title="AI Email Subject Line Generator",
    page_icon="📧",
    layout="centered"
)

# Custom CSS with background, fonts, and animations
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Open Sans', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #eef2f3, #8e9eab);
    color: #333333;
    padding: 0;
}

/* Title */
h1 {
    color: #0a3871;
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* Subtitle */
h3, .stSubheader {
    color: #333333;
    text-align: center;
    font-size: 18px;
    font-weight: 400;
    margin-bottom: 20px;
}

/* Text input box */
input {
    background-color: #ffffff !important;
    color: #333333 !important;
    border: 1px solid #0a3871 !important;
    padding: 12px !important;
    font-size: 16px !important;
    border-radius: 8px !important;
}

/* Generate Button */
div.stButton > button:first-child {
    background-color: #0a3871;
    color: white;
    font-size: 16px;
    font-weight: 600;
    border-radius: 8px;
    padding: 0.8em 2.5em;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

div.stButton > button:hover {
    background-color: #072f5f;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.15);
}

/* Output box */
.stMarkdown {
    background-color: #ffffff;
    color: #333333;
    padding: 20px;
    font-size: 16px;
    border-radius: 12px;
    border: 1px solid #dddddd;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #1e1e2f;
}

section[data-testid="stSidebar"] .css-1d391kg {
    color: #ffffff;
}

section[data-testid="stSidebar"] .stMarkdown {
    color: #ffffff;
}

footer {
    visibility: hidden;
}

</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Title and Description
st.title("AI Email Subject Line & Preview Text Generator")
st.subheader("Boost your email open rates with catchy AI-powered subject lines!")

# OpenAI API Key (Replace with your actual API Key)
openai.api_key = 'Grow With Me'  # Replace this with your key

# Sidebar instructions
with st.sidebar:
    st.markdown("## How to Use:")
    st.markdown("""
    1. Enter your product description  
    2. Click **'Generate'**  
    3. Download your catchy subject lines  
    """)
    st.markdown("---")
    st.markdown("Made with ❤️ by Grow With Me")

# Input Fields
product_description = st.text_input("Enter your product or email description", "")

# Generate Button
if st.button("Generate Email Subject Lines"):
    if product_description:
        with st.spinner("Generating..."):
            # OpenAI API call to generate subject lines
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Create 5 persuasive email subject lines and preview text for: {product_description}",
                max_tokens=150,
                temperature=0.7
            )
            generated_text = response.choices[0].text.strip()

            # Display Results
            st.success("Here are your AI-generated email subject lines & previews!")
            st.markdown(f"```{generated_text}```")
    else:
        st.warning("Please enter your product description.")

# Footer
st.markdown("---")
st.caption("© 2025 Grow With Me | Powered by OpenAI")
