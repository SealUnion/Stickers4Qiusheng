#!/bin/bash

# 重命名脚本：将stickers目录中所有文件名的CoffeeBean修改为LingQiusheng

STICKERS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/stickers"

if [ ! -d "$STICKERS_DIR" ]; then
    echo "错误：stickers目录不存在！路径: $STICKERS_DIR"
    exit 1
fi

# 计数器
count=0
failed=0

echo "开始重命名文件..."
echo "目标目录: $STICKERS_DIR"
echo ""

# 遍历所有文件
for file in "$STICKERS_DIR"/CoffeeBean*; do
    if [ -f "$file" ]; then
        # 获取文件名（不含路径）
        filename=$(basename "$file")
        
        # 替换文件名中的CoffeeBean为LingQiusheng
        newfilename="${filename//CoffeeBean/LingQiusheng}"
        
        # 构建新的完整路径
        newfile="$STICKERS_DIR/$newfilename"
        
        # 重命名文件
        if mv "$file" "$newfile"; then
            echo "✓ 已重命名: $filename → $newfilename"
            ((count++))
        else
            echo "✗ 重命名失败: $filename"
            ((failed++))
        fi
    fi
done

echo ""
echo "================================"
echo "重命名完成！"
echo "成功: $count 个文件"
if [ $failed -gt 0 ]; then
    echo "失败: $failed 个文件"
fi
echo "================================"
