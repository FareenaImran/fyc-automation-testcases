import os

def generate_tree(start_path, output_file):
    """Generate directory tree structure"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('Folder PATH listing\n')
        f.write('Volume serial number is ...\n\n')
        
        for root, dirs, files in os.walk(start_path):
            level = root.replace(start_path, '').count(os.sep)
            indent = '|   ' * level
            f.write(f'{indent}+---{os.path.basename(root)}\n')
            subindent = '|   ' * (level + 1)
            for file in files:
                f.write(f'{subindent}{file}\n')

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(__file__))
    output_path = os.path.join(os.path.dirname(__file__), 'structure.txt')
    generate_tree(base_path, output_path)
