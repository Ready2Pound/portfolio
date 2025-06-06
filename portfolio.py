import streamlit as st

def download_pdf():
    with open("resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="Download Resume (PDF)",
                data=pdf_file,
                file_name="resume.pdf",
                mime="application/pdf"
            )

def main():

    menu = st.sidebar.radio(
        "Navigate",
        ("About Me", "Skills", "Projects", "Contact")
    )

    if menu == "About Me":
        st.title("Automate & Defend: Nathaniel's Portfolio")
        #st.header("Hello")
        st.write(
            "I am Nathaniel and I am an IT and cybersecurity professional by day, and a builder, learner, and hobby enthusiast by night.\n"
            "I currently support global teams with identity access and incident response.\n"
            "I have over 3 years of professional experience in help desk, system administration, and security operations. Seeking to expand into a junior security or support engineering role.\n"
            "Along the way I have been diving deeper into Python to create simple but useful tools that combine my interests in tech with solving real-world problems.\n"
            "Outside of work, you can find me reading, playing video games, rock climbing, training BJJ or Muay Thai, or testing my patience in a fencing class.\n"
            "I believe hobbies and curiosity fuel creativity, which is evident in my projects and in my demonstrated continued learning beyond traditional schooling."
        )

    elif menu == "Skills":
        st.title("Skills")
        st.write("I bring a hands-on, problem solving approach to IT and cybersecurity. I have a particular interest in automation, identity management, and threat detection.\n"
                "These are some of the tools I have used in real world environments, personal projects, and security labs. \n"
                "Whatever task I work on, I aim to combine reliability with curiosity in everything I do.")
        st.subheader("SIEM")
        st.write("- Microsoft Sentinel: KQL based alerts and Azure playbooks for real time monitoring.")
        st.write("- Splunk")
        st.subheader("EDR & XDR")
        st.write("- Microsoft Defender: Endpoint protection, investigation, and response.")
        st.write("- Perception Point, Crowdstrike Falcon")
        st.subheader("Threat Detection & Response")
        st.write("- Incident triage, alert investigation, escalation procedures.")
        st.subheader("IAM")
        st.write("- Okta administration and access reviews, Active Directory, SSO provisioning")
        st.subheader("Cloud Security")
        st.write("- Orca security, Microsoft Purview")
        st.subheader("Security Frameworks")
        st.write("- Basic understanding of NIST, MITRE ATT&CK")

    elif menu == "Projects":
        st.title("Projects")
        st.subheader("1. Inventory Tracker & Dashboard")
        st.write("Designed a CLI tool to manage product inventory using CSV files. Integrated add/edit/delete/search\n"
                 "function and validations to prevent data entry errors. Features include a web dashboard to help identify stock\n"
                 "readily available, in need of repair, and in transit.")
        st.write("GitHub Repo: [Link](https://github.com/yourusername/project1)")
        st.subheader("2. Expense Tracker")
        st.write("Built a script to track personal expenses with add/view,delete functionality.\n"
                 "Implemented Pandas for data handling and Streamlit for UI. Future updates include charts and export options.")
        st.write("GitHub Repo: [Link](https://github.com/Ready2Pound/expense_tracker)")
        st.subheader("3. SOC Log Analyzer")
        st.write("Developed a Python log parser to extract and organize key system data (IPs, timestamps, user activity), enabling automated analysis and reporting.\n"
                "Enhanced scripting and data processing skills.")
        st.write("GitHub Repo: [Link](https://github.com/Ready2Pound/log_parser)")
        st.subheader("4. Brazilian Jiu Jitsu Trivia Game")
        st.write("This BJJ Quiz Game is a fun quiz that tests your knowledge of Brazilian Jiu-Jitsu with easy and hard difficulty modes.\n" 
                 "Available via a CLI interface and a Streamlit web app, it tracks your score and time to keep your progressing skills motivated.")
        st.write("GitHub Repo: [Link](https://github.com/Ready2Pound/bjj_quiz)")

    elif menu == "Contact":
        st.title("Get in Touch!")
        st.write("Thanks for checking out my portfolio. If you have any questions, feedback, or just want to connect, feel free to reach out!")
        st.write("Email: nathanieljrodriguez@gmail.com")
        st.write("LinkedIn: [Nathaniel](https://www.linkedin.com/in/nathaniel-rodriguez71594/)")
        st.write("Whether it's for a collab, a job opportunity, or just a nerdy conversation about building tools that solve problems, I'd love to hear from you!")

        download_pdf()

if __name__ == "__main__":
    main()
