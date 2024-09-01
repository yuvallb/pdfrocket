from pdfrw import PdfReader, PdfWriter

def merge_pdfs(pdf_list, output_path):
    pdf_writer = PdfWriter()
    for pdf in pdf_list:
        pdf_reader = PdfReader(pdf)
        pdf_writer.addpages(pdf_reader.pages)
    pdf_writer.write(output_path)

if __name__ == "__main__":
    pdf_files = ['test1.pdf', 'test2.pdf']
    output_file = 'merged_output.pdf'
    
    merge_pdfs(pdf_files, output_file)
    print(f"PDFs merged into {output_file}")
