import streamlit as st
import openai
import base64

# ====================== Custom CSS ==========================
custom_css = """
<style>
/* Gradient Background */
.stApp {
    background: linear-gradient(135deg, #e0eafc, #cfdef3);
    color: #333333;
    font-family: 'Arial', sans-serif;
}

/* Titles */
h1 {
    color: #0a3871;
    text-align: center;
}

h3 {
    color: #333333;
    text-align: center;
}

/* Input box */
input {
    background-color: #ffffff;
    border: 1px solid #0a3871;
    padding: 10px;
    border-radius: 5px;
}

/* Generate Button */
div.stButton > button:first-child {
    background-color: #0a3871;
    color: white;
    border-radius: 8px;
    padding: 0.6em 2em;
    transition: background-color 0.3s ease;
}

div.stButton > button:hover {
    background-color: #072f5f;
}

/* Result Box */
.stMarkdown {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #dddddd;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

footer {
    visibility: hidden;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ====================== Sidebar ==========================
st.sidebar.title("Grow With Me 🌱")
st.sidebar.info(
    """
    **How to Use:**  
    - Enter your product description  
    - Click 'Generate'  
    - Download your catchy subject lines  
    """
)
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by Grow With Me")

# ====================== Brand Logo ==========================
logo_path = "logo.png"  
try:
    file_ = open(logo_path, "rb")
    contents = file_.read()
    logo_base64 = base64.b64encode(contents).decode("utf-8")
    st.markdown(
        f'<div style="text-align:center;"><img src="data:image/png;base64,{logo_base64}" width="150"/></div>',
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.warning("No logo found! Upload 'logo.png' to display your brand logo.")

# ====================== Main App ==========================

# Titles
st.markdown("<h1>AI Email Subject Line & Preview Text Generator</h1>", unsafe_allow_html=True)
st.markdown("<h3>Boost your email open rates with catchy AI-powered subject lines!</h3>", unsafe_allow_html=True)

# OpenAI API Key (Replace with your actual key)
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Input
product_description = st.text_input("Enter your product or email description", "")

generated_text = ""

# Button
if st.button("Generate Email Subject Lines"):
    if product_description:
        with st.spinner("Generating your email magic..."):
            try:
                # OpenAI ChatCompletion API (GPT-3.5 Turbo)
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": f"Create 5 persuasive email subject lines and preview text for: {product_description}"}
                    ],
                    temperature=0.7,
                    max_tokens=300
                )

                generated_text = response['choices'][0]['message']['content'].strip()

                st.success("✅ Your AI-generated subject lines are ready!")
                st.markdown(f"<div class='stMarkdown'>{generated_text}</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"⚠️ Oops! Something went wrong: {e}")
    else:
        st.warning("⚠️ Please enter your product or email description.")

# ====================== Download Button ==========================
if generated_text:
    def text_to_download_link(text, filename, label):
        b64 = base64.b64encode(text.encode()).decode()  # some strings
        href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">{label}</a>'
        return href

    st.markdown("---")
    st.markdown(text_to_download_link(generated_text, "email_subject_lines.txt", "📥 Download as .txt"), unsafe_allow_html=True)

# ====================== Footer ==========================
st.markdown("""
<hr style="margin-top:50px;">
<p style='text-align: center; color: #888888;'>
    © 2025 Grow With Me | Powered by OpenAI
</p>
""", unsafe_allow_html=True)

