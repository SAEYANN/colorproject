import os
import streamlit as st
from PIL import Image


# header 부분
image = Image.open('color_project.jpg')
st.image(image)
st.title(':coat: 퍼스널 컬러를 통한 나를 표현하기')
st.subheader("")

# 글자체 특징
path = os.getcwd() + '/NanumGothic.ttf'

# 1번 구역
st.subheader('1. 알아보기: 스타일북?! :open_book:', divider='violet')
st.markdown('##### ※ 스타일북: 시간, 장소, 상황에 맞게 내가 표현하고자 하는 이미지를 보여줄 수 있는 코디를 제시한 것')

con1,con2, con3 = st.columns([2.0,1.1,1.1])

with con1:
    image = Image.open('codibook1.jpg')
    st.image(image)

with con2:
    image = Image.open('codibook2.jpg')
    st.image(image)

with con3:
    image = Image.open('codibook3.jpg')
    st.image(image)

st.divider()

# 2번 구역
st.subheader('2. 해보기: 나만의 스타일북 만들기 :lower_left_paintbrush:', divider='violet')
st.markdown('##### **다음 과정에 따라 활동해 봅시다.**')
st.markdown(" 1. 출석 번호의 끝자리에 맞는 상황(T.P.O) 및 번호를 확인한다.")
st.markdown(" 2. 주어진 상황에 따라 본인이 표현하고자 하는 이미지를 보여줄 수 있는 코디를 생각해본다.")
st.markdown(" **: 퍼스널 컬러(도감 참고) 뿐만 아니라 얼굴형, 체형, 피해야할 색 등 요소들을 고려** ")
st.markdown(" 3. CANVA(캔바)를 이용해서 표현하고자 한 이미지(장점), 고려한 요소 등 설명을 포함하여 스타일북을 제작한다.")
st.markdown(" 4. 제작한 스타일북을 '.jpg' 형식으로 다운 받는다.")
st.markdown(" 5. 상황(T.P.O) 번호와 본인 이름을 입력한 후 다운 받은 스타일북 파일(.jpg)을 업로드해서 공유한다.")

expander = st.expander('출석번호(끝자리)에 맞는 상황(T.P.O) 및 번호 확인')
expander.markdown('**- 상황 1(끝자리 0, 5)** : **11월 오후 1시 실내 지인의 결혼식**\n\n**- 상황 2(끝자리 1, 6) : 4월 초 오후 2시 벗꽃축제**\n\n**- 상황 3(끝자리 2, 7) : 7월 초 오후 5시 야외 파티**\n\n**- 상황 4(끝자리 3, 8) : 10월 오후 단풍축제**\n\n**- 상황 5(끝자리 4, 9) : 5월 학교 수련회 활동**')

st.divider()

# 파일 구분을 위한 조 이름 입력
style_number = st.text_input(':busts_in_silhouette: **상황(T.P.O) 번호를 입력해주세요.**')
if style_number is None or style_number == '':
    st.warning('상황 번호를 입력해주세요')
else:
    st.success('상황 번호 입력 완료')

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
    name = st.text_input(':pencil: **이름을 입력하세요:**')

    if name is None or name == '':
        st.warning('이름을 입력하세요.')
    else:
        st.success('이름 입력 완료')
    
# 제출 버튼
image_folder = os.getcwd() + '/img3'

# 'img' 디렉토리가 존재하는지 확인하고, 없다면 생성합니다.
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# 제출 버튼이 눌렸을 때만 파일 리스트를 가져옵니다.
if st.button('스타일 도감에 업로드', use_container_width = True):
    if jpg_file is None:
        st.warning('파일을 업로드하세요.')
    elif style_number is None or style_number == '':
        st.warning('상황 번호를 입력하세요.')
    elif name is None or name == '':
        st.warning('이름을 입력하세요.')
    else:
        filename = style_number + '_' + name + '.jpg'  #조 이름과 색상을 파일명에 포함
        jpg_file.name = filename
        save_uploaded_file('img3', jpg_file)

        files = os.listdir(image_folder)
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        my_range = range(len(image_files))

st.divider()

# 3번 구역
st.subheader(':dress: 우리반 스타일 도감 :necktie:', divider='violet')
cols = st.columns(2)
image_folder = os.getcwd() + '/img3'
files = os.listdir(image_folder)
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
print(image_files) # 점검용
my_range = range(len(image_files))

# 이미지 출력
for i in my_range:
    image_name_parts = image_files[i].split('.')[0].split('_') # 파일명을 '_' 기준으로 분리
    with cols[i % 2].expander(f"{image_name_parts[0]}" + "-" + f"{image_name_parts[1]}"): 
        st.image('img3' + '/' + image_files[int(i)], caption = image_files[int(i)])


st.divider()
st.markdown("### :grinning: 수고했어요!")
