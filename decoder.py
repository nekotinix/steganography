import mtk_2_codec
codecs = [ "cp866", "koi8_r","cp1252"]
import docx
import os
paths = []
folder = os.getcwd()
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('docx') and not file.startswith('~'):
            paths.append(os.path.join(root, file))
for path in paths:
    doc = docx.Document('pun12.docx')
for codec in codecs:
    with open('1.txt', "r", encoding=codec,errors="ignore") as file:
        text = file.read()
    print(codec.rjust(12), "|", text)
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

