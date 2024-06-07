#!/bin/bash

# Проверяем наличие аргумента
if [ -z "$1" ]; then
    echo "Usage: $0 input_file"
    exit 1
fi

# Получаем путь и имя файла без расширения
file_path=$(dirname "$1")
file_name=$(basename "$1")
file_name_no_ext="${file_name%.*}"

# Конвертируем файл в mp3
ffmpeg -i "$1" -ac 1 -ar 16000 "$file_path/$file_name_no_ext.mp3"

echo "Conversion complete: $file_path/$file_name_no_ext.mp3"

