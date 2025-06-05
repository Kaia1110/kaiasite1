import streamlit as st
from components.styles import load_css
from components.footer import display_footer
from page_content.home import home_page
from page_content.education import education_page
from page_content.experience import experience_page
from page_content.projects import projects_page
from page_content.skills import skills_page

# 配置页面
st.set_page_config(
    page_title="许世晨个人简历",
    layout="wide",
    page_icon="📄",
    initial_sidebar_state="expanded"
)

# 初始化多页面应用
class MultiApp:
    def __init__(self):
        self.apps = []
        
    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})
        
    def run(self):
        load_css()  # 加载样式
        st.sidebar.title("导航菜单")
        
        # 侧边栏导航
        selection = st.sidebar.radio(
            "请选择页面",
            self.apps,
            format_func=lambda app: app["title"],
            key="page_nav"
        )
        
        # 渲染选中页面
        selection["function"]()
        display_footer()  # 显示页脚

# 创建应用实例并添加页面
app = MultiApp()
app.add_app("主页", home_page)
app.add_app("教育背景", education_page)
app.add_app("实习经历", experience_page)
app.add_app("项目经历", projects_page)
app.add_app("技能与证书", skills_page)

# 运行应用
if __name__ == "__main__":
    app.run()