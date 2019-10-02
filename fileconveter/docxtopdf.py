import sys
import subprocess
import re


def convert_to(folder, source, timeout=None):
    print(source)
    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]
    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    # stdout, stderr = process.communicate()
    # stdout_formatted = stdout.decode('UTF-16')
    # stderr_formatted = stderr.decode('UTF-16')
    print(process)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())
    print(filename)
    if filename is None:
        filename=source
        indx=filename.find('.docx')
        filename=filename[:indx]+".pdf"
        print(filename)
        return filename
    else:
        return filename.group(1)


def libreoffice_exec():
    # TODO: Provide support for more platforms
    if sys.platform == 'darwin':
        return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    return 'libreoffice'


class LibreOfficeError(Exception):
    def __init__(self, output):
        self.output = output


