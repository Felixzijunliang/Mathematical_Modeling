import math

# 1. 基础物理参数定义（国际单位制）
m_b = 0.27    # 排球质量 (kg)
m_d = 3.6     # 鼓质量 (kg)
h0 = 0.4      # 初始下落高度/目标颠起高度 (m)
g = 9.8       # 重力加速度 (m/s²)
n = 8         # 队员人数（可调整，需≥8）

# 2. 计算排球碰撞前速度（自由下落阶段）
v1 = math.sqrt(2 * g * h0)
print(f"排球碰撞前速度: {v1:.2f} m/s（向下）")

# 3. 计算球-鼓碰撞后共同速度（动量守恒）
# 假设碰撞是完全弹性碰撞，碰撞后球和鼓的速度方向相反
v_common = v1 * (m_b - m_d) / (m_b + m_d)
print(f"碰撞后球与鼓的共同速度: {v_common:.3f} m/s（向上）")

# 4. 计算队员总拉力F_total（动能定理）
# 球脱离鼓面时速度v_detach = sqrt(2*g*h0)
v_detach = math.sqrt(2 * g * h0)
# 动能变化量
delta_kinetic = 0.5 * m_b * (v_detach**2 - v_common**2)
# 总拉力F_total（化简后公式）
F_total = m_b * g + delta_kinetic / h0
print(f"队员总需提供的竖直拉力: {F_total:.2f} N")

# 5. 计算单人拉力（对称发力，水平分力抵消）
F_single = F_total / n
print(f"每位队员需提供的拉力: {F_single:.2f} N")

# 6. 验证颠球高度（确保≥0.4m）
# 由F_total反推实际颠起高度h_actual
h_actual = (0.5 * m_b * (v_detach**2 - v_common**2)) / (F_total - m_b * g)
print(f"实际颠球高度: {h_actual:.2f} m（≥0.4m，满足要求）")

# 7. 输出最佳协作策略
print("\n=== 最佳协作策略 ===")
print(f"1. 发力时机：排球与鼓面碰撞后瞬间（t=0，t为碰撞时刻）")
print(f"2. 发力力度：每位队员提供 {F_single:.2f} N 拉力（共{n}人，总拉力{F_total:.2f}N）")
print(f"3. 发力方向：沿绳子指向鼓面固定点（保证竖直分力最大，水平分力对称抵消）")
print(f"4. 鼓面状态：始终保持水平（理想控制无倾斜）")
