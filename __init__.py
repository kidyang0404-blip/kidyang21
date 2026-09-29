# pybo/__init__.py 내부 예시
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM 초기화
    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린트 임포트 및 등록
    from .views import main_views, question_views, answer_views
    
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)  # <-- 추가

    return app