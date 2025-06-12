import os
from PIL import Image

def compress_images(folder_path, quality=30):
    """
    遍历指定文件夹下的所有图片，并进行压缩。
    压缩后的图片将替换原始图片。

    Args:
        folder_path (str): 包含图片的文件夹路径。
        quality (int): 压缩质量，0-100之间，100代表最高质量。
                       默认值为85，这是一个在质量和文件大小之间较好的平衡点。
    """
    if not os.path.isdir(folder_path):
        print(f"错误：文件夹 '{folder_path}' 不存在。")
        return

    print(f"开始压缩文件夹 '{folder_path}' 中的图片...")
    compressed_count = 0

    # 支持的图片格式
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 检查是否是文件且是支持的图片格式
        if os.path.isfile(file_path) and filename.lower().endswith(supported_formats):
            try:
                # 打开图片
                with Image.open(file_path) as img:
                    original_size = os.path.getsize(file_path)

                    # 如果是PNG，尝试优化压缩；其他格式则直接调整质量
                    if img.format == 'PNG':
                        # 对于PNG，optimize=True可以减小文件大小，通常不会损失质量
                        img.save(file_path, optimize=True)
                    else:
                        # 对于JPEG等格式，通过调整质量参数进行压缩
                        img.save(file_path, quality=quality)

                    new_size = os.path.getsize(file_path)
                    print(f"已压缩 '{filename}'：原始大小 {original_size / 1024:.2f} KB -> 压缩后 {new_size / 1024:.2f} KB")
                    compressed_count += 1

            except Exception as e:
                print(f"处理文件 '{filename}' 时发生错误：{e}")

    print(f"--- 压缩完成！共压缩了 {compressed_count} 张图片。---")

if __name__ == "__main__":
    images_folder = input("请输入您要压缩图片的文件夹路径：")
    compress_images(images_folder)