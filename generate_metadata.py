#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re
from pathlib import Path

# 项目根目录
project_root = Path(__file__).parent
stickers_dir = project_root / "stickers"

if not stickers_dir.exists():
    print(f"错误：stickers目录不存在！路径: {stickers_dir}")
    exit(1)

print("开始处理文件...")
print(f"目标目录: {stickers_dir}")
print("")

# 获取所有文件并排序
files = sorted([f for f in stickers_dir.iterdir() if f.is_file() and f.suffix.lower() == '.gif'])

print(f"找到 {len(files)} 个GIF文件")
print("")

# 存储映射关系
metadata = {}
rename_count = 0
failed_count = 0

for index, file_path in enumerate(files, start=1):
    old_name = file_path.name
    new_name = f"{index}.gif"
    new_path = stickers_dir / new_name
    
    # 提取中文解释
    # 文件名格式: LingQiusheng_[描述]_[时间戳].gif
    # 需要提取[描述]部分
    match = re.match(r'LingQiusheng_(.+?)_\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}\.gif$', old_name)
    
    if match:
        description = match.group(1)
    else:
        # 备用方案：如果格式不匹配，尝试其他方式
        description = old_name.replace('LingQiusheng_', '').rsplit('_', 4)[0]
    
    # 重命名文件
    try:
        file_path.rename(new_path)
        print(f"✓ [{index:3d}] 已重命名: {old_name} → {new_name}")
        print(f"           中文: {description}")
        
        # 记录到元数据
        metadata[description] = f"/stickers/{new_name}"
        rename_count += 1
    except Exception as e:
        print(f"✗ [{index:3d}] 重命名失败: {old_name}")
        print(f"           错误: {str(e)}")
        failed_count += 1

print("")
print("=" * 50)
print("文件重命名完成！")
print(f"成功: {rename_count} 个文件")
if failed_count > 0:
    print(f"失败: {failed_count} 个文件")
print("=" * 50)
print("")

# 生成JSON文件
metadata_file = project_root / "stickers_metadata.json"

try:
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 已生成元数据文件: {metadata_file}")
    print(f"  包含 {len(metadata)} 个条目")
    print("")
    
    # 显示部分预览
    print("预览（前10条）:")
    for i, (key, value) in enumerate(list(metadata.items())[:10]):
        print(f"  \"{key}\": \"{value}\"")
    if len(metadata) > 10:
        print(f"  ... 还有 {len(metadata) - 10} 条")
    
except Exception as e:
    print(f"✗ 生成JSON文件失败: {str(e)}")
    exit(1)

print("")
print("=" * 50)
print("所有操作完成！")
print("=" * 50)
