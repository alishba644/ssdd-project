import ast

def sast_scan(file_path):
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    issues = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if hasattr(node.func, 'id') and node.func.id == "eval":
                issues.append("Unsafe eval detected")

    return issues
    