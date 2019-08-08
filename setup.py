import cx_Freeze
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable(script="billgates.py",
                                    icon = "img/techlaunch.ico",
                                    base=base
                                    )]

cx_Freeze.setup(
    name="MLG_B1llG@t3sTr0j@n.exe",
    version = "1.0",
    options={"build_exe":{"packages":["pygame"],"include_files":["img", "settings.py", "starthacks.bat",
                                                                "hacks.bat", "BILL_GATES_HACKED_YOUR_COMPUTER.vbs",
                                                                "message.vbs"]}},
    description = "Bill Gates WindowsXP Trojan Wirus Found!!!",
    executables = executables
    )
