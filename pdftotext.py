import subprocess

def convert_pdf_to_tex(pdf_path, tex_path):
	try:
    	# Use pdf2tex command-line tool to convert PDF to TeX
    	subprocess.run(['pdftotex', pdf_path, tex_path], check=True)
    	print(f"Converted {pdf_path} to {tex_path}")
	except subprocess.CalledProcessError as e:
    	print(f"Error occurred while converting {pdf_path} to {tex_path}: {e}")

# Example usage
path = input("Insira o nome do arquivo: ")
pdf_path = f'/home/nera/Pdfs/{path}'  # Replace with the path to your PDF file
tex_path = '/home/nera/Pdfs'  # Replace with the desired path for the resulting TeX file

convert_pdf_to_tex(pdf_path, tex_path)
