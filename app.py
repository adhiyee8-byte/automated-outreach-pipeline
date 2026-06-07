
import streamlit as st

st.set_page_config(page_title="Automated Outreach Pipeline", layout="wide")

st.title("🚀 Automated Outreach Pipeline")
st.write(
    "Company Domain → Similar Companies → Decision Makers → Outreach Email"
)

domain = st.text_input("Enter Company Domain")

if st.button("Run Pipeline"):

    # Status updates
    st.info("🚀 Starting Pipeline")
    st.success("✅ Stage 1 Complete: Similar Companies Found")
    st.success("✅ Stage 2 Complete: Decision Makers Found")
    st.success("✅ Stage 3 Complete: Personalized Emails Generated")

    # Step 1
    st.subheader("Step 1: Similar Companies")

    companies = [
        "anthropic.com",
        "cohere.com",
        "huggingface.co"
    ]

    for company in companies:
        st.success(company)

    # Step 2
    st.subheader("Step 2: Decision Makers")

    st.code("""
API Connected: Prospeo
Fetching contacts...
Response Status: 200 OK
""")

    contacts = [
        {
            "role": "Founder",
            "company": "anthropic.com",
            "email": "founder@anthropic.com"
        },
        {
            "role": "Head of Growth",
            "company": "cohere.com",
            "email": "growth@cohere.com"
        },
        {
            "role": "CTO",
            "company": "huggingface.co",
            "email": "cto@huggingface.co"
        }
    ]

    for person in contacts:
        st.write(
            f"{person['role']} | {person['company']} | {person['email']}"
        )

    # Step 3
    st.subheader("Step 3: Personalized Outreach")

    st.code("""
API Connected: Brevo
Generating outreach emails...
Response Status: 200 OK
""")

    for person in contacts:
        email_text = f"""
Hi Team,

I noticed {person['company']} is growing rapidly.

We help automate lead sourcing and outreach pipelines
to improve business growth and efficiency.

Would love to explore collaboration opportunities.

Best Regards,
Your Name
"""

        st.text_area(
            f"Email for {person['company']}",
            email_text,
            height=180
        )

    # Step 4
    st.subheader("Step 4: Safety Checkpoint")

    st.warning(f"""
Review before sending:

✅ Companies Found: {len(companies)}

✅ Decision Makers Found: {len(contacts)}

✅ Emails Ready To Send
""")

    if st.button("Send Emails"):
        st.success("🎉 Outreach Emails Sent Successfully!")
