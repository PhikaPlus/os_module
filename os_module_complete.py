import os

# 1: os name
print(os.name)

# 2: Executing a shell command
# برای اجرای دستورات شل
os.system('mkdir NEW_FOLDER')

# 3: Returns the current working directory.
# نمایش دایرکتوری فعلی
print(os.getcwd())


# 4: Return a list of files and folders in cwd
# نمایش فایل ها و فولدرها در یک دایرکتوری
print(os.listdir())

# 5: Create a directory named 'DIR1'
# ساخت فولدر یا دایرکتوری
os.mkdir('DIR1')

# 6: Remove (delete) the file.
# حذف یک فایل
os.remove('Log.txt')

# 7: Remove directories recursively.
# حذف یک دایرکتوری خاص
os.removedirs('DIR1')

# 8: Remove (delete) the directory path.
# حذف یک دایرکتوری خاص
os.rmdir('DIR1')

# 9: Rename the file or directory src to dst.
# تغییر نام یک فایل یا دایرکتوری
os.rename('test', 'test1')

# 10: Change the current working directory to path
# تغیر دایرکتوری
os.chdir('new_path')


# 11: is file or directory?
# اسم داده شده فایل هستش یا دایرکتوری
print(os.path.isfile('test1'))
print(os.path.isdir('test1.png'))


# 12: create path
# ساخت مسیر فایل یا دایرکتوری
# os.sep: OS separator (in windows = '\')
print(os.path.join(os.sep, 'dir1', 'dir2', 'my_file.txt'))

# 13: returns True if dir exists (full pathname or filename)
# آیا یک فایل یا فولدر در دایرکتوری مورد نظر موجود است؟
print(os.path.exists('DIR1'))

# 14: returns size of a file ("bytes")
# بدست آوردن حجم یک فایل
print(os.path.getsize('my_file.txt'))

# 15: returns time when the file was last modified
# آخرین زمانی که فایل مورد نظر تغییر کرده؟
import time
make_time = os.path.getmtime('my_file.txt')
print(time.ctime(make_time))



# 16: get file path, file name and file directory
# دسترسی به نام فایل، نام دایرکتوری و مسیر کامل فایل
file_path = os.path.abspath(__file__)
print(file_path)
# F:\Programming\Examples_Projects\Python\os_example.py

file_name = os.path.basename(file_path)
print(file_name)
# os_example.py

file_dir = os.path.dirname(file_path)
print(file_dir)
# F:\Programming\Examples_Projects\Python
