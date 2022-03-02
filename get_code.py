import os

from config import DIR_TO_LAB


def get_all_files():
    filelist = []
    for root, dirs, files in os.walk(DIR_TO_LAB):
        for file in files:
            if file.endswith(".java"):
                filelist.append(os.path.join(root, file))

    return filelist


def get_all_code():
    result = {}
    for file in get_all_files():
        with open(file) as code:
            filename = os.path.basename(file)
            result[filename] = code.read()
    return result


def code_to_latex():
    result = ""
    data = get_all_code()
    for key in data:
        result += '\n\\newpage'
        result += "\n\\begin{lstlisting}[label=listing1, caption=" + key + "]\n"
        result += str(data[key])
        result += '\end{lstlisting}'
    return result




