import streamlit as st

def skills_page():
    st.header("技能与证书")
    
    # 技能分类展示
    st.markdown("### 专业技能")
    st.markdown("- 办公软件: 熟练使用Office、剪映、Adobe InDesign/Photoshop")
    st.markdown("- 数据分析: Python、R、网络数据抓取、数据可视化（Matplotlib/Seaborn）")
    
    st.markdown("### 语言能力")
    st.markdown("- 英语: 专业八级（优秀）、雅思7.5分（听/说/读/写精通）")
    st.markdown("- 粤语: 流利日常交流")
    st.markdown("- 西班牙语: 基础会话水平")
    
    # 技能卡片布局
    st.markdown("### 能力概览")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**跨文化沟通**")
        st.markdown("- 国际项目申报与学术合作经验")
        st.markdown("- 多语言内容创作（中/英/日纪录片）")
    with col2:
        st.markdown("**项目管理**")
        st.markdown("- 协调跨部门资源（如realme联名项目）")
        st.markdown("- 千人规模活动执行经验（MBA毕业典礼）")