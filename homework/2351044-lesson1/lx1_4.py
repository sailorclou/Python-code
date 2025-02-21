import qrcode
from PIL import Image


def generate_and_open_qr_code(url, file_path):
    # 创建 QR code 对象
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # 向 QR code 传输信息
    qr.add_data(url)
    qr.make(fit=True)

    # 从 QR code 实例生成图像
    img = qr.make_image(fill='black', back_color='white')

    # 保存图像
    img.save(file_path)
    print(f"QR code saved to {file_path}")

    # 打开图像
    img.show()


# URL
url = "https://www.tongji.edu.cn"
# 保存路径
file_path = "tongji_qr_code.png"

# 产生二维码并打开
generate_and_open_qr_code(url, file_path)
