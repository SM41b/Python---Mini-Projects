from PyPDF2 import PdfMerger

merger = PdfMerger()
try:
    num = int(input('Enter number of pdfs you want to merge : '))

    for i in range(num):
        pdf_file = input(f'Enter name of PDF {i+1} : ')
        try:
            merger.append(pdf_file)
        except:
            print(f'Could not open {pdf_file}!')

    output = input('Enter name of merged pdf : ')

    merger.write(output)

    merger.close()
    print('Yayyy!!!PDF merged successfully;)')
except:
    print('Something went wrong!')