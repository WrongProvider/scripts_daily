import os
from PyPDF2 import PdfMerger


def merge_pdfs(input_folder, output_pdf):
    pdf_merger = PdfMerger()


    # Lista todos os arquivos na pasta
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            filepath = os.path.join(input_folder, filename)
            print(f"Adicionando {filename} ao PDF final.")
            with open(filepath, 'rb') as pdf_file:
                pdf_merger.append(pdf_file)
   
    # Escreve o PDF final
    with open(output_pdf, 'wb') as output_file:
        pdf_merger.write(output_file)


    print(f"PDF final gerado: {output_pdf}")


# Exemplo de uso
input_folder = 'C:\\Users\\you\\Documents\\OPENAI\\Kasper\\relatorios'  # Pasta onde estão os PDFs
output_pdf = 'pdf_final.pdf'     # Nome do PDF final


merge_pdfs(input_folder, output_pdf)
