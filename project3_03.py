import os
import streamlit as st
from PIL import Image


# header 부분
image = Image.open('color_project.jpg')
st.image(image)
st.title(':traffic_light: 빛의 합성과 퍼스널 컬러')
st.subheader("")

# 글자체 특징
path = os.getcwd() + '/NanumGothic.ttf'

# 1번 구역
st.subheader('1. 빛의 합성 탐구 과정 안내 :clipboard:', divider='violet')
st.markdown('##### :smile: **다음 과정에 따라 탐구해 봅시다.**')
st.markdown(" 1. 2번 탐구에서 활동 조를 선택하여, 클릭한 후 사진 속 색을 스마트 현미경으로 관찰한 후 캡처한다.")
st.markdown(" 2. 활동 조의 색에 맞춰 red/green/blue의 슬라이더를 움직이고 색을 맞췄을 때 rgb 값이 함께 나오도록 화면을 캡처한다.")
st.markdown(" 3. 실험 결과를 CANVA(캔바)를 활용하여 정리한다.")
st.markdown(" 4. CANVA(캔바)로 정리한 실험 결과를 '.jpg' 형태로 다운 받는다.")
st.markdown(" 5. 조 이름과 분석한 색상을 입력한 후 다운 받은 실험 결과 파일(.jpg)을 업로드 한다.")
st.markdown(" 6. 다른 조들과 실험 결과를 공유하며 아래(3번) 탐구 결과를 분석한다.")

st.divider()

# 2번 구역
st.subheader('2. 빛의 합성으로 보는 웜톤 VS 쿨톤', divider='violet')

# 조 목록
group_list = ['1조(초록)', '2조(보라)', '3조(빨강)', '4조(분홍)']

# 각 조에 대한 이미지 디렉토리
image_dir = 'images'

cols = st.columns(2)
for i, group in enumerate(group_list):
    with cols[i % 2].expander(group):
        # 해당 조의 이미지 파일 경로
        image_path = os.path.join(image_dir, f'{group}.png')

        # 이미지 파일이 존재하는 경우 이미지를 표시
        if os.path.isfile(image_path):
            st.image(image_path)
        else:
            st.write(f'{group}의 이미지가 없습니다.')



con1, con2, con3 = st.columns([0.6, 0.1, 0.3])
with con1:
    def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb

    r = st.slider('Red', min_value=0, max_value=255, value=0)
    g = st.slider('Green', min_value=0, max_value=255, value=0)
    b = st.slider('Blue', min_value=0, max_value=255, value=0)

    col = rgb_to_hex((r,g,b))

    st.markdown(f'RGB({r},{g},{b})')
    st.markdown(f'색상: {col}') 
    

with con3:
    st.image(Image.new('RGB', (250, 300), col)) 
    

st.divider()

# 파일 구분을 위한 조 이름 입력
group_name = st.text_input(':busts_in_silhouette: **조 이름을 입력해주세요.**')
if group_name is None or group_name == '':
    st.warning('조 이름을 입력하세요.')
else:
    st.success('조 이름 입력 완료')

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
    jpg_file = st.file_uploader(':file_folder: **CANVA(캔바)로 작업한 파일(.jpg)을 업로드 하세요.**', type = ['jpg'])

with con1: 
    # 색상 값 입력 부분
    color = st.text_input(':pencil: **실험에서 분석한 색상을 입력하세요:**')

    if color is None or color == '':
        st.warning('색상을 입력하세요.')
    else:
        st.write('**실험 색상:**', color)
        st.success('색상 입력 완료')
    
# 제출 버튼
image_folder = os.getcwd() + '/img'

# 'img' 디렉토리가 존재하는지 확인하고, 없다면 생성합니다.
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# 제출 버튼이 눌렸을 때만 파일 리스트를 가져옵니다.
if st.button('탐구 결과 보고', use_container_width = True):
    if jpg_file is None:
        st.warning('파일을 업로드하세요.')
    elif group_name is None or group_name == '':
        st.warning('조 이름을 입력하세요.')
    elif color is None or color == '':
        st.warning('색상을 입력하세요.')
    else:
        filename = group_name + '_' + color + '.jpg'  #조 이름과 색상을 파일명에 포함
        jpg_file.name = filename
        save_uploaded_file('img', jpg_file)

        files = os.listdir(image_folder)
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        my_range = range(len(image_files))

st.divider()

# 3번 구역: 실험 결과 도감
st.subheader(':rainbow-flag: 우리반 탐구 결과 모음', divider='violet')
cols = st.columns(1)
image_folder = os.getcwd() + '/img'
files = os.listdir(image_folder)
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
print(image_files) # 점검용
my_range = range(len(image_files))

