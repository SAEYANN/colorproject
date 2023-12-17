import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.set_page_config(layout="wide")
# header 부분
image = Image.open('color_project.jpg')
st.image(image)
st.title(":rainbow: PROJECT NAME: Personal Color Project")
st.header(' ')
st.subheader(':laughing: 재미로 알아보는 퍼스널 컬러', divider='violet')

con1,con2 = st.columns([1.0,1.0])

# YouTube Shorts 링크
shorts_link = 'https://www.youtube.com/shorts/rIMasPs_IY4'  # 'YOUR_VIDEO_ID' 부분을 실제 비디오 ID로 변경해주세요.
# YouTube 링크에서 ID 추출
video_id = shorts_link.split('/')[-1]
# 원하는 비디오의 가로, 세로 크기 설정
width = 360  
height = 480
# YouTube Shorts 비디오 재생
with con1:
    st.markdown(
        f'<iframe width="{width}" height="{height}" src="https://www.youtube.com/embed/{video_id}" '
        'frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" '
        'allowfullscreen></iframe>',
        unsafe_allow_html=True,
    )

con2.subheader("내가 곽윤기라면 LEFT or RIGHT?!", divider = 'grey')
with con2:
    image = Image.open('personal01.png')
    st.image(image)
st.divider()

st.subheader(':thinking_face: 무조건 유행을 따라하다 보면?', divider='violet')

image = Image.open('page01.png')
st.image(image)

st.markdown('')
st.markdown('###### 나의 이미지에 맞는다면 괜찮지만 나에게 맞지 않는 유행은 오히려 이미지에 마이너스 요소가 된다.')
st.markdown('###### 나에게 맞는 나만의 스타일을 표현하기 위해서는 나에 대해 먼저 알아야 한다!')
st.divider()

st.subheader(':art: 나를 표현할 때 참고하세요!: 퍼스널 컬러', divider='violet')
con1,con2, con3 = st.columns([1.5,0.1,1.0])

with con1:
    st.markdown('#### **무슨 색인가요?**')
    image = Image.open('lip.jpg')
    st.image(image)
    
with con3:
    image = Image.open('red.jpg')
    st.image(image)

st.markdown('')
st.markdown('###### 빨강이지만 다 같은 색이 아니다! 나의 이미지에 맞지 않는 색이 있는 반면 나의 이미지를 살리는 색이 있다.')
st.markdown('###### 나에게 가장 잘 어울리는 색을 찾아 단점은 보완하고 장점을 극대화시켜 긍정적이고, 자신감 있는 이미지를 연출하자는 이론이')
st.markdown('##### 퍼스널컬러이다!')

st.divider()

st.markdown("### :rainbow-flag: 퍼스널 컬러를 통해 나의 이미지를 알아보자! :heavy_check_mark:")



# 페이지 묶기
show_pages(
    [
        Page("project3_01.py", "퍼스널 컬러?!", ":rainbow:"),
        Page("project3_02.py", "미술: 색상의 3요소와 퍼스널 컬러", ":lower_left_paintbrush:"),
        Page("project3_03.py", "과학: 빛의 합성과 퍼스널 컬러", ":lower_left_crayon:"),
        Page("project3_04.py", "가정: 나만의 스타일 표현하기", ":coat:"),
    ]
)