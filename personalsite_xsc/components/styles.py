import streamlit as st

def load_css():
    """直接嵌入 CSS 样式，避免文件依赖"""
    st.markdown(
        """
        <style>
        /* 引入 Open Sans 字体 */
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');

        /* 全局样式，设置网页整体背景为#F4F4F4 */
        body {
            font-family: 'Open Sans', sans-serif;
            line-height: 1.8;
            background-color: #F4F4F4;
            color: #000000; /* 字体颜色使用黑色 */
        }
        .st-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        h1, h2, h3 {
            color: #000000; /* 标题颜色使用黑色 */
            margin-bottom: 1rem;
        }
        /* 设置导航菜单背景为#DCD0C0 */
        .stApp > header {
            background-color: #DCD0C0;
        }
        /* 卡片效果增强 */
        .section {
            background: white;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            border-left: 4px solid #C0B283; /* 使用#C0B283作为强调色 */
        }
        .section:hover {
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            transform: translateY(-5px);
        }
        .contact-info {
            margin: 1.5rem 0;
        }
        .experience-item {
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid #e0e0e0;
        }
        .skill-list {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }
        .skill-card {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 4px;
        }
        /* 侧边栏美化 */
        .stSidebar {
            background: #C0B283; /* 使用#C0B283作为侧边栏背景 */
            border-radius: 0 10px 10px 0;
        }
        .stSidebar .stButton > button {
            color: #000000;
        }
        .stSidebar .stRadio > div {
            color: #000000;
        }
        /* 按钮样式优化 */
        .stButton > button {
            background: #C0B283; /* 使用#C0B283作为按钮背景 */
            color: #000000;
            border-radius: 5px;
            border: none;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background: #B0A273; /* 按钮悬停时使用稍深的颜色 */
            transform: scale(1.05);
        }
        /* 响应式布局 */
        @media (max-width: 768px) {
            .skill-list { grid-template-columns: 1fr; }
            .st-sidebar { width: 100% !important; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )