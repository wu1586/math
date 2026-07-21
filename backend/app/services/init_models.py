"""初始化数学模型数据"""
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import async_engine
from app.models.models import Category, Model, CategoryEnum


# 数学规划模型
MATHEMATICAL_PROGRAMMING_MODELS = [
    {
        "name": "线性规划",
        "name_en": "linear_programming",
        "theory": """
# 线性规划基本理论

线性规划是运筹学中研究较早、发展较快、应用广泛、方法较成熟的一个重要分支。

## 标准形式
目标函数：max z = c₁x₁ + c₂x₂ + ... + cₙxₙ
约束条件：
- a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ ≤ b₁
- a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ ≤ b₂
- 非负约束：xᵢ ≥ 0

## 求解方法
1. 图解法（二维问题）
2. 单纯形法（标准算法）
3. 内点法（大规模问题）
        """,
        "cases": """
# 生产计划问题

某工厂生产A、B两种产品，需要使用三种资源：
- 资源1：A产品需要2单位，B产品需要4单位，总共32单位
- 资源2：A产品需要4单位，B产品需要2单位，总共32单位
- 资源3：A产品需要3单位，B产品需要1单位，总共24单位

A产品利润5元/件，B产品利润4元/件。求最大利润的生产方案。

## 数学模型
max z = 5x₁ + 4x₂
s.t.
- 2x₁ + 4x₂ ≤ 32
- 4x₁ + 2x₂ ≤ 32
- 3x₁ + x₂ ≤ 24
- x₁, x₂ ≥ 0
        """,
        "code": """% 线性规划求解 - 生产计划问题
% 目标函数系数（求最大值时取负）
c = [-5; -4];

% 不等式约束 Ax <= b
A = [2, 4;
     4, 2;
     3, 1];
b = [32; 32; 24];

% 变量下界
lb = [0; 0];

% 求解
[x, fval] = linprog(c, A, b, [], [], lb);

% 输出结果
fprintf('最优解：\\n');
fprintf('生产A产品：%.2f 件\\n', x(1));
fprintf('生产B产品：%.2f 件\\n', x(2));
fprintf('最大利润：%.2f 元\\n', -fval);

% 绘制可行域和最优解
x1 = 0:0.1:12;
y1 = (32 - 2*x1) / 4;  % 约束1
y2 = (32 - 4*x1) / 2;  % 约束2
y3 = 24 - 3*x1;        % 约束3

figure;
hold on;
plot(x1, y1, 'r-', 'LineWidth', 2);
plot(x1, y2, 'g-', 'LineWidth', 2);
plot(x1, y3, 'b-', 'LineWidth', 2);
plot(x(1), x(2), 'ko', 'MarkerSize', 12, 'MarkerFaceColor', 'y');
xlabel('x_1 (A产品)');
ylabel('x_2 (B产品)');
title('线性规划图解法');
legend('约束1', '约束2', '约束3', '最优解');
grid on;
axis([0 12 0 12]);
        """
    },
    {
        "name": "整数规划",
        "name_en": "integer_programming",
        "theory": """
# 整数规划理论

整数规划是线性规划的特殊情况，要求决策变量取整数值。

## 分类
- 纯整数规划：所有变量都是整数
- 混合整数规划：部分变量是整数
- 0-1规划：变量只能取0或1

## 求解方法
1. 分支定界法
2. 割平面法
3. 启发式算法
        """,
        "cases": """
# 背包问题

有5件物品，重量和价值如下：
| 物品 | 重量 | 价值 |
|------|------|------|
| 1    | 2    | 12   |
| 2    | 1    | 10   |
| 3    | 3    | 20   |
| 4    | 2    | 15   |
| 5    | 4    | 25   |

背包容量为7，求最大价值。
        """,
        "code": """% 0-1背包问题 - 整数规划求解
% 物品重量和价值
w = [2, 1, 3, 2, 4];  % 重量
v = [12, 10, 20, 15, 25];  % 价值
capacity = 7;  % 背包容量

% 目标函数（最大化价值）
f = -v;  % 求最大值取负

% 约束条件 w*x <= capacity
A = w;
b = capacity;

% 整数约束（0-1变量）
intcon = 1:5;  % 所有变量都是整数
lb = zeros(5, 1);  % 下界为0
ub = ones(5, 1);   % 上界为1

% 求解
[x, fval] = intlinprog(f, intcon, A, b, [], [], lb, ub);

% 输出结果
fprintf('最优解：\\n');
for i = 1:5
    if x(i) > 0.5
        fprintf('选择物品%d (重量=%d, 价值=%d)\\n', i, w(i), v(i));
    end
end
fprintf('\\n总重量：%.0f\\n', sum(w .* x'));
fprintf('总价值：%.0f\\n', -fval);
        """
    },
    {
        "name": "动态规划",
        "name_en": "dynamic_programming",
        "theory": """
# 动态规划理论

动态规划是解决多阶段决策过程最优化的方法。

## 基本要素
1. 阶段：整个问题的求解过程划分为若干个相互联系的阶段
2. 状态：各阶段开始时的客观条件
3. 决策：在某阶段某状态下的决策
4. 状态转移方程：从前一阶段某状态到后一阶段某状态的转化关系
5. 最优性原理：最优策略具有子策略最优的性质

## 求解步骤
1. 划分阶段
2. 确定状态和状态变量
3. 建立状态转移方程
4. 确定边界条件
5. 逆序或顺序求解
        """,
        "cases": """
# 最短路径问题

某城市有8个交叉路口，从路口1到路口8的各段路程如下图所示。
求从路口1到路口8的最短路径。

路网结构：
1→2(2), 1→3(5)
2→4(3), 2→5(4)
3→4(2), 3→6(6)
4→7(3), 5→7(5)
6→7(4), 5→8(4)
7→8(2), 6→8(5)
        """,
        "code": """% 动态规划求解最短路径问题
% 定义路网邻接矩阵（INF表示不连通）
INF = 999;
G = [0,   2,   5,   INF, INF, INF, INF, INF;
     INF, 0,   INF, 3,   4,   INF, INF, INF;
     INF, INF, 0,   2,   INF, 6,   INF, INF;
     INF, INF, INF, 0,   INF, INF, 3,   INF;
     INF, INF, INF, INF, 0,   INF, 5,   4;
     INF, INF, INF, INF, INF, 0,   4,   5;
     INF, INF, INF, INF, INF, INF, 0,   2;
     INF, INF, INF, INF, INF, INF, INF, 0];

n = 8;  % 节点数
start = 1;  % 起点
dest = 8;   % 终点

% 动态规划数组
d = INF * ones(1, n);  % 到各节点的最短距离
path = zeros(1, n);    % 路径记录

d(start) = 0;

% 逆序动态规划
for k = n-1:-1:1
    for i = 1:n
        if G(k, i) < INF && d(k) + G(k, i) < d(i)
            d(i) = d(k) + G(k, i);
            path(i) = k;
        end
    end
end

% 输出最短路径
fprintf('从节点%d到节点%d的最短距离：%.0f\\n', start, dest, d(dest));
fprintf('最短路径：');
node = dest;
route = node;
while node ~= start
    node = path(node);
    route = [node, route];
end
fprintf('%d', route(1));
for i = 2:length(route)
    fprintf(' → %d', route(i));
end
fprintf('\\n');
        """
    }
]

# 更多分类的模型数据...
# 为了节省篇幅，这里先实现一个分类的完整数据

async def init_models():
    """初始化模型数据"""
    async with AsyncSession(async_engine) as session:
        print("开始初始化模型数据...")

        # 获取数学规划分类
        result = await session.execute(
            select(Category).where(Category.name_en == CategoryEnum.MATHEMATICAL_PROGRAMMING)
        )
        category = result.scalar_one_or_none()

        if not category:
            print("错误：未找到数学规划分类")
            return

        # 添加模型
        for model_data in MATHEMATICAL_PROGRAMMING_MODELS:
            model = Model(
                category_id=category.id,
                name=model_data["name"],
                name_en=model_data["name_en"],
                theory=model_data["theory"],
                cases=model_data["cases"],
                code=model_data["code"]
            )
            session.add(model)

        await session.commit()
        print(f"✓ 已为【{category.name}】添加 {len(MATHEMATICAL_PROGRAMMING_MODELS)} 个模型")
        print("模型数据初始化完成！")


if __name__ == "__main__":
    asyncio.run(init_models())
