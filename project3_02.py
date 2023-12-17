import os
import streamlit as st
from PIL import Image


# header 부분
image = Image.open('color_project.jpg')
st.image(image)
st.title(':artist: 미술: 색의 3요소와 퍼스널 컬러')
st.subheader("")

# 글자체 특징
path = os.getcwd() + '/NanumGothic.ttf'

# 1번 구역
st.subheader('1. 생각해보기: 색의 차이는?! :thinking_face:', divider='violet')
st.markdown("##### 색의 차이는 무엇 때문에 나타나는지 생각해보자!")
con1,con2, con3 = st.columns([1.0,1.0,1.0])

with con1:
    image = Image.open('red.jpg')
    st.image(image)

with con2:
    image = Image.open('pink.jpg')
    st.image(image)
    
with con3:
    image = Image.open('violet.jpg')
    st.image(image)

con1,con2, con3 = st.columns([1.0,1.0,1.0])

with con1:
    image = Image.open('green.jpg')
    st.image(image)

with con2:
    image = Image.open('blue.jpg')
    st.image(image)


st.divider()

st.subheader('2. 알아보기: 색의 3요소(색상/채도/명도) :clipboard:', divider='violet')
st.markdown("##### 색의 차이를 '색상, 채도, 명도' 색의 3요소로 알아보자!")
image = Image.open('art.png')
st.image(image)
st.divider()

# 2번 구역
st.subheader('3. 해보기: 퍼스널 컬러 컨설턴트 되어보기(퍼스널 컬러 진단) :artist:', divider='violet')
video_file = open('project3.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.markdown('##### **다음 과정에 따라 활동해 봅시다.**')
st.markdown(" 1. 퍼스널 컬러 컨설턴트가 되어 고객(친구)의 이미지에 맞는 색을 찾기 위해 고객(친구)과 이미지에 대해 의견을 나눈다.")
st.markdown(" 2. 드레이프 천을 이용하여 고객(친구)에게 어울리는 색상 및 퍼스널 컬러를 찾아 진단해본다.")
st.markdown(" 3. 고객(친구)의 퍼스널 컬러에 맞는 진단지를 참고할 수 있도록 CANVA(캔바)로 제작한다.")
st.markdown(" 4. 제작한 진단지를 '.jpg' 형식으로 다운 받는다.")
st.markdown(" 5. 고객(친구) 이름과 진단한 퍼스널 컬러 입력한 후 다운 받은 진단서 파일(.jpg)을 업로드해서 공유한다.")

st.divider()

# 파일 구분을 위한 조 이름 입력
customer_name = st.text_input(':busts_in_silhouette: **고객(친구) 이름을 입력해주세요.**')
if customer_name is None or customer_name == '':
    st.warning('고객(친구) 이름을 입력하세요.')
else:
    st.success('고객(친구) 이름 입력 완료')

# 컨텐츠1(색상 입력), 컨텐츠2(jpg 업로드)
con1, con2 = st.columns([0.4,0.6])
with con2: 
    # 파일 저장하는 함수 정의
    def save_uploaded_file(directory, file):
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(os.path.join(directory, file.name),'wb') as f: 
            f.write(file.getbuffer())
        
        return st.success('파일 업로드 성공')

    # jpg 파일 업로드 부분
    jpg_file = st.file_uploader(':file_folder: **CANVA(캔바)로 작업한 진단서 파일(.jpg)을 업로드 하세요.**', type = ['jpg'])

with con1: 
    # 색상 값 입력 부분
    color = st.text_input(':pencil: **진단한 퍼스널 컬러를 입력하세요:**')

    if color is None or color == '':
        st.warning('퍼스널 컬러를 입력하세요.')
    else:
        st.write('**퍼스널 컬러:**', color)
        st.success('퍼스널 컬러 입력 완료')
    
# 제출 버튼
image_folder = os.getcwd() + '/img2'

# 'img' 디렉토리가 존재하는지 확인하고, 없다면 생성합니다.
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# 제출 버튼이 눌렸을 때만 파일 리스트를 가져옵니다.
if st.button('퍼스널 컬러 도감 만들기', use_container_width = True):
    if jpg_file is None:
        st.warning('파일을 업로드하세요.')
    elif customer_name is None or customer_name == '':
        st.warning('고객(친구) 이름을 입력하세요.')
    elif color is None or color == '':
        st.warning('퍼스널 컬러를 입력하세요.')
    else:
        filename = customer_name + '_' + color + '.jpg'  #조 이름과 색상을 파일명에 포함
        jpg_file.name = filename
        save_uploaded_file('img2', jpg_file)

        files = os.listdir(image_folder)
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        my_range = range(len(image_files))

st.divider()

# 3번 구역
st.subheader(':rainbow: 우리반 퍼스널 컬러 도감', divider='violet')
cols = st.columns(1)
image_folder = os.getcwd() + '/img2'
files = os.listdir(image_folder)
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
print(image_files) # 점검용
my_range = range(len(image_files))

# 이미지 출력
for i in my_range:
    image_name_parts = image_files[i].split('.')[0].split('_') # 파일명을 '_' 기준으로 분리
    with cols[i % 1].expander(f"{image_name_parts[0]}" + "-" + f"{image_name_parts[1]}"): 
        st.image('img2' + '/' + image_files[int(i)], caption = image_files[int(i)])


st.divider()
st.markdown("#### :smile: 수고했어요! 나의 이미지 탐색을 끝냈으니 이미지를 스타일로 표현해볼까요?")