import os
from PIL import Image


def convert_jpg_to_webp(directory):
    """
    将指定目录下所有 JPG 图片转换为 WebP 格式，并显示转换前后文件大小。

    Args:
        directory (str): 包含 JPG 图片的目录路径。
    """
    if not os.path.isdir(directory):
        print(f"错误：目录 '{directory}' 不存在。")
        return

    print(f"正在处理目录：'{directory}'")
    print("-" * 30)

    for filename in os.listdir(directory):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            filepath = os.path.join(directory, filename)

            try:
                # 获取原始文件大小
                original_size = os.path.getsize(filepath)
                print(f"文件: {filename}")
                print(f"  原始大小: {original_size / 1024:.2f} KB")

                # 打开图片并转换为 WebP
                with Image.open(filepath) as img:
                    webp_filename = os.path.splitext(filename)[0] + ".webp"
                    webp_filepath = os.path.join(directory, webp_filename)
                    img.save(webp_filepath, "webp")

                # 获取转换后文件大小
                converted_size = os.path.getsize(webp_filepath)
                print(f"  转换后大小: {converted_size / 1024:.2f} KB (保存为 {webp_filename})")
                print("-" * 30)

            except Exception as e:
                print(f"  处理文件 '{filename}' 时发生错误: {e}")
                print("-" * 30)


if __name__ == "__main__":
    # 指定你的图片目录
    # 由于你提供了具体的路径，我将使用它。请确保该路径正确。
    image_directory = r"C:\Users\gy_caoshipeng\Desktop\photo-gallery-main\pictures"
    convert_jpg_to_webp(image_directory)