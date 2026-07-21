# 数学建模学习平台 - 开发指南

## 项目概述

这是一个跨平台的数学建模学习应用，包含：
- **后端**：Python FastAPI + SQLAlchemy + SQLite
- **前端**：Flutter（iOS/Android）
- **功能**：10大类数学模型学习、进度追踪、收藏管理

---

## 环境要求

### 后端环境
- Python 3.8+
- pip（Python包管理器）

### 前端环境
- Flutter 3.0+
- Dart SDK
- Android Studio / Xcode（用于模拟器）

---

## 快速开始

### 1. 后端启动

#### 安装依赖
```bash
cd backend
pip install -r requirements.txt
```

#### 配置环境变量
复制 `.env.example` 为 `.env`：
```bash
copy .env.example .env  # Windows
```

修改 `.env` 文件中的配置（可选）：
```env
DATABASE_URL=sqlite+aiosqlite:///./math_modeling.db
SECRET_KEY=your-secret-key-change-this
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

#### 初始化数据库
```bash
python init_db.py
```
这会创建数据库表并插入10大分类的初始数据。

#### 启动服务
```bash
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

服务启动后访问：
- API根路径：http://localhost:8000
- Swagger文档：http://localhost:8000/docs
- ReDoc文档：http://localhost:8000/redoc

---

### 2. 前端启动

#### 安装Flutter

**Windows安装步骤**：

1. **下载Flutter SDK**
   - 访问：https://flutter.dev/docs/get-started/install/windows
   - 下载Flutter SDK压缩包

2. **解压并配置环境变量**
   ```bash
   # 解压到：C:\flutter
   # 添加到系统环境变量Path：
   C:\flutter\bin
   ```

3. **验证安装**
   ```bash
   flutter doctor
   ```

4. **安装Android Studio**（可选，用于Android开发）
   - 下载：https://developer.android.com/studio
   - 安装Android SDK和模拟器

#### 运行Flutter项目

**注意**：由于你的系统还未安装Flutter，目前项目结构已创建，但需要先安装Flutter才能运行。

安装Flutter后执行：

```bash
cd frontend

# 获取依赖
flutter pub get

# 运行（连接设备或启动模拟器）
flutter run

# 或指定平台
flutter run -d chrome  # 网页版
flutter run -d windows  # Windows桌面版
```

#### 配置后端地址

修改 `frontend/lib/utils/api_constants.dart` 中的 `baseUrl`：

```dart
static const String baseUrl = 'http://localhost:8000';  // 本地开发
// static const String baseUrl = 'http://10.0.2.2:8000';  // Android模拟器
// static const String baseUrl = 'http://your-server-ip:8000';  // 生产环境
```

---

## 项目结构说明

```
math-modeling-app/
├── backend/                    # Python后端
│   ├── app/
│   │   ├── api/               # API路由
│   │   │   ├── auth.py        # 认证接口
│   │   │   └── models.py      # 模型接口
│   │   ├── core/              # 核心配置
│   │   │   ├── config.py      # 配置管理
│   │   │   ├── database.py    # 数据库连接
│   │   │   └── security.py    # 安全认证
│   │   ├── models/            # 数据模型
│   │   │   └── models.py      # SQLAlchemy模型
│   │   ├── schemas/           # Pydantic模式
│   │   │   ├── user.py        # 用户模式
│   │   │   └── model.py       # 模型模式
│   │   ├── services/          # 业务逻辑
│   │   │   └── init_data.py   # 数据初始化
│   │   └── main.py            # 应用入口
│   ├── requirements.txt       # Python依赖
│   ├── .env.example          # 环境变量示例
│   └── init_db.py            # 数据库初始化脚本
│
├── frontend/                  # Flutter前端
│   ├── lib/
│   │   ├── models/           # 数据模型
│   │   │   ├── user.dart
│   │   │   └── model.dart
│   │   ├── screens/          # 页面
│   │   │   ├── login_screen.dart
│   │   │   └── home_screen.dart
│   │   ├── services/         # API服务
│   │   │   ├── api_service.dart
│   │   │   ├── auth_service.dart
│   │   │   └── model_service.dart
│   │   ├── utils/            # 工具类
│   │   │   └── api_constants.dart
│   │   └── main.dart         # 应用入口
│   └── pubspec.yaml          # Flutter依赖配置
│
├── docs/                     # 文档
│   ├── api.md               # API文档
│   ├── database.md          # 数据库设计
│   └── DEVELOPMENT.md       # 本文件
│
└── README.md                # 项目说明
```

