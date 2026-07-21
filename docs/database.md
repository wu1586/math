# 数据库设计文档

## 概述
数学建模学习平台使用SQLite（开发环境）/PostgreSQL（生产环境）作为数据库，使用SQLAlchemy ORM进行数据访问。

## 数据表结构

### 1. users（用户表）
存储用户账号信息。

| 字段 | 类型 | 说明 | 约束 |
|------|------|------|------|
| id | Integer | 用户ID | 主键，自增 |
| username | String(50) | 用户名 | 唯一，非空，索引 |
| email | String(100) | 邮箱 | 唯一，非空，索引 |
| hashed_password | String(255) | 密码哈希 | 非空 |
| is_active | Boolean | 是否激活 | 默认True |
| created_at | DateTime | 创建时间 | 自动生成 |
| updated_at | DateTime | 更新时间 | 自动更新 |

**关系**：
- 一对多：learning_progress（学习进度）
- 一对多：favorites（收藏）

### 2. categories（分类表）
存储10大模型分类信息。

| 字段 | 类型 | 说明 | 约束 |
|------|------|------|------|
| id | Integer | 分类ID | 主键，自增 |
| name | String(100) | 分类名称（中文） | 非空 |
| name_en | Enum | 分类名称（英文枚举） | 唯一，非空 |
| description | Text | 分类描述 | 可空 |
| icon | String(50) | 图标名称 | 可空 |
| display_order | Integer | 显示顺序 | 默认0 |
| created_at | DateTime | 创建时间 | 自动生成 |

**分类枚举值**：
- mathematical_programming：数学规划
- evaluation_decision：综合评价与决策
- prediction：预测类模型
- statistics：概率统计与数据分析
- differential_equations：微分方程与系统动力学
- graph_theory：图论与网络优化
- intelligent_optimization：智能优化算法
- machine_learning：机器学习与数据挖掘
- operations_research：运筹学经典模型
- other_models：其他专项模型

**关系**：
- 一对多：models（数学模型）

### 3. models（数学模型表）
存储各个具体的数学模型内容。

| 字段 | 类型 | 说明 | 约束 |
|------|------|------|------|
| id | Integer | 模型ID | 主键，自增 |
| category_id | Integer | 所属分类ID | 外键，非空 |
| name | String(100) | 模型名称 | 非空 |
| name_en | String(100) | 模型英文名 | 可空 |
| description | Text | 模型简介 | 可空 |
| theory_content | Text | 理论知识内容 | 可空 |
| case_content | Text | 案例分析内容 | 可空 |
| code_content | Text | 代码示例 | 可空 |
| demo_url | String(255) | 交互Demo链接 | 可空 |
| difficulty_level | Integer | 难度等级（1-5） | 默认1 |
| display_order | Integer | 显示顺序 | 默认0 |
| created_at | DateTime | 创建时间 | 自动生成 |
| updated_at | DateTime | 更新时间 | 自动更新 |

**关系**：
- 多对一：category（所属分类）
- 一对多：learning_progress（学习进度）
- 一对多：favorites（收藏）

### 4. learning_progress（学习进度表）
记录用户对每个模型的学习进度。

| 字段 | 类型 | 说明 | 约束 |
|------|------|------|------|
| id | Integer | 进度ID | 主键，自增 |
| user_id | Integer | 用户ID | 外键，非空 |
| model_id | Integer | 模型ID | 外键，非空 |
| is_completed | Boolean | 是否完成 | 默认False |
| progress_percentage | Integer | 进度百分比（0-100） | 默认0 |
| last_studied_at | DateTime | 最后学习时间 | 自动生成 |
| created_at | DateTime | 创建时间 | 自动生成 |

**关系**：
- 多对一：user（用户）
- 多对一：model（模型）

**复合唯一约束**：(user_id, model_id)

### 5. favorites（收藏表）
记录用户收藏的模型。

| 字段 | 类型 | 说明 | 约束 |
|------|------|------|------|
| id | Integer | 收藏ID | 主键，自增 |
| user_id | Integer | 用户ID | 外键，非空 |
| model_id | Integer | 模型ID | 外键，非空 |
| created_at | DateTime | 创建时间 | 自动生成 |

**关系**：
- 多对一：user（用户）
- 多对一：model（模型）

**复合唯一约束**：(user_id, model_id)

## ER图关系

```
users (1) ----< (N) learning_progress (N) >---- (1) models
users (1) ----< (N) favorites (N) >---- (1) models
categories (1) ----< (N) models
```

## 索引策略

### 主要索引
- users: username, email（唯一索引）
- categories: name_en（唯一索引）
- learning_progress: (user_id, model_id)组合索引
- favorites: (user_id, model_id)组合索引

### 查询优化
- 按分类查询模型：category_id索引
- 用户学习记录查询：user_id索引
- 最近学习时间排序：last_studied_at索引

## 初始数据

### categories表初始数据
系统启动时会自动插入10大分类的基础数据，包括：
- 分类名称（中英文）
- 描述信息
- 图标标识
- 显示顺序

运行命令：`python backend/init_db.py`

## 数据迁移

使用Alembic进行数据库版本管理：

```bash
# 初始化迁移
alembic init alembic

# 生成迁移脚本
alembic revision --autogenerate -m "Initial migration"

# 执行迁移
alembic upgrade head
```

## 数据完整性

### 外键约束
- learning_progress.user_id → users.id
- learning_progress.model_id → models.id
- favorites.user_id → users.id
- favorites.model_id → models.id
- models.category_id → categories.id

### 级联操作
- 删除用户时：级联删除其学习进度和收藏记录
- 删除模型时：级联删除相关的学习进度和收藏记录
- 删除分类时：限制删除（需先删除或转移该分类下的模型）
