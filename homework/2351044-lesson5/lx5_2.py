import cv2
import os


def cartoonise(picture_name):
    # 构造输出文件路径
    imgInput_FileName = picture_name
    imgOutput_FileName = picture_name.rsplit('.', 1)[0] + 'cartoon.jpg'

    # 检查输入文件是否存在
    if not os.path.isfile(imgInput_FileName):
        print(f"错误: 输入文件 {imgInput_FileName} 不存在.")
        return

    # 读取图片
    img_rgb = cv2.imread(imgInput_FileName)
    if img_rgb is None:
        print(f"错误: 无法读取文件 {imgInput_FileName}.")
        return

    # 用高斯金字塔降低取样
    img_color = img_rgb
    num_down = 2  # 缩减像素采样的数目
    num_bilateral = 7  # 定义双边滤波的数目

    for _ in range(num_down):
        img_color = cv2.pyrDown(img_color)

    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

    for _ in range(num_down):
        img_color = cv2.pyrUp(img_color)

    # 转换为灰度并且使其产生中等的模糊
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)

    # 检测到边缘并且增强其效果
    img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,
                                     blockSize=9,
                                     C=2)

    # 转换回彩色图像
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

    # 调整边缘图像大小以匹配彩色图像大小
    if img_color.shape[:2] != img_edge.shape[:2]:
        img_edge = cv2.resize(img_edge, (img_color.shape[1], img_color.shape[0]), interpolation=cv2.INTER_AREA)

    # 合并边缘和滤波后的图像
    img_cartoon = cv2.bitwise_and(img_color, img_edge)

    # 确保输出目录存在
    output_directory = os.path.dirname(imgOutput_FileName)
    if output_directory:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
    else:
        # 如果没有目录部分，则直接使用当前工作目录
        output_directory = os.getcwd()

    # 保存转换后的图片
    full_output_path = os.path.join(output_directory, imgOutput_FileName)
    if not cv2.imwrite(full_output_path, img_cartoon):
        print(f"错误: 无法写入文件 {full_output_path}.")
    else:
        print(f"卡通化后的图像已保存为 {full_output_path}")


# 调用函数
cartoonise('2351044.jpg')
