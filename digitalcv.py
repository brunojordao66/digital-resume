from pathlib import Path

import streamlit as st
from PIL import Image

##current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
##css_file =  current_dir / "styles" / "main.css"
##resume_file = current_dir / "assets" / "resumee en.pdf"
##profile_pic = current_dir / "assets" / 'profilepic.PNG'


## informaçoes gerais

page_title = 'Digital CV | Bruno Jordão da Silva'
page_icon = ':wave:'
name = 'Bruno Jordão'
personal_info = 'Brazilian, 22y'
Description = 'data analyst and solution architect | assisting enterprises by supporting data-driven decision-making and developing solutions with python and power platform'
email = 'bruno.jordao8@gmail.com'
social_media = {
    'LinkedIn': 'https://www.linkedin.com/in/jord%C3%A3o/',
    'GitHub': 'https://github.com/brunojordao66',
    'Medium': 'https://medium.com/@bruno.jordao8'

}

## hard skills
Python = 30
powerbi = 90
excel = 100
sql = 40
aws = 20
agile = 50

## linguagens

ingles = 90
portugues = 100
espanhol = 20

st.set_page_config(page_title= page_title, page_icon= page_icon)

## subir CSS e assets

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,'rb') as pdf_file:
    PDFbyte = pdf_file.read()
##profile_pic = Image.open(profile_pic)

## formatando apresentação

col1, col2 = st.columns(2, gap='small')
with col1:
    ##st.image(profile_pic, width=250)
with col2:
    st.title(name)
    st.subheader(personal_info)
    st.write(Description)
    st.download_button(
        label=' Download Resume',
        data= PDFbyte,
        file_name= resume_file.name,
        mime='application/octet-stream'
    )
    st.write("✉️", email)

## formatando os redirecionamentos

cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f'[{platform}]({link})')

## formatando experiências e qualificações
st.write('#')
st.subheader('Hard skills')

col1, col2, col3 = st.columns(3, gap='medium')

with col1:
    st.progress(Python, '🐍 Python')
    st.progress(powerbi, '📊Power Bi')

with col2:
    st.progress(excel, '📈Excel')
    st.progress(sql, '< \ > SQL')
with col3:
    st.progress(aws,'☁️AWS')
    st.progress(agile, '🏃🏽 Agile methodologies')

st.subheader('Languages')
st.progress(ingles, 'English')
st.progress(portugues, 'Brazilian portuguese')
st.progress(espanhol, 'Spanish')

st.subheader('Education')
st.write('Centro Universitário Fundação Santo André')
st.write("Bachelor's Degree in Data Science and Artificial Intelligence - Feb. 2028")


st.write('#')
st.subheader('Experience & qualifications')
col1, col2 = st.columns(2, gap='large')
with col1:
    st.subheader('OVERHAUL - Planning and process assistant')
st.write(   
        '''
- Implementation of performance dashboards through data analysis and case studies.
- Implementation of shared internal systems, automations, and process optimizations using Power 
Platform (Power Apps, Power Automate, SharePoint, and Power BI).
- Process analysis, identification of improvement points, and implementation of solutions utilizing 
Power Platform.
- Development of an internal inventory control system for trackable devices in Power Apps, 
implemented in global fulfillment operations resulting in reduced device loss and cost savings.
- Automation of billing for registration research and victimology consultation in python Streamlit + 
Pandas, resulting in the automated delivery of demand for validation, ensuring punctuality and 
operational improvement.
- Case studies on risk management in road transport, leading to the identification of issues and 
preventive decision-making for continuous improvement of vehicle monitoring and telemetry 
processes.
- Development of structured reports automatically translated into English from internal systems, 
resulting in enhanced effectiveness during result presentations.


    ''')

with col2:
    st.subheader('São Paulo | Jun. 2023 – Present')

col1, col2 = st.columns(2, gap='large')


with col1:
    st.subheader('OVERHAUL - Watch officer')
st.write(
    '''
- Responsible for monitoring road freight transport operations through tracking technologies.
- Responsible for contacting clients, carriers, and drivers via email and phone.
- Experience with vehicle telemetry systems such as Onixsat, Autotrack, Sascar, Sighra, Omnilink, 
and Trafegus.
- Monitoring of tracking devices including Golden Sat, SG Tracks, and Positron.
- General control of bases and monitoring operations for a wide range of products and clients
'''
)

with col2:
    st.subheader('São Paulo | Jun. 2022 –Jun. 2023')




