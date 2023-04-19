import docx

doc = docx.Document('example1.docx')
for para in doc.paragraphs:
    for run in para.runs:
        if run.font.color.rgb == docx.shared.RGBColor(255, 0, 0):
            #run.text='0'
            print(run.text)
        else:
            print(run.text)
