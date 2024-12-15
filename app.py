import streamlit as st
import json

st.set_page_config(
    page_title="Interactive JSON Path Finder",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="auto",
)

def build_path_map(data, parent_path=""):
    """
    Build a map of all JSON paths in the structure for dropdown navigation.
    """
    path_map = {}
    if isinstance(data, dict):
        for key, value in data.items():
            full_path = f"{parent_path}.{key}" if parent_path else key
            path_map[full_path] = value
            if isinstance(value, (dict, list)):
                path_map.update(build_path_map(value, full_path))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            full_path = f"{parent_path}[{idx}]"
            path_map[full_path] = item
            if isinstance(item, (dict, list)):
                path_map.update(build_path_map(item, full_path))
    return path_map



st.sidebar.markdown("## Connect with Me")
st.sidebar.markdown(
    """
    <a href="https://github.com/xspoilt-dev" target="_blank" style="text-decoration: none;">
        <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png" style="vertical-align: middle; margin-right: 10px;">
        GitHub
    </a>
    <br>
    <a href="https://x.com/x_spoilt" target="_blank" style="text-decoration: none;">
        <img src="https://img.icons8.com/ios-glyphs/30/1DA1F2/twitter.png" style="vertical-align: middle; margin-right: 10px;">
        Twitter
    </a>
    <br>
    <a href="https://facebook.com/xspoilt" target="_blank" style="text-decoration: none;">
        <img src="https://img.icons8.com/ios-glyphs/30/4267B2/facebook.png" style="vertical-align: middle; margin-right: 10px;">
        Facebook
    </a>
    """,
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")


st.markdown(
    """
    <div style="text-align: center;">
        <h1>🌟 Interactive JSON Path Finder 🌟</h1>
        <p style="font-size: 16px;">Easily navigate and find paths in your JSON files.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("### 📂 Upload JSON File")
uploaded_file = st.file_uploader("Upload a JSON file to get started", type=["json"])

if uploaded_file:
    try:
        with st.spinner("Parsing your JSON file..."):
            json_data = json.load(uploaded_file)

        st.markdown("### ✅ Uploaded JSON Data")
        st.json(json_data, expanded=False)
        path_map = build_path_map(json_data)

        st.markdown("---")
        st.markdown("### 🔍 Select a Variable Path")
        selected_path = st.selectbox(
            "Choose a path from the dropdown below:", list(path_map.keys())
        )

        if selected_path:
            st.success(f"Selected JSON Path: `{selected_path}`")
            st.code(selected_path, language="text")
            st.markdown("### 🧾 Value at Selected Path")
            st.write(path_map[selected_path])

        st.markdown("---")

        st.markdown(
            """
            <div style="text-align: center; margin-top: 20px;">
                <p style="font-size: 14px;">Made with ❤️ by @x_spoilt</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    except Exception as e:
        st.error(f"Error parsing JSON: {e}")
else:
    st.info("Upload a JSON file to begin.")
