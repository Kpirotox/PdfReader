from PyPDF2 import PdfFileReader

infile = "Abadia.pdf"
pdf_reader = PdfFileReader(open(infile, "rb"))



with open('destino.txt','w',encoding='utf-8') as arquivo:
    for i in range(0, 1000):
        print("Campo " + str(i+1))
        # page = pdf_reader.getPage(i)
        # print(page.extractText())
        dicionario = pdf_reader.getFields()
        
        print(dicionario)

        # for x in range(0, len(dicionario)):
        #     print(dicionario[x] + '\n')
            
        # arquivo.write(page.extractText())

