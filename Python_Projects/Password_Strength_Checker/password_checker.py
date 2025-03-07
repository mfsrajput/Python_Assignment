import re
import streamlit as st

def check_password_strength(password):
    messages = []
    if len(password) < 8:
        messages.append("🔴 Password must be at least 8 characters long")
    if not any(char.isdigit() for char in password):
        messages.append("🔴 Password must contain at least one digit")
    if not any(char.isupper() for char in password):
        messages.append("🔴 Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        messages.append("🔴 Password must contain at least one lowercase letter")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        messages.append("🟠 Password should include at least one special character for better security")
    
    if not messages:
        return "🟢 Strong: Your password is well-secured! Great job! ✅", "#4CAF50"
    
    if len(messages) <= 2:
        return ("🟠 Medium: Your password is decent but could be stronger! Consider using a mix of: "
                "<br>✅ Uppercase & lowercase letters "
                "<br>✅ Digits (0-9) "
                "<br>✅ Special characters (!@#$%^&*) "
                "<br>🔒 A stronger password keeps your data safer!"), "#FFA500"
    
    return ("🔴 Weak: Your password is too weak! Consider using a mix of: "
            "<br>✅ Uppercase & lowercase letters "
            "<br>✅ Digits (0-9) "
            "<br>✅ Special characters (!@#$%^&*) "
            "<br>🔒 A strong password keeps your data safe!"), "#FF4B4B"

# Streamlit UI
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        .main { background-color: #f0f2f5; padding: 20px; }
        h1 { color: #1F618D; text-align: center; font-weight: bold; }
        .stTextInput { text-align: center; }
        .password-box { background-color: white; padding: 10px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

st.title("🔑 Secure Password Strength Checker")
st.markdown("#### 🔐 Create a strong password to protect your accounts!")

password = st.text_input("Enter your password", type="password", key="password_input")

if password:
    strength, color = check_password_strength(password)
    st.markdown(f'<div class="password-box"><p style="color: {color}; font-size: 18px; text-align: center; font-weight: bold;">{strength}</p></div>', unsafe_allow_html=True)

