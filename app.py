import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Apple Music Vinyl Turntable",
    page_icon="💿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def load_html_player():
    html_path = os.path.join("htmls", "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        return html_content
    else:
        return None

def main():
    # 전체화면 레이아웃에 맞게 Streamlit 기본 여백 및 패딩 최소화 스타일 적용
    st.markdown("""
        <style>
            .stApp {
                background-color: #08080a;
            }
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding: 0 !important;
                max-width: 100% !important;
            }
        </style>
    """, unsafe_allow_html=True)

    html_code = load_html_player()
    
    if html_code:
        # 컴포넌트 높이를 넉넉히 주어 스크롤바 없이 쾌적하게 렌더링 (반응형 대응)
        components.html(html_code, height=880, scrolling=True)
    else:
        st.error("🚨 `htmls/index.html` 파일을 찾을 수 없습니다. 경로와 파일 이름을 다시 확인해주세요.")
        st.info("💡 깃허브 저장소 루트에 `htmls` 폴더를 만들고 그 안에 `index.html`이 올바르게 위치해 있는지 확인하세요.")

if __name__ == "__main__":
    main()
