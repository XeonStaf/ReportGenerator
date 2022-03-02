import subprocess

from config import *
from get_code import code_to_latex
from get_description import get_description_lab


if __name__ == '__main__':
    with open('template.tex') as template_file:
        global latex_code
        latex_code = template_file.read()
    filename = f'report_{LAB_NUM}.tex'
    with open(filename, 'w') as latex_file:
        latex = latex_code.replace(r'\var{FIO}', NAME)
        latex = latex.replace(r'\var{GROUP}', GROUP)
        latex = latex.replace(r'\var{CHECKER}', CHECKING)
        latex = latex.replace(r'\var{TASK}', '\n\\\\'.join(get_description_lab(LAB_NUM)))
        latex = latex.replace(r'\var{SOLUTION}', code_to_latex())
        latex = latex.replace(r'\var{LAB_NUM}', str(LAB_NUM))
        latex_file.write(latex)
    print(f'Latex File {filename} generated')
    if GENERATE_PDF:
        subprocess.call(['latexmk', '-pdf', filename])
    else:
        print("Now you have to generate pdf from .tex file")
        print("For example use http://overleaf.com")



