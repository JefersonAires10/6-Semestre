import os
import zipfile

def process_file(file_path):
    # Abre o arquivo para leitura
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Remove linhas em branco
    non_empty_lines = [line for line in lines if line.strip() != '']
    # Conta o número de palavras em cada linha não vazia
    word_count = sum(len(line.split()) for line in non_empty_lines)
    # Conta o número de caracteres em cada linha não vazia
    char_count = sum(len(line) for line in non_empty_lines)
    
    return word_count, char_count

def main():
    input_directory = 'textos'  
    results_directory = 'results'  
    output_file = os.path.join(results_directory, 'consolidado.txt')  
    zip_file = os.path.join(results_directory, 'saida.zip') 
    
    os.makedirs(results_directory, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(input_directory):
            if filename.endswith('.txt'):  
                file_path = os.path.join(input_directory, filename)
                word_count, char_count = process_file(file_path)  
                outfile.write(f'{filename}: {word_count} palavras, {char_count} caracteres\n')
    
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        zipf.write(output_file, os.path.basename(output_file))

if __name__ == '__main__':
    main()  