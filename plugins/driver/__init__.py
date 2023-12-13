import shutil
import os

from plugins.driver.derive import MemoryRw
from common.file import force_delete_file

driver = MemoryRw()


def init_driver(driver_name: str):
    src = "./static/{}.sys".format(driver_name)
    driver_path = "C:\\{}\\{}.sys".format(driver_name, driver_name)
    if os.path.exists(driver_path) is False:
        try:
            shutil.copy2(os.path.abspath(src), driver_path)
        except Exception as e:
            raise Exception("驱动不存在")

    if not driver.load_driver(driver_path, driver_name, driver_name):
        raise Exception("驱动加载失败")

    force_delete_file(driver_path)