import streamlit as st
import openai
import datetime

# Page setup
st.set_page_config(
    page_title="AI Email Subject Line Generator",
    page_icon="📧",
    layout="centered"
)

# --- Dark/Light Mode Toggle ---
dark_mode = st.toggle("🌙 Dark Mode", value=False)

if dark_mode:
    custom_css = """
    <style>
    .stApp { background-color: #1e1e1e; color: #ffffff; }
    .main-container { background: #2c2c2c; color: #ffffff; }
    .stSidebar { background-color: #111827 !important; color: #ffffff !important; }
    .stSidebar * { color: #ffffff !important; } /* Fixes all sidebar text */
    input, textarea { background: #333; color: #ffffff !important; }
    div.stButton > button:first-child { background-color: #4f46e5; color: #ffffff !important; }
    h1, h2, h3, h4, h5, h6, p, label { color: #ffffff !important; }
    </style>
    """
else:
    custom_css = """
    <style>
    .stApp { background-color: #f9fafb; }
    .main-container { background: white; color: #000000; } /* Fix text visibility */
    .stSidebar { background-color: #f3f4f6 !important; color: #000000 !important; }
    div.stButton > button:first-child { background-color: #2563eb; color: #ffffff !important; }
    h1, h2, h3, h4, h5, h6, p, label { color: #000000 !important; } /* ✅ Ensures text is visible */
    </style>
    """

st.markdown(custom_css, unsafe_allow_html=True)

# Logo
st.image('logo.png', width=150)

# Main Title & Subheading
st.title("AI Email Subject Line & Preview Text Generator")
st.subheader("Boost your email open rates with catchy AI-powered subject lines!")

# OpenAI API Key (Replace with actual key)
openai.api_key = "your-openai-api-key"

# Main container
with st.container():
    recipient_name = st.text_input("Enter recipient's name (optional)", "")
    product_description = st.text_area("Enter your product or email description", "")

    # Generate Button
    if st.button("Generate Email Subject Lines"):
        if product_description:
            with st.spinner("Generating..."):
                
                # OpenAI API call to generate subject lines
                prompt = f"Create 5 catchy email subject lines and preview text for: {product_description}"
                if recipient_name:
                    prompt = f"Personalize the subject lines for {recipient_name}. {prompt}"

                client = openai.OpenAI()  # ✅ Use the new API client
                
                response = client.chat.completions.create(  # ✅ Correct method
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert email marketing assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=150,
                    temperature=0.7
                )

                # Extract generated text
                generated_text = response.choices[0].message.content.strip()

                # Display Results
                st.success("Here are your AI-generated email subject lines & preview text!")
                st.markdown(f"```{generated_text}```")

                # Download Button
                file_name = f"email_subjects_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                st.download_button("📥 Download as TXT", generated_text, file_name)
        else:
            st.warning("⚠️ Please enter your product description.")

# Sidebar
with st.sidebar:
    st.markdown("## How to Use:")
    st.markdown("""
    👉 **Enter recipient's name** (optional)  
    👉 **Enter your product description**  
    👉 Click **'Generate'**  
    👉 **Copy or download** the subject lines  
    """)
    st.markdown("---")
    st.markdown("### Made with ❤️ by Grow With Me")

# Footer Text
st.markdown("---")
st.caption("© 2025 Grow With Me | Powered by OpenAI")

