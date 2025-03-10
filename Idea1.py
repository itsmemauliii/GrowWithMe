import streamlit as st
import openai

# Title and Description
st.title("AI Email Subject Line & Preview Text Generator")
st.subheader("Boost your email open rates with catchy AI-powered subject lines!")

# OpenAI API Key Setup
openai.api_key = 'Grow With Me'  # Replace this with your key

# Input Fields
product_description = st.text_input("Enter your product or email description", "")

if st.button("Generate Email Subject Lines"):
    if product_description:
        with st.spinner("Generating..."):
            # Call OpenAI to generate subject lines
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Create 5 persuasive email subject lines and preview text for: {product_description}",
                max_tokens=150,
                temperature=0.7
            )
            generated_text = response.choices[0].text.strip()

            # Display results
            st.success("Here are your AI-generated email subject lines & previews!")
            st.write(generated_text)
    else:
        st.warning("Please enter your product description.")
