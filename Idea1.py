import streamlit as st
import openai

# Page setup
st.set_page_config(
    page_title="AI Email Subject Line Generator",
    page_icon="📧",
    layout="centered"
)

# --- CSS Styling ---
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Open Sans', sans-serif;
}

/* Background */
.stApp {
    background-color: #f9fafb;
}

/* Main container */
.main-container {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    margin-top: 20px;
}

/* Title */
h1 {
    color: #1f2937;
    text-align: center;
    font-weight: 700;
    margin-bottom: 10px;
}

/* Subheader */
h3, .stSubheader {
    color: #4b5563;
    text-align: center;
    font-weight: 400;
    margin-bottom: 20px;
}

/* Input */
input {
    padding: 12px !important;
    border-radius: 8px !important;
    border: 1px solid #d1d5db !important;
    font-size: 16px !important;
}

/* Button */
div.stButton > button:first-child {
    background-color: #2563eb;
    color: white;
    font-size: 16px;
    font-weight: 600;
    padding: 0.75em 2.5em;
    border-radius: 8px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

div.stButton > button:hover {
    background-color: #1d4ed8;
    transform: translateY(-2px);
}

/* Output box */
.stMarkdown {
    background-color: #f3f4f6;
    padding: 20px;
    font-size: 16px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    margin-top: 20px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

section[data-testid="stSidebar"] .css-1d391kg, 
section[data-testid="stSidebar"] .stMarkdown {
    color: #f9fafb;
}

footer {
    visibility: hidden;
}
</style>
"""

# Inject CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Logo
st.image('logo.png', width=150)

# Main Title & Subheading
st.title("AI Email Subject Line & Preview Text Generator")
st.subheader("Boost your email open rates with catchy AI-powered subject lines!")

# Main container
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # API Key (Replace with your actual OpenAI API Key)
    openai.api_key = 'Grow With Me'  # Replace this with your OpenAI key

    # Input Field
    product_description = st.text_input("Enter your product or email description", "")

    # Generate Button
    if st.button("Generate Email Subject Lines"):
        if product_description:
            with st.spinner("Generating..."):
                # OpenAI API call to generate subject lines
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Create 5 catchy email subject lines and preview text for: {product_description}",
                    max_tokens=150,
                    temperature=0.7
                )
                generated_text = response.choices[0].text.strip()

                # Display Results
                st.success("Here are your AI-generated email subject lines & preview text!")
                st.markdown(f"```{generated_text}```")
        else:
            st.warning("Please enter your product description.")

    st.markdown('</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## How to Use:")
    st.markdown("""
    👉 Enter your product description  
    👉 Click **'Generate'**  
    👉 Copy and use the subject lines  
    """)
    st.markdown("---")
    st.markdown("### Made with ❤️ by Grow With Me")

# Footer Text
st.markdown("---")
st.caption("© 2025 Grow With Me | Powered by OpenAI")

