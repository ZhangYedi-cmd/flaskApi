from web.views.index import route_index
from web.views.static import static_route
from application import app

# 注册蓝图
app.register_blueprint(route_index)
app.register_blueprint(static_route)
