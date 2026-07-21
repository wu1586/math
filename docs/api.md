# API 接口文档

## 基础信息

- **Base URL**: `http://localhost:8000`
- **认证方式**: JWT Bearer Token
- **Content-Type**: `application/json`

## 认证接口

### 1. 用户注册
**POST** `/auth/register`

**请求体**:
```json
{
  "username": "string",
  "email": "user@example.com",
  "password": "string"
}
```

**响应** (201 Created):
```json
{
  "id": 1,
  "username": "string",
  "email": "user@example.com",
  "is_active": true,
  "created_at": "2026-07-21T08:00:00Z"
}
```

**错误响应**:
- 400: 用户名或邮箱已存在

---

### 2. 用户登录
**POST** `/auth/login`

**请求体**:
```json
{
  "username": "string",
  "password": "string"
}
```

**响应** (200 OK):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**错误响应**:
- 401: 用户名或密码错误
- 400: 账户已被禁用

---

### 3. 获取当前用户信息
**GET** `/auth/me`

**请求头**:
```
Authorization: Bearer {access_token}
```

**响应** (200 OK):
```json
{
  "id": 1,
  "username": "string",
  "email": "user@example.com",
  "is_active": true,
  "created_at": "2026-07-21T08:00:00Z"
}
```

**错误响应**:
- 401: 未授权或token无效

---

## 模型分类接口

### 4. 获取所有分类
**GET** `/models/categories`

**响应** (200 OK):
```json
[
  {
    "id": 1,
    "name": "数学规划",
    "name_en": "mathematical_programming",
    "description": "线性规划、整数规划、非线性规划、动态规划等优化问题求解方法",
    "icon": "calculator",
    "display_order": 1,
    "created_at": "2026-07-21T08:00:00Z"
  },
  {
    "id": 2,
    "name": "综合评价与决策",
    "name_en": "evaluation_decision",
    "description": "AHP层次分析法、TOPSIS、DEA数据包络分析等多指标评价方法",
    "icon": "assessment",
    "display_order": 2,
    "created_at": "2026-07-21T08:00:00Z"
  }
]
```

---

### 5. 获取分类下的模型列表
**GET** `/models/categories/{category_id}/models`

**路径参数**:
- `category_id`: 分类ID

**响应** (200 OK):
```json
[
  {
    "id": 1,
    "name": "线性规划",
    "description": "求解线性目标函数在线性约束条件下的最优解",
    "difficulty_level": 2,
    "category_id": 1
  }
]
```

**错误响应**:
- 404: 分类不存在

---

## 模型详情接口

### 6. 获取模型详情
**GET** `/models/{model_id}`

**路径参数**:
- `model_id`: 模型ID

**响应** (200 OK):
```json
{
  "id": 1,
  "category_id": 1,
  "name": "线性规划",
  "name_en": "Linear Programming",
  "description": "求解线性目标函数在线性约束条件下的最优解",
  "theory_content": "理论知识内容...",
  "case_content": "案例分析内容...",
  "code_content": "代码示例...",
  "demo_url": "https://example.com/demo",
  "difficulty_level": 2,
  "display_order": 1,
  "created_at": "2026-07-21T08:00:00Z",
  "updated_at": "2026-07-21T08:00:00Z"
}
```

**错误响应**:
- 404: 模型不存在

---

## 学习进度接口

### 7. 更新学习进度
**POST** `/models/progress`

**请求头**:
```
Authorization: Bearer {access_token}
```

**请求体**:
```json
{
  "model_id": 1,
  "progress_percentage": 50,
  "is_completed": false
}
```

**响应** (200 OK):
```json
{
  "id": 1,
  "user_id": 1,
  "model_id": 1,
  "is_completed": false,
  "progress_percentage": 50,
  "last_studied_at": "2026-07-21T08:00:00Z",
  "created_at": "2026-07-21T08:00:00Z"
}
```

**错误响应**:
- 401: 未授权
- 404: 模型不存在

---

### 8. 获取我的学习进度
**GET** `/models/progress/my`

**请求头**:
```
Authorization: Bearer {access_token}
```

**响应** (200 OK):
```json
[
  {
    "id": 1,
    "user_id": 1,
    "model_id": 1,
    "is_completed": false,
    "progress_percentage": 50,
    "last_studied_at": "2026-07-21T08:00:00Z",
    "created_at": "2026-07-21T08:00:00Z"
  }
]
```

**错误响应**:
- 401: 未授权

---

## 收藏接口

### 9. 添加收藏
**POST** `/models/favorites/{model_id}`

**请求头**:
```
Authorization: Bearer {access_token}
```

**路径参数**:
- `model_id`: 模型ID

**响应** (201 Created):
```json
{
  "message": "收藏成功"
}
```

**错误响应**:
- 401: 未授权
- 404: 模型不存在
- 400: 已收藏该模型

---

### 10. 取消收藏
**DELETE** `/models/favorites/{model_id}`

**请求头**:
```
Authorization: Bearer {access_token}
```

**路径参数**:
- `model_id`: 模型ID

**响应** (204 No Content)

**错误响应**:
- 401: 未授权
- 404: 收藏记录不存在

---

## 通用响应

### 根路径
**GET** `/`

**响应**:
```json
{
  "message": "数学建模学习平台API",
  "version": "1.0.0",
  "docs": "/docs"
}
```

### 健康检查
**GET** `/health`

**响应**:
```json
{
  "status": "healthy"
}
```

---

## 错误码说明

| 状态码 | 说明 |
|--------|------|
| 200 | 请求成功 |
| 201 | 创建成功 |
| 204 | 删除成功（无内容返回） |
| 400 | 请求参数错误 |
| 401 | 未授权或token无效 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

---

## 使用示例

### Python示例
```python
import requests

# 登录
response = requests.post('http://localhost:8000/auth/login', json={
    'username': 'testuser',
    'password': 'password123'
})
token = response.json()['access_token']

# 获取分类
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('http://localhost:8000/models/categories', headers=headers)
categories = response.json()
```

### JavaScript示例
```javascript
// 登录
const loginResponse = await fetch('http://localhost:8000/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username: 'testuser', password: 'password123' })
});
const { access_token } = await loginResponse.json();

// 获取分类
const categoriesResponse = await fetch('http://localhost:8000/models/categories', {
    headers: { 'Authorization': `Bearer ${access_token}` }
});
const categories = await categoriesResponse.json();
```

---

## 在线API文档

启动后端服务后，可以访问：
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
