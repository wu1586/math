from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Category, CategoryEnum


async def init_categories(db: AsyncSession):
    """初始化10大分类数据"""
    categories_data = [
        {
            "name": "数学规划",
            "name_en": CategoryEnum.MATHEMATICAL_PROGRAMMING,
            "description": "线性规划、整数规划、非线性规划、动态规划等优化问题求解方法",
            "icon": "calculator",
            "display_order": 1
        },
        {
            "name": "综合评价与决策",
            "name_en": CategoryEnum.EVALUATION_DECISION,
            "description": "AHP层次分析法、TOPSIS、DEA数据包络分析等多指标评价方法",
            "icon": "assessment",
            "display_order": 2
        },
        {
            "name": "预测类模型",
            "name_en": CategoryEnum.PREDICTION,
            "description": "回归分析、时间序列分析、机器学习预测等预测建模方法",
            "icon": "trending_up",
            "display_order": 3
        },
        {
            "name": "概率统计与数据分析",
            "name_en": CategoryEnum.STATISTICS,
            "description": "聚类分析、主成分分析、假设检验等统计分析方法",
            "icon": "analytics",
            "display_order": 4
        },
        {
            "name": "微分方程与系统动力学",
            "name_en": CategoryEnum.DIFFERENTIAL_EQUATIONS,
            "description": "常微分方程、偏微分方程、传染病模型等动态系统建模",
            "icon": "timeline",
            "display_order": 5
        },
        {
            "name": "图论与网络优化",
            "name_en": CategoryEnum.GRAPH_THEORY,
            "description": "最短路径、网络流、旅行商问题等图论算法",
            "icon": "share",
            "display_order": 6
        },
        {
            "name": "智能优化算法",
            "name_en": CategoryEnum.INTELLIGENT_OPTIMIZATION,
            "description": "遗传算法、粒子群算法、模拟退火等启发式优化算法",
            "icon": "psychology",
            "display_order": 7
        },
        {
            "name": "机器学习与数据挖掘",
            "name_en": CategoryEnum.MACHINE_LEARNING,
            "description": "监督学习、深度学习、神经网络等机器学习方法",
            "icon": "smart_toy",
            "display_order": 8
        },
        {
            "name": "运筹学经典模型",
            "name_en": CategoryEnum.OPERATIONS_RESEARCH,
            "description": "排队论、存贮论、博弈论等运筹学经典理论",
            "icon": "grid_on",
            "display_order": 9
        },
        {
            "name": "其他专项模型",
            "name_en": CategoryEnum.OTHER_MODELS,
            "description": "元胞自动机、贝叶斯网络、模糊数学等特殊模型",
            "icon": "extension",
            "display_order": 10
        }
    ]

    for cat_data in categories_data:
        category = Category(**cat_data)
        db.add(category)

    await db.commit()
    print("✓ 分类数据初始化完成")
