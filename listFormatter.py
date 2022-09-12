#format lists to '', '', '', '',...
import re
import pyperclip as ppc

def main():
    list = ppc.paste()
    elmt = re.compile(r'\w+')
    formatted = elmt.findall(list)
    final = str(formatted)
    ppc.copy(final.lower())
    
main()