# 이미지 출력
for i in my_range:
    image_name_parts = image_files[i].split('.')[0].split('_') # 파일명을 '_' 기준으로 분리
    with cols[i % 1].expander(f"{image_name_parts[0]}" + "-" + f"{image_name_parts[1]}"): 
        st.image('img' + '/' + image_files[int(i)], caption = image_files[int(i)])


st.divider()

# 4번 구역: 탐구 정리
st.subheader('3. 보고서: 실험 결과 해석하기 :bookmark_tabs:', divider='violet')

with st.form(key='my_form1'):
    st.markdown('**1. 웜톤 색상들의 rgb 결과를 보면 일반적으로 쿨톤에 비해 r(빨강), g(초록), b(파랑) 중 어느 요소(들)가 많이 포함되어 있나요? (색상 별로 r, g, b의 비율을 계산해서 비교해보세요!)**')
    question1 = st.multiselect(
        "",
        ["r(빨강)", "g(초록)", "b(파랑)"]
    )
    answer1 = st.form_submit_button("정답 제출")

if answer1:
    if set(question1) == set(["r(빨강)", "g(초록)"]):
        st.write("정답입니다! :clap:")
    else:
        st.write("실험 결과를 보고 다시 풀어보세요. :sweat_smile:")

with st.form(key='my_form2'):
    st.markdown('**2. 쿨톤 색상들의 rgb 결과를 보면 일반적으로 쿨톤에 비해 r(빨강), g(초록), b(파랑) 중 어느 요소(들)가 많이 포함되어 있나요? (색상 별로 r, g, b의 비율을 계산해서 비교해보세요!)**')
    question2 = st.multiselect(
        "",
        ["r(빨강)", "g(초록)", "b(파랑)"]
    )
    answer2 = st.form_submit_button("정답 제출")

if answer2:
    if set(question2) == set(["b(파랑)"]):
        st.write("정답입니다! :clap:")
    else:
        st.write("실험 결과를 보고 다시 풀어보세요. :sweat_smile:")

with st.form(key='my_form3'):
    st.markdown('**3. 보고서: 실험 결과 한줄로 정리하기** :pencil:')
    student_result = st.text_input("**위의 문제의 답을 참고해서 웜톤과 쿨톤의 차이를 한줄로 정리해보세요!** :blush:")

    if st.form_submit_button('한줄 보고서 제출'):
        st.write(f"**'{student_result}'** 라고 정리했군요! 수고했어요 :clap:")

st.divider()

# 5번 구역
st.subheader('4. 더 생각해보기: 봄 웜톤 VS 가을 웜톤?! 여름 쿨톤 VS 겨울 쿨톤?! :upside_down_face:', divider='violet')
st.markdown('**웜톤과 쿨톤은 봄 웜/여름 쿨/가을 웜/겨울 쿨톤, 계절로 세분화 되는데 계절 별 차이의 이유를 생각해보자!**')

con1, con2, con3 = st.columns([0.9, 1.0, 1.0])
with con1:
    image = Image.open('personalcolor.png')
    st.image(image)

with con2:
    image = Image.open('red.png')
    st.image(image)

with con3:
    image = Image.open('yellow.png')
    st.image(image)


con1, con2, con3 = st.columns([0.6, 0.1, 0.3])
with con1:
    def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb

    r = st.slider('Red', min_value=0, max_value=255, value=0, key='slider1')
    g = st.slider('Green', min_value=0, max_value=255, value=0, key='slider2')
    b = st.slider('Blue', min_value=0, max_value=255, value=0, key='slider3')

    col = rgb_to_hex((r,g,b))

    st.markdown(f'RGB({r},{g},{b})')
    st.markdown(f'색상: {col}') 

with con3:
    st.image(Image.new('RGB', (250, 300), col))


with st.form(key='my_form4'):
    st.markdown('**봄 웜톤/가을 웜톤 계절에 따른 색의 차이는 색상/채도/명도 중 무엇(들) 때문인가요? (슬라이더를 움직이며 확인해보세요)**')
    question4 = st.multiselect(
        "",
        ["색상", "채도", "명도"]
    )
    answer4 = st.form_submit_button("정답 제출")

if answer4:
    if set(question4) == set(["채도", "명도"]):
        st.write("정답입니다! :clap:")
    else:
        st.write("다시 슬라이더를 움직여보면서 풀어보세요. :sweat_smile:")

st.divider()
st.markdown("#### :smile: 수고했어요! 색에 대한 개념을 바탕으로 퍼스널 컬러:art:를 진단해볼까요?")
