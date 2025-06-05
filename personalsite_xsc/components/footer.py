import streamlit as st

def display_footer():
    """显示统一页脚"""
    st.markdown(
        """
        <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e0e0e0; text-align: center;">
            © 2025 许世晨 | 简历最后更新：2025年06月<br>
            联系邮箱：<a href="mailto:xushichen2024@163.com">xushichen2024@163.com</a>
        </div>
        """,
        unsafe_allow_html=True
    )