import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image, ImageDraw
from streamlit_lottie import st_lottie
import json
import base64
import io
import os
from datetime import datetime

st.set_page_config(page_title=" Sathish Duraiyan",page_icon="asset/icons8-anonymous-mask-40.png", layout="wide", initial_sidebar_state="auto")

with st.sidebar:
    selected = option_menu(
                            'Menu',
                            ['About Me','Acedemics', 'Projects', 'Resume','Achievements','Technical Profiles','Coding Blogs','Problem of the Day'],
                            icons=['person-hearts','mortarboard', 'tools','person-lines-fill','patch-check-fill','person-badge','code','calendar-day'])


if selected == "About Me":
    
    
    # Create two columns with equal proportions
    col1, col2 = st.columns([2, 1])

    # Display the text in the left column
    with col1: 
        
        st.write("<div style='margin-top:90px;'></div>", unsafe_allow_html=True)
        st.write("""
        <div>
            <p style="font-size:40px; font-weight:550; color:#d2d6d2">Hey There!, Welcome👋 </p>
                <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=26&duration=4000&pause=1000&color=0cc218&multiline=true&random=true&width=435&lines=Hello!+I'm+Sathish+Duraiyan" alt="" style="height:120px;width: 700px; margin-top:-30px"/>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='width:90%;margin-top:-25px;'>"
        "<p style='font-family: Courier New; font-size: 18px; text-align: justify;color:#b4bfb5'>I'm a Software Engineer currently pursuing my final year in Computer Science and Engineering. I have a keen interest in frontend design and development, as well as data analytics and visualization using Power BI.</p>"            "<p style='font-family: Courier New; font-size: 17px;text-align:justify;color:#b4bfb5'>Thanks for visiting my page! To pick more about me, explore the items in the Menu :)</p>"
        "</div>", unsafe_allow_html=True)

        #i nedd to add the social media links here
        #linkedin,mail,instagram
        st.write("""
            <div style="display: flex; justify-content: ; align-items: center;">
            <a href='https://www.linkedin.com/in/sathish-duraiyan-043a1624b/' target='_blank' style='margin-right: 10px;'>
            <img width="30" height="30" src="https://img.icons8.com/fluency/40/linkedin.png" alt="linkedin"/>
            </a>
            <a href="https://mail.google.com/mail/?view=cm&fs=1&to=sathishduriyan6@gmail.com" target="_blank" style="margin-right: 10px;">
                <img width="30" height="30" src="https://img.icons8.com/fluency/48/gmail-new.png" alt="gmail-new"/>
            </a>
            <a href='https://www.instagram.com/sathishhz/' target='_blank'>
            <img width="30" height="30" src="https://img.icons8.com/color/40/instagram-new--v1.png" alt="instagram-new--v1"/>
            </a>
            </div>
            """, unsafe_allow_html=True)
    # Display the image in the right column
    with col2:
        st.write("<div style='margin-top:80px;'></div>", unsafe_allow_html=True)
        img = Image.open('asset/Me.jpg')
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        # Convert the image to bytes
        byte_arr = io.BytesIO()
        img.save(byte_arr, format='JPEG')
        byte_arr = byte_arr.getvalue()

        # Encode the bytes to base64
        b64_string = base64.b64encode(byte_arr).decode()
        st.write(f"""
        <div style='border-radius: 50%; overflow: hidden; box-shadow: 0px 0px 60px 0px rgba(0,128,0,1);'>
            <img src='data:image/png;base64,{b64_string}' style='width: 100%; height: auto;'>
        </div>
        """, unsafe_allow_html=True)

if selected == "Acedemics":
    col1, col2 = st.columns([2,2])
    with col1:
        #st.markdown("<style>body { font-family: Courier New; font-size: 10px; }</style>", unsafe_allow_html=True)
        st.markdown("<div style=''><h1 style='font-size:35px;color:;margin-top:30px'>Acedemic Progress</h1></div>", unsafe_allow_html=True)

        st.markdown("<div style='color: #0cc218;font-size: 25px; font-weight: bold;'>UG / Computer Science and Engineering</div>", unsafe_allow_html=True)
        st.markdown("**Knowledge Institute of Technology, Salem**", unsafe_allow_html=True)
        st.markdown("<div style='font-family: Courier New; color:; font-size: 15px; font-weight: bold;'>2021 - 2025</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-family: Courier New; color:; font-size: 15px; font-weight: bold;margin-bottom:15px'>CGPA : 8.24/10 (upto 5th sem)</div>", unsafe_allow_html=True)


        st.markdown("<div style='color:#0cc218;font-size: 25px; font-weight: bold;'>HSC / Maths-Biology</div>", unsafe_allow_html=True)
        st.markdown("**Swamy Vivekanandar Matric Higher Secondary School, Salem**", unsafe_allow_html=True)
        st.markdown("<div style='font-family: Courier New; color:; font-size: 15px; font-weight: bold;'>2020 - 2021</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-family: Courier New; color:; font-size: 15px; font-weight: bold;margin-bottom:15px'>Percentage: 91.16%</div>", unsafe_allow_html=True)

        st.markdown("<div style='color: #0cc218;font-size: 25px; font-weight: bold;'>SSLC</div>", unsafe_allow_html=True)
        st.markdown("**Swamy Vivekanandar Matric Higher Secondary School, Salem**", unsafe_allow_html=True)
        st.markdown("<div style='font-family: Courier New; color: ; font-size: 15px; font-weight: bold;'>2018 - 2019</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-family: Courier New; color: ; font-size: 15px; font-weight: bold;margin-bottom:15px'>Percentage: 92.40%</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='margin-top: -50px;'></div>", unsafe_allow_html=True)
        with open("asset/Animation - 1719155339760.json") as f:
            animation = json.load(f)
            st_lottie(animation, speed=0.5, width=500, height=500, key="initial")


if selected == "Resume":
    # Open the PDF file in binary mode
    with open("asset/SathishDuraiyanResume.pdf", "rb") as pdf_file:
        # Read the PDF file and encode it in base64
        base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
    
    # Embed the base64 encoded PDF using an HTML <embed> tag within an iframe, centered on the page
    pdf_display = f'''
    <div style="display: flex; justify-content: center; align-items: center;">
        <iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf" style="border:none;"></iframe>
    </div>
    '''
    
    # Use unsafe_allow_html=True to allow HTML tags
    st.markdown(pdf_display, unsafe_allow_html=True)


if selected == "Coding Blogs":
    # Define a function to r

    def read_markdown_file(markdown_file):
        with open(markdown_file, "r", encoding="utf-8") as file:
            content = file.read()
        return content

    # Main page content
    st.write("<div style='margin-top:0px;'></div>", unsafe_allow_html=True)
    st.write("""
    <div>
        <p style="font-size:40px; font-weight:550; color:#0fdb46">Java Blogs🛠️</p>
    </div>
    """, unsafe_allow_html=True)

    # Topics and their corresponding markdown files

    
    def read_markdown_file(markdown_file):
        with open(markdown_file, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    
    portfolio_path = "blogs"  # Adjust this path to your portfolio directory
    
    # Initialize topics_files outside the loop
    topics_files = {}
    
    # Correctly traverse the directory structure
    for root, dirs, files in os.walk(portfolio_path, topdown=True):
        for dir in dirs:
            topic_path = os.path.join(root, dir)
            # Ensure only markdown files are added
            markdown_files = [f for f in os.listdir(topic_path) if f.endswith('.md')]
            if markdown_files:  # Only add if there are markdown files
                topics_files[dir] = [os.path.join(topic_path, file) for file in markdown_files]
    
    # Create two main columns: one for the topics and files, and another for the content
    col1, col2 = st.columns([1, 3])
    
    with col1:
        selected_file = None
        # Generate expanders for each topic and list files within them
        for topic, files in topics_files.items():
            with st.expander(topic):
                for file in files:
                    file_name = os.path.basename(file)
                    if st.button(file_name, key=f"{topic}_{file}"):
                        selected_file = file
    
    with col2:
        if selected_file:
            st.markdown(read_markdown_file(selected_file))
            st.markdown("---")
            pass
        else:
            st.markdown("<div style='width:90%;margin-top:-5px;text-align:center'>"
                "<p style='font-family: Courier New; font-size: 17px; text-align: justify;color:#b4bfb5;'>Problems I've solved in my day-to-day life are updated here. This includes fundamentals of Java and data structures using Java, along with insights into other programming languages that will be added in the future.</p>"
                "</div>", unsafe_allow_html=True)
            col1, col2 = st.columns([1,4])
            with col2:
                with open("asset/Animation - 1719348566011.json") as f:
                    animation = json.load(f)
                    st_lottie(animation, speed=0.5, width=600, height=500, key="initial")

    # Example main projects data
    

if selected == "Projects":
    main_projects = [
        {
            "name": "Occupational Healthcare Management System",
            "url": "https://www.figma.com/proto/WeOFu28lDNKG35RozDTPcV/New-JSW-OHC?node-id=2-8&t=7TI0DGMFhPk1fKxr-0&scaling=scale-down&content-scaling=fixed&page-id=2%3A4",
            "description": "In this Figma design, it works as a team to design this. It helps show the data entry of employee health records and highlights employee health records. It is developed using Python as a web application.",
            "tools": "Figma"
        },
        {
            "name":"Bus Ticket Booking Analtyics",
            "url":"https://app.powerbi.com/groups/4246783d-8fd0-4ae8-87f7-6eec861c8a03/reports/228740e7-9ba0-42e0-9a69-85d480ae353e/ReportSection?experience=power-bi",
            "description":"In this project, I needed to search for bus ticket analysis data. Since I didn't have proper data, I created a sample dataset using NumPy and pandas with the help of ChatGPT. This sample dataset looks like real-time data and was used to perform analysis in Power BI.",
            "tools":"Power BI, Python, Chat-GPT"
        }
    ]

    project_ideas = [
        {
            "name": "Bus Ticket Booking System",
            "url": "https://www.figma.com/proto/zqfunFkAAqLLKjIpJ5ePoM/Untitled?node-id=75-2&t=DBlMVcvVbmgxTCAJ-0&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=75%3A2",
            "description": "In this Figma design, I worked on making it easy to book tickets and ensuring the UI is comfortable for both customers and passengers to manage and view.",
            "tools": "Figma"
        },
        
        # Add more project ideas as needed
    ]

    st.markdown("<p style='color: #0fdb46; font-weight: 900;font-size:30px;'>Projects</p>", unsafe_allow_html=True)
    for project in main_projects:
        cols = st.columns([2,2])  # Adjust the ratio as needed
        with cols[0]:
            st.markdown(f"[{project['name']}]({project['url']})")
            st.markdown(f"<span style='color: #0fdb46;'>**Tools Used:**</span> {project['tools']}", unsafe_allow_html=True)
        with cols[1]:
            st.write(project['description'])
        st.markdown("---")    
    
    st.markdown("<p style='color: #0fdb46; font-weight: 900;font-size:30px;'>Mini Projects</p>", unsafe_allow_html=True)
    for idea in project_ideas:
        cols = st.columns([2,2])  # Adjust the ratio as needed
        with cols[0]:
            st.markdown(f"[{idea['name']}]({idea['url']})")
            st.markdown(f"<span style='color: #0fdb46;'>**Tools Used:**</span> {idea['tools']}", unsafe_allow_html=True)

        with cols[1]:
            st.write(idea['description'])
        st.markdown("---")    

        # Optional: Adds a separator between files # Optional: Adds a separator between files  # Optional: Adds a separator between files
if selected == "Achievements":
    st.write("<p style='font-size:30px;color:#0fdb46;font-weight:bold'>Achievements</p>",unsafe_allow_html=True)
    r1c1,r1c2 = st.columns([1,3])

    with r1c1:
        st.write("<p style='font-size:20px;color:white;font-weight:Bold'>Awards</p>", unsafe_allow_html=True)
    with r1c2:
        st.write("<p style='font-size:20px;color:white;font-weight:Bold'>Key Achievement</p>", unsafe_allow_html=True)

    st.write("---")
    r2c1,r2c2 = st.columns([1,3])
    with r2c1:
        st.write("<p style='font-size:15px;color:white'>KIOT Achievers Award 2023-24</p>", unsafe_allow_html=True)
    with r2c2:
        st.write("<p style='font-size:15px;color:white'>Developed an automated Occupational Healthcare Management System for JSW Steel, addressing manual data management challenges, minimizing errors, and improving accessibility. The user-friendly interface enhances productivity, ensuring smooth employee adoption and efficient healthcare management.</p>", unsafe_allow_html=True)

if selected == "Technical Profiles":
    # Change font to Courier New for the heading
    st.write("<p style='font-size:30px;color:#0fdb46;font-weight:bold;font-family:\"Courier New\", monospace'>Technical Profiles</p>", unsafe_allow_html=True)
    # Define the table style with Courier New font
    table_style = """
    <style>
    table {
        font-family: "Courier New", monospace; /* Change font to Courier New */
        border-collapse: collapse;
        width: 70%;
    }
    td, th {
        border: 1px solid #008000;
        text-align: left;
        padding: 8px;
    }
    tr:nth-child(even) {
        background-color:; /* Consider specifying a color here */
    }
    </style>
    """

    # Define the table content with clickable links
    table_content = """
    <table>
        <tr>
            <th>Platform</th>
            <th>Profile</th>
        </tr>
        <tr>
            <td>HackerRank</td>
            <td><a href='https://www.hackerrank.com/profile/sathishduriyan6' target='_blank'>https://www.hackerrank.com/profile/sathishduriyan6</a></td>
        </tr>
        <tr>
            <td>LeetCode</td>
            <td><a href='https://leetcode.com/u/Sathish_Duraiyan/' target='_blank'>https://leetcode.com/u/Sathish_Duraiyan/</a></td>
        </tr>
        <tr>
            <td>GitHub</td>
            <td><a href='https://github.com/SathishDuraiyan' target='_blank'>https://github.com/SathishDuraiyan</a></td>
        </tr>
    </table>
    """

    # Display the table
    st.markdown(table_style, unsafe_allow_html=True)
    st.markdown(table_content, unsafe_allow_html=True)
