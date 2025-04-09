import math
import random
import svgwrite
from datetime import datetime

def generate_health_monitoring_svg(output_file="health_monitoring_realistic.svg", width=1200, height=800):
    """生成更加真实照片风格的健康监控界面"""
    # 创建SVG画布，使用完整SVG配置文件
    dwg = svgwrite.Drawing(output_file, size=(width, height))
    
    # 添加渐变定义
    add_gradients_and_filters(dwg)
    
    # 添加背景 - 使用更逼真的医疗设备面板颜色
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='url(#bg_gradient)', rx=5, ry=5))
    
    # 添加边框高光效果模拟塑料机身
    dwg.add(dwg.rect(insert=(2, 2), size=(width-4, height-4), 
                     fill='none', stroke='white', stroke_width=1, 
                     stroke_opacity=0.3, rx=5, ry=5))
    
    # 添加标题区域
    title_bg = dwg.rect(insert=(50, 20), size=(width-100, 80), 
                     fill='url(#header_gradient)', rx=5, ry=5,
                     filter="url(#drop_shadow)")
    dwg.add(title_bg)
    
    # 添加标题和品牌
    dwg.add(dwg.text("HealthGuard™ Pro 3000", insert=(width//2, 60), 
                     font_size=28, font_family="Arial", 
                     text_anchor="middle", fill='white', font_weight="bold"))
    
    dwg.add(dwg.text("实时生命体征监测系统", insert=(width//2, 90), 
                     font_size=18, font_family="Arial", 
                     text_anchor="middle", fill='#e0e0ff'))
    
    # 添加当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dwg.add(dwg.text(f"更新时间: {current_time}", insert=(width-80, 50), 
                     font_size=14, font_family="Arial", 
                     text_anchor="end", fill='#a0e0ff'))
    
    # 添加扫描线动画效果 - 模拟CRT显示器
    dwg.add(dwg.rect(insert=(0, 140 + (datetime.now().second % 10) * 50), 
                     size=(width, 5), fill='#81e8ff', fill_opacity=0.1))
    
    # 定义四个指标区域的参数 - 更真实的医疗参数和范围
    metrics = [
        {"name": "心率", "unit": "BPM", "value": 72, "min": 40, "max": 180, "color": "#ff2e63", 
         "x": width//4, "y": height//3, "normal_range": "60-100"},
        {"name": "血氧", "unit": "%", "value": 98, "min": 80, "max": 100, "color": "#00b8d9", 
         "x": 3*width//4, "y": height//3, "normal_range": "95-100"},
        {"name": "呼吸率", "unit": "次/分", "value": 16, "min": 8, "max": 30, "color": "#48cae4", 
         "x": width//4, "y": 2*height//3, "normal_range": "12-20"},
        {"name": "血糖", "unit": "mmol/L", "value": 5.8, "min": 3.0, "max": 10.0, "color": "#9d4edd", 
         "x": 3*width//4, "y": 2*height//3, "normal_range": "4.0-6.1"}
    ]
    
    # 绘制每个指标区域
    for metric in metrics:
        draw_realistic_metric_box(dwg, metric)
    
    # 添加波形图例 - 更真实的医疗监测波形
    draw_realistic_wave_legend(dwg, width, height)
    
    # 添加装饰和细节
    draw_realistic_decorations(dwg, width, height)
    
    # 保存SVG文件
    dwg.save()
    print(f"Realistic SVG monitoring interface generated: {output_file}")
    return output_file

def add_gradients_and_filters(dwg):
    """添加渐变和滤镜效果，增强真实感"""
    # 添加背景渐变
    bg_gradient = dwg.linearGradient(id="bg_gradient", x1=0, y1=0, x2=0, y2=1)
    bg_gradient.add_stop_color(offset=0, color='#1e293b', opacity=1)
    bg_gradient.add_stop_color(offset=1, color='#0f172a', opacity=1)
    dwg.defs.add(bg_gradient)
    
    # 添加标题区域渐变
    header_gradient = dwg.linearGradient(id="header_gradient", x1=0, y1=0, x2=0, y2=1)
    header_gradient.add_stop_color(offset=0, color='#334477', opacity=1)
    header_gradient.add_stop_color(offset=1, color='#223366', opacity=1)
    dwg.defs.add(header_gradient)
    
    # 添加指标面板渐变
    panel_gradient = dwg.linearGradient(id="panel_gradient", x1=0, y1=0, x2=0, y2=1)
    panel_gradient.add_stop_color(offset=0, color='#1e293b', opacity=1)
    panel_gradient.add_stop_color(offset=1, color='#1a1f35', opacity=1)
    dwg.defs.add(panel_gradient)
    
    # 添加波形区域渐变
    wave_gradient = dwg.linearGradient(id="wave_gradient", x1=0, y1=0, x2=0, y2=1)
    wave_gradient.add_stop_color(offset=0, color='#0f1729', opacity=1)
    wave_gradient.add_stop_color(offset=1, color='#101624', opacity=1)
    dwg.defs.add(wave_gradient)
    
    # 添加阴影滤镜
    filter = dwg.filter(id="drop_shadow", x="-20%", y="-20%", width="140%", height="140%")
    filter.feGaussianBlur(in_="SourceAlpha", stdDeviation=3)
    filter.feOffset(dx=2, dy=2)
    
    # 创建componentTransfer并添加funcA，正确使用type_参数
    transfer = filter.feComponentTransfer()
    transfer.feFuncA(type_="linear", slope=0.5)
    
    filter.feBlend(in_="SourceGraphic", mode="normal")
    dwg.defs.add(filter)
    
    # 添加发光滤镜
    glow = dwg.filter(id="glow_effect", x="-20%", y="-20%", width="140%", height="140%")
    glow.feGaussianBlur(in_="SourceGraphic", stdDeviation=2)
    
    # 创建componentTransfer并添加funcA，正确使用type_参数
    glow_transfer = glow.feComponentTransfer()
    glow_transfer.feFuncA(type_="linear", slope=1.5)
    
    glow.feBlend(in_="SourceGraphic", mode="screen")
    dwg.defs.add(glow)
    
    # 添加心电图发光滤镜
    ecg_glow = dwg.filter(id="ecg_glow", x="-10%", y="-10%", width="120%", height="120%")
    ecg_glow.feGaussianBlur(in_="SourceGraphic", stdDeviation=1)
    
    # 创建componentTransfer并添加funcA，正确使用type_参数
    ecg_transfer = ecg_glow.feComponentTransfer()
    ecg_transfer.feFuncA(type_="linear", slope=2)
    
    ecg_glow.feBlend(in_="SourceGraphic", mode="screen")
    dwg.defs.add(ecg_glow)

def draw_realistic_metric_box(dwg, metric):
    """绘制更加真实的医疗监控指标面板"""
    box_width, box_height = 280, 180
    x, y = metric["x"] - box_width//2, metric["y"] - box_height//2
    
    # 绘制指标框背景 - 添加内嵌显示屏效果
    outer_panel = dwg.rect(insert=(x, y), size=(box_width, box_height), 
                     fill='#0a1022', rx=8, ry=8, 
                     stroke="#344266", stroke_width=2,
                     filter="url(#drop_shadow)")
    dwg.add(outer_panel)
    
    inner_panel = dwg.rect(insert=(x+8, y+8), size=(box_width-16, box_height-16), 
                     fill='url(#panel_gradient)', rx=4, ry=4)
    dwg.add(inner_panel)
    
    # 模拟屏幕反光
    reflection = dwg.path(d=f"M {x+10} {y+10} l {box_width-20} 0 l 0 10 l -{box_width-20} 0 z", 
                         fill="white", fill_opacity=0.05)
    dwg.add(reflection)
    
    # 绘制指标名称 - 模拟LED显示
    name_bg = dwg.rect(insert=(x+15, y+15), size=(box_width-110, 30), 
                     fill='#0a0e1c', rx=3, ry=3)
    dwg.add(name_bg)
    
    dwg.add(dwg.text(metric["name"], insert=(x+25, y+36), 
                     font_size=18, font_family="Arial", 
                     fill=metric["color"], font_weight="bold",
                     filter="url(#glow_effect)"))
    
    # 绘制指标值 - 模拟LED数字显示
    value_text = f"{metric['value']}" if isinstance(metric['value'], int) else f"{metric['value']:.1f}"
    dwg.add(dwg.text(value_text, insert=(x+25, y+90), 
                     font_size=48, font_family="'Courier New', monospace", 
                     fill=metric["color"], font_weight="bold",
                     filter="url(#glow_effect)"))
    
    # 绘制单位和正常范围
    dwg.add(dwg.text(metric["unit"], insert=(x+25, y+120), 
                     font_size=16, font_family="Arial", 
                     fill='#8d99ae'))
    
    dwg.add(dwg.text(f"正常范围: {metric['normal_range']}", insert=(x+25, y+145), 
                     font_size=14, font_family="Arial", 
                     fill='#8d99ae'))
    
    # 绘制状态LED指示灯
    status_color = "#4ade80" if is_in_normal_value(metric["value"], metric["normal_range"]) else "#f43f5e"
    led_x, led_y = x + box_width - 45, y + 30
    
    # LED底座
    dwg.add(dwg.circle(center=(led_x, led_y), r=12, 
                       fill="#0a0e1c", stroke="#344266", stroke_width=1))
    
    # LED灯 - 直接添加滤镜属性
    led = dwg.circle(center=(led_x, led_y), r=8, 
                     fill=status_color,
                     filter="url(#glow_effect)")
    dwg.add(led)
    
    # 绘制更真实的波形
    wave_bg = dwg.rect(insert=(x+15, y+box_height-50), size=(box_width-30, 35), 
                     fill='#0a0e1c', rx=3, ry=3)
    dwg.add(wave_bg)
    
    # 生成特定类型的波形
    if metric["name"] == "心率":
        wave_path = generate_ecg_wave(x+20, y+box_height-32, box_width-40, 20, metric["color"])
    elif metric["name"] == "血氧":
        wave_path = generate_pluth_wave(x+20, y+box_height-32, box_width-40, 20, metric["color"])
    elif metric["name"] == "呼吸率":
        wave_path = generate_respiratory_wave(x+20, y+box_height-32, box_width-40, 20, metric["color"])
    else:
        wave_path = generate_smooth_wave(x+20, y+box_height-32, box_width-40, 20, metric["color"])
    
    # 直接添加滤镜属性
    wave_element = dwg.path(d=wave_path, fill="none", stroke=metric["color"], stroke_width=2,
                          filter="url(#ecg_glow)")
    dwg.add(wave_element)

def is_in_normal_value(value, range_str):
    """检查值是否在正常范围内"""
    low, high = map(float, range_str.split('-'))
    return low <= value <= high

def generate_ecg_wave(x, y, width, height, color):
    """生成仿真心电图波形"""
    path = f"M {x} {y}"
    segment_width = width / 4
    
    for i in range(4):
        base_x = x + i * segment_width
        # P波
        path += f" L {base_x + segment_width*0.1} {y - height*0.2}"
        # 回基线
        path += f" L {base_x + segment_width*0.2} {y}"
        # Q波
        path += f" L {base_x + segment_width*0.25} {y + height*0.2}"
        # R波 (尖峰)
        path += f" L {base_x + segment_width*0.3} {y - height*0.8}"
        # S波
        path += f" L {base_x + segment_width*0.35} {y + height*0.3}"
        # 回基线
        path += f" L {base_x + segment_width*0.4} {y}"
        # T波
        path += f" L {base_x + segment_width*0.6} {y - height*0.3}"
        # 回基线
        path += f" L {base_x + segment_width*0.8} {y}"
    
    return path

def generate_pluth_wave(x, y, width, height, color):
    """生成仿真血氧波形(脉搏血氧波形)"""
    path = f"M {x} {y}"
    segment_width = width / 6
    
    for i in range(6):
        base_x = x + i * segment_width
        # 缓慢上升
        path += f" L {base_x + segment_width*0.3} {y - height*0.1}"
        # 快速上升
        path += f" L {base_x + segment_width*0.4} {y - height*0.9}"
        # 双峰顶部
        path += f" L {base_x + segment_width*0.5} {y - height*0.7}"
        path += f" L {base_x + segment_width*0.6} {y - height*0.8}"
        # 下降
        path += f" L {base_x + segment_width*0.9} {y}"
    
    return path

def generate_respiratory_wave(x, y, width, height, color):
    """生成仿真呼吸波形"""
    path = f"M {x} {y}"
    segment_width = width / 3
    
    for i in range(3):
        base_x = x + i * segment_width
        # 缓慢上升(吸气)
        path += f" Q {base_x + segment_width*0.25} {y - height*0.9}, {base_x + segment_width*0.5} {y - height*0.9}"
        # 缓慢下降(呼气)
        path += f" Q {base_x + segment_width*0.75} {y - height*0.9}, {base_x + segment_width} {y}"
    
    return path

def generate_smooth_wave(x, y, width, height, color):
    """生成平滑波形"""
    path = f"M {x} {y}"
    points = []
    
    for i in range(0, width+1, 5):
        value = 0
        for freq, amp in [(0.01, 0.4), (0.03, 0.2), (0.07, 0.4)]:
            value += math.sin(i * freq * 2 * math.pi) * amp
        
        point_y = y - (value * height/2 + height/5)
        points.append((x + i, point_y))
    
    # 创建平滑的曲线
    for i in range(1, len(points)):
        cp1x = (points[i][0] + points[i-1][0]) / 2
        cp1y = points[i-1][1]
        cp2x = (points[i][0] + points[i-1][0]) / 2
        cp2y = points[i][1]
        path += f" C {cp1x} {cp1y}, {cp2x} {cp2y}, {points[i][0]} {points[i][1]}"
    
    return path

def draw_realistic_wave_legend(dwg, width, height):
    """绘制更真实的波形图例区域"""
    legend_y = height - 140
    legend_height = 120
    
    # 创建波形图例背景 - 模拟嵌入式显示屏
    outer_panel = dwg.rect(insert=(30, legend_y), size=(width - 60, legend_height), 
                     fill='#0a1022', rx=8, ry=8, 
                     stroke="#344266", stroke_width=2,
                     filter="url(#drop_shadow)")
    dwg.add(outer_panel)
    
    inner_panel = dwg.rect(insert=(38, legend_y+8), size=(width - 76, legend_height-16), 
                     fill='url(#wave_gradient)', rx=4, ry=4)
    dwg.add(inner_panel)
    
    # 标题
    dwg.add(dwg.text("24小时生命体征趋势", insert=(width//2, legend_y+30), 
                     font_size=16, font_family="Arial", 
                     text_anchor="middle", fill="white", font_weight="bold"))
    
    # 创建时间刻度
    times = ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "24:00"]
    grid_width = width - 100
    
    # 水平轴线
    dwg.add(dwg.line(start=(50, legend_y+80), end=(50+grid_width, legend_y+80), 
                    stroke='#444c66', stroke_width=1))
    
    for i, time in enumerate(times):
        x = 50 + (i * grid_width / (len(times) - 1))
        # 时间标签
        dwg.add(dwg.text(time, insert=(x, legend_y+100), 
                        font_size=12, font_family="Arial", 
                        text_anchor="middle", fill='#8d99ae'))
        
        # 垂直网格线
        dwg.add(dwg.line(start=(x, legend_y+40), end=(x, legend_y+80), 
                        stroke='#344266', stroke_width=1, stroke_dasharray="2,2"))

    # 绘制几条不同颜色的波形 - 模拟真实生理信号
    wave_types = [
        {"name": "心率", "color": "#ff2e63", "generate_func": generate_ecg_wave},
        {"name": "血氧", "color": "#00b8d9", "generate_func": generate_pluth_wave},
        {"name": "呼吸率", "color": "#48cae4", "generate_func": generate_respiratory_wave},
        {"name": "血糖", "color": "#9d4edd", "generate_func": generate_smooth_wave}
    ]
    
    # 绘制波形
    for i, wave_type in enumerate(wave_types):
        # 指标标签
        dwg.add(dwg.text(wave_type["name"], insert=(45, legend_y+55+i*6), 
                        font_size=10, font_family="Arial", 
                        text_anchor="end", fill=wave_type["color"]))
                
        # 生成并显示波形
        offset = i * 8 - 10
        wave_path = wave_type["generate_func"](50, legend_y+60+offset, grid_width, 15, wave_type["color"])
        # 直接添加滤镜属性
        wave_element = dwg.path(d=wave_path, fill="none", stroke=wave_type["color"], 
                               stroke_width=1.5, filter="url(#ecg_glow)")
        dwg.add(wave_element)

def draw_realistic_decorations(dwg, width, height):
    """绘制更真实的医疗设备装饰元素"""
    # 添加设备控制面板区域
    control_panel = dwg.rect(insert=(width-130, 120), size=(100, 200), 
                     fill='#1a1e2e', rx=5, ry=5, 
                     stroke="#344266", stroke_width=1,
                     filter="url(#drop_shadow)")
    dwg.add(control_panel)
    
    # 添加按钮和旋钮
    buttons = [
        {"label": "报警设置", "y": 150, "color": "#aab9cf"},
        {"label": "打印", "y": 190, "color": "#aab9cf"},
        {"label": "静音", "y": 230, "color": "#f1a942"},
        {"label": "锁定", "y": 270, "color": "#aab9cf"}
    ]
    
    for button in buttons:
        # 按钮背景
        dwg.add(dwg.rect(insert=(width-120, button["y"]), size=(80, 25), 
                        fill='#0f1525', rx=3, ry=3, 
                        stroke="#344266", stroke_width=1))
        
        # 按钮文字
        dwg.add(dwg.text(button["label"], insert=(width-80, button["y"]+17), 
                        font_size=12, font_family="Arial", 
                        text_anchor="middle", fill=button["color"]))
    
    # 设备信息面板
    info_panel = dwg.rect(insert=(30, 120), size=(100, 200), 
                     fill='#1a1e2e', rx=5, ry=5, 
                     stroke="#344266", stroke_width=1,
                     filter="url(#drop_shadow)")
    dwg.add(info_panel)
    
    # 设备信息
    device_info = [
        {"label": "设备ID", "value": "HC-7830", "y": 145},
        {"label": "患者ID", "value": "P-10056", "y": 175},
        {"label": "医护", "value": "张医生", "y": 205},
        {"label": "模式", "value": "连续监测", "y": 235},
        {"label": "状态", "value": "正常", "y": 265, "value_color": "#4ade80"}
    ]
    
    for info in device_info:
        # 标签
        dwg.add(dwg.text(info["label"], insert=(40, info["y"]), 
                        font_size=10, font_family="Arial", 
                        fill='#8d99ae'))
        
        # 值
        value_color = info.get("value_color", "#e0e0ff")
        dwg.add(dwg.text(info["value"], insert=(40, info["y"]+15), 
                        font_size=12, font_family="Arial", 
                        fill=value_color))
    
    # 添加医院标志
    logo_circle = dwg.circle(center=(80, 330), r=15, 
                           fill='#0a1022', stroke="#4f83cc", stroke_width=2)
    dwg.add(logo_circle)
    
    # 添加十字标志
    dwg.add(dwg.line(start=(80, 320), end=(80, 340), stroke='#4f83cc', stroke_width=2))
    dwg.add(dwg.line(start=(70, 330), end=(90, 330), stroke='#4f83cc', stroke_width=2))
    
    # 添加医院名称
    dwg.add(dwg.text("山东医学中心", insert=(120, 335), 
                    font_size=14, font_family="Arial", 
                    fill='#aab9cf'))
    
    # 添加状态指示器
    dwg.add(dwg.circle(center=(width-30, 40), r=8, fill='#4ade80', filter="url(#glow_effect)"))
    dwg.add(dwg.text("在线监测中", insert=(width-45, 40), 
                    font_size=12, font_family="Arial", 
                    text_anchor="end", fill='#4ade80'))
    
    # 添加网格背景
    for i in range(40, width, 40):
        dwg.add(dwg.line(start=(i, 0), end=(i, height), 
                        stroke='#223355', stroke_width=0.5, stroke_opacity=0.2))
    for i in range(40, height, 40):
        dwg.add(dwg.line(start=(0, i), end=(width, i), 
                        stroke='#223355', stroke_width=0.5, stroke_opacity=0.2))
    
    # 添加设备镜面反光效果
    reflection = dwg.path(d=f"M 30 20 L {width-30} 20 L {width-60} 15 L 60 15 Z", 
                         fill="white", fill_opacity=0.03)
    dwg.add(reflection)

if __name__ == "__main__":
    generate_health_monitoring_svg()
