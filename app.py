import streamlit as st

st.set_page_config(page_title="Student Profile Application", page_icon="🎓", layout="centered")

st.title("🎓 Student Profile Application") 
st.caption("Developed by Student Name")  # <-- replace with your name

name = st.text_input("Student Name", placeholder="Enter your name")
usn = st.text_input("USN / Roll Number", placeholder="Enter roll number")
department = st.selectbox("Department", ["CSE", "ISE", "ECE", "EEE", "ME", "CV", "AI & ML", "Other"])
year = st.radio("Current Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])

if st.button("View My Profile"):
    if not name.strip() or not usn.strip():
        st.warning("Please enter both your name and USN / Roll Number.")
    else:
        st.success("Profile generated successfully!")
        st.subheader("Student Profile")
        st.write(f"**Name:** {name}")
        st.write(f"**USN / Roll Number:** {usn}")
        st.write(f"**Department:** {department}")
        st.write(f"**Current Year:** {year}")
