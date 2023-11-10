import pypandoc

input_file = "README.md"
output_file = "README.pdf"

pypandoc.convert_file(input_file, "pdf", outputfile=output_file)
