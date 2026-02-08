import streamlit as st
import requests
import base64
import urllib.parse

# 🔥 Single API base URL (easy to change later)
API = "https://fastapiphotovideosharing.onrender.com"

st.set_page_config(page_title="FAStAPI Social", layout="wide")

# Session state
if "token" not in st.session_state:
    st.session_state.token = None
if "user" not in st.session_state:
    st.session_state.user = None


def get_headers():
    if st.session_state.token:
        return {"Authorization": f"Bearer {st.session_state.token}"}
    return {}


# ---------------- LOGIN ----------------
def login_page():
    st.title("🚀 Welcome to FASTAPI Social")

    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")

    if email and password:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Login", type="primary", use_container_width=True):
                login_data = {"username": email, "password": password}

                try:
                    response = requests.post(f"{API}/auth/jwt/login", data=login_data)
                except requests.exceptions.RequestException:
                    st.error("Backend not reachable")
                    return

                if response.status_code == 200:
                    token_data = response.json()
                    st.session_state.token = token_data["access_token"]

                    user_response = requests.get(f"{API}/users/me", headers=get_headers())
                    if user_response.status_code == 200:
                        st.session_state.user = user_response.json()
                        st.rerun()
                    else:
                        st.error("Failed to fetch user info")
                else:
                    st.error("Invalid email or password")

        with col2:
            if st.button("Sign Up", use_container_width=True):
                signup_data = {"email": email, "password": password}
                response = requests.post(f"{API}/auth/register", json=signup_data)

                if response.status_code == 201:
                    st.success("Account created! Login now ✅")
                else:
                    error_detail = response.json().get("detail", "Registration failed")
                    st.error(error_detail)


# ---------------- UPLOAD ----------------
def upload_page():
    st.title("📸 Share Something")

    uploaded_file = st.file_uploader("Choose media", type=["png", "jpg", "jpeg", "mp4"])
    caption = st.text_area("Caption:")

    if uploaded_file and st.button("Share"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        data = {"caption": caption}

        response = requests.post(f"{API}/upload", files=files, data=data, headers=get_headers())

        if response.status_code == 200:
            st.success("Posted!")
            st.rerun()
        else:
            st.error("Upload failed")


# ---------------- FEED ----------------
def feed_page():
    st.title("🏠 Feed")

    response = requests.get(f"{API}/feed", headers=get_headers())

    if response.status_code != 200:
        st.error("Failed to load feed")
        return

    posts = response.json()["posts"]

    if not posts:
        st.info("No posts yet!")
        return

    for post in posts:
        st.markdown("---")
        st.markdown(f"**{post['email']}** • {post['created_at'][:10]}")

        caption = post.get("caption", "")

        if post["file_type"] == "image":
            st.image(post["url"], width=300)
        else:
            st.video(post["url"], width=300)
            st.caption(caption)


# ---------------- APP ----------------
if st.session_state.user is None:
    login_page()
else:
    st.sidebar.title(f"👋 Hi {st.session_state.user['email']}!")

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.session_state.token = None
        st.rerun()

    page = st.sidebar.radio("Navigate:", ["🏠 Feed", "📸 Upload"])

    if page == "🏠 Feed":
        feed_page()
    else:
        upload_page()