---

## 开发流程

### 1. 测试后端API

使用Swagger文档测试：
1. 访问 http://localhost:8000/docs
2. 注册用户：POST /auth/register
3. 登录获取token：POST /auth/login
4. 使用token测试其他接口

### 2. 前端开发流程

当前已完成：
- ✅ 登录/注册页面
- ✅ 主页10大分类卡片展示
- ✅ 用户认证流程
- ✅ API服务封装

待开发功能：
- [ ] 模型列表页面
- [ ] 模型详情页面（理论、案例、代码、Demo）
- [ ] 学习进度可视化
- [ ] 收藏功能
- [ ] 搜索功能
- [ ] 用户个人中心

### 3. 添加新模型内容

在后端添加模型数据：

```python
# 创建新的数据初始化脚本或直接通过API添加
from app.models.models import Model

new_model = Model(
    category_id=1,
    name="线性规划",
    name_en="Linear Programming",
    description="求解线性目标函数在线性约束条件下的最优解",
    theory_content="理论内容...",
    case_content="案例内容...",
    code_content="代码示例...",
    difficulty_level=2,
    display_order=1
)
```

---

## 调试技巧

### 后端调试
```bash
# 查看详细日志
uvicorn app.main:app --reload --log-level debug

# 使用Python调试器
import pdb; pdb.set_trace()
```

### 前端调试
```bash
# 查看Flutter日志
flutter logs

# 热重载（开发时自动）
# 保存文件即可自动刷新

# 查看设备
flutter devices
```

---

## 常见问题

### Q1: 后端启动失败
**解决**：检查Python版本和依赖是否正确安装
```bash
python --version  # 应该是3.8+
pip list  # 查看已安装的包
```

### Q2: 前端无法连接后端
**解决**：
- 检查后端是否正常运行（访问 http://localhost:8000）
- Android模拟器使用 `10.0.2.2` 替代 `localhost`
- iOS模拟器可以使用 `localhost`
- 检查防火墙设置

### Q3: Flutter未安装
**解决**：
1. 访问 https://flutter.dev/docs/get-started/install
2. 按照Windows安装指南操作
3. 配置环境变量
4. 运行 `flutter doctor` 验证

### Q4: 数据库文件在哪里？
**解决**：SQLite数据库文件位于 `backend/math_modeling.db`

---

## 生产部署

### 后端部署
```bash
# 使用Gunicorn（生产环境）
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker

# 使用PostgreSQL
# 修改.env中的DATABASE_URL
DATABASE_URL=postgresql://user:password@localhost/math_modeling_db
```

### 前端打包
```bash
# Android APK
flutter build apk --release

# iOS IPA（需要Mac）
flutter build ios --release

# Windows桌面版
flutter build windows --release
```

---

## 下一步计划

1. **完善模型内容**：逐步添加10大类下的具体模型
2. **开发详情页面**：展示理论、案例、代码、Demo
3. **添加搜索功能**：按模型名称和关键词搜索
4. **优化UI设计**：提升用户体验
5. **性能优化**：缓存、懒加载等
6. **单元测试**：编写测试用例
7. **部署上线**：发布到应用商店

---

## 技术支持

如有问题，请查阅：
- FastAPI文档：https://fastapi.tiangolo.com/
- Flutter文档：https://flutter.dev/docs
- SQLAlchemy文档：https://docs.sqlalchemy.org/
