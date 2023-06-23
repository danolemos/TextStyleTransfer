import subprocess
import re

def remove_tex_symbols(text):
	# Define regular expressions for LaTeX symbols and constructions
	tex_patterns = [
    	# Remove LaTeX symbols and constructions
    	(r'\\[^\s]+', ''),  # Remove LaTeX commands starting with '\'
    	(r'\$[^\$]+\$', ''),  # Remove inline math expressions: $...$
    	(r'\$\$[^\$]+\$\$', ''),  # Remove displayed math expressions: $$...$$
    	(r'\\begin\{[^\}]+\}.*?\\end\{[^\}]+\}', ''),  # Remove \begin{...}...\end{...}
    	(r'\\[a-zA-Z]+\{\}', ''),  # Remove other LaTeX commands: \command{}
    	(r'\b\d+\b', ''),  # Remove numbers
    	(r'\\[a-zA-Z]+\b', ''),  # Remove Greek symbols (alpha, beta, gamma, etc.)
	]

	# Remove LaTeX symbols, numbers, and Greek symbols using regular expressions
	for pattern, replacement in tex_patterns:
    		text = re.sub(pattern, replacement, text, flags=re.DOTALL)

		# Remove leading and trailing spaces from each line
		text = re.sub(r'^\s+|\s+$', '', text, flags=re.MULTILINE)

	# Remove multiple spaces and replace with a single space
	text = re.sub(r'\s+', ' ', text)

	# Remove non-Latin characters and punctuation
	text = re.sub(r'[^a-zA-Z\s]', '', text)

	return text

def convert_pdf_to_text(pdf_path, text_path):
try:
    		# Use pdftotext command-line tool to convert PDF to text
    		subprocess.run(['pdftotext', '-layout', pdf_path, text_path], check=True)
    		print(f"Converted {pdf_path} to {text_path}")

    		# Read the converted text file
    		with open(text_path, 'r') as file:
        			text = file.read()

    		# Remove LaTeX symbols, numbers, Greek symbols, and clean up the text
    		text = remove_tex_symbols(text)

    		# Write the modified text back to the file
    		with open(text_path, 'w') as file:
        			file.write(text)

    		print(f"Removed LaTeX symbols, numbers, Greek symbols, and cleaned up {text_path}")
	except subprocess.CalledProcessError as e:
    		print(f"Error occurred while converting {pdf_path} to {text_path}: {e}")

# Example usage
pasta = '/home/nera/Pdfs'
entries = os.listdir(pasta)

for elem in entries:
text_path = f'{elem}.txt'
	convert_pdf_to_text(elem, text_path)
