import streamlit as st
import random
import string

def generate_password(Length,us_digits,use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits #adds digits to the characters

    if use_special:
        characters += string.punctuation #adds special characters
    
    return ''.join(random.choice(characters)for _ in range(Length))

st.title("Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("include digits")
use_special = st.checkbox("include special characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"Generated Password: `{password}`")

st.write("--------------------------------")
st.write("Build with ❤️ by [Farhan Rajput](https://github.com/mfsrajput)")

