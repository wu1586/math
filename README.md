# 数学建模全量学习平台

一个跨平台的数学建模学习应用，支持iOS/Android移动端，提供10大类数学建模模型的系统学习。

## 项目结构

```
math-modeling-app/
├── backend/              # Python FastAPI 后端
│   ├── app/
│   │   ├── api/         # API路由
│   │   ├── models/      # 数据库模型
│   │   ├── schemas/     # Pydantic数据模式
│   │   ├── services/    # 业务逻辑
│   │   ├── core/        # 核心配置（JWT、数据库等）
│   │   └── main.py      # FastAPI应用入口
│   ├── requirements.txt
│   └── .env.example
├── frontend/            # Flutter前端应用
│   ├── lib/
│   │   ├── models/      # 数据模型
│   │   ├── screens/     # 页面
│   │   ├── widgets/     # 自定义组件
│   │   ├── services/    # API服务
│   │   └── main.dart    # 应用入口
│   └── pubspec.yaml
└── docs/                # 文档
    ├── api.md           # API文档
    └── database.md      # 数据库设计文档
```

## 技术栈

### 后端
- **框架**: FastAPI 0.115+
- **数据库**: SQLite (开发) / PostgreSQL (生产)
- **ORM**: SQLAlchemy 2.0+
- **认证**: JWT Token
- **数据验证**: Pydantic

### 前端
- **框架**: Flutter 3.24+
- **状态管理**: Provider / Riverpod
- **HTTP客户端**: Dio
- **本地存储**: SharedPreferences / Hive

## 核心功能

### 1. 用户系统
- 注册/登录/登出
- JWT Token认证
- 用户信息管理

### 2. 10大模型分类
1. 数学规划（线性规划、整数规划、非线性规划、动态规划）
2. 综合评价与决策（AHP、TOPSIS、DEA）
3. 预测类模型（回归、时间序列、机器学习预测）
4. 概率统计与数据分析（聚类、降维、假设检验）
5. 微分方程与系统动力学（ODE、PDE、传染病模型）
6. 图论与网络优化（最短路径、网络流、TSP）
7. 智能优化算法（遗传算法、粒子群、模拟退火）
8. 机器学习与数据挖掘（监督学习、深度学习）
9. 运筹学经典模型（排队论、存贮论、博弈论）
10. 其他专项模型（元胞自动机、贝叶斯网络）

### 3. 学习内容展示
- 理论知识讲解
- 实际案例分析
- 交互式Demo演示
- 完整代码展示（Python/MATLAB）

### 4. 学习进度追踪
- 学习记录保存
- 进度可视化
- 收藏功能

## 快速开始

### 后端启动
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 前端启动
```bash
cd frontend
flutter pub get
flutter run
```

## 开发计划

- [x] 项目初始化
- [ ] 数据库设计
- [ ] 后端API开发
- [ ] 前端UI框架搭建
- [ ] 用户认证实现
- [ ] 内容管理系统
- [ ] 学习进度追踪
- [ ] 各模型内容填充

## 许可证

MIT License
