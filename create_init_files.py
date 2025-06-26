import os

def add_init_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "__init__.py" not in filenames:
            init_file = os.path.join(dirpath, "__init__.py")
            with open(init_file, "w") as f:
                pass  # create empty file
            print(f"Created: {init_file}")
        else:
            print(f"Already exists: {os.path.join(dirpath, '__init__.py')}")

# Update this path to match your project's test root
project_root = r"C:\SkillWright\AutomationTesting\Test_FYC"
add_init_files(project_root)
