import ast
from enum import Enum

class Errors(Enum):
    Function_length_is_longer_then_20 = 0
    There_are_unused_variables = 1
    Function_has_no_documentation_string = 2
    File_length_is_longer_then_200 = 3

class MyVisitor(ast.NodeVisitor):
    def __init__(self,code):
        self.source_lines = code.splitlines()
        self.lengths = []
        self.used_globals = 0
        self.assigned_globals = 0
        self.errors = [0,0,0,0]
        self.visit(ast.parse(code))

    def visit_FunctionDef(self,node):
        length = self.get_function_length(node)
        self.lengths.append(length)
        if length > 20:
            self.errors[Errors.Function_length_is_longer_then_20.value] += 1
        if not ast.get_docstring(node):
            self.errors[Errors.Function_has_no_documentation_string.value] += 1
        assigned_vars = set()
        used_vars = set()
        for subNode in ast.walk(node):
            if isinstance(subNode, ast.Name):
                if isinstance(subNode.ctx, ast.Store):
                    assigned_vars.add(subNode.id)
                elif isinstance(subNode.ctx, ast.Load):
                    used_vars.add(subNode.id)
        unused = assigned_vars - used_vars
        self.errors[Errors.There_are_unused_variables.value] += len(unused)
        self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(getattr(node, 'parent', None), ast.Module):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.assigned_globals += 1
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.used_globals += 1
        self.generic_visit(node)

    def get_unused_globals(self):
        self.errors[Errors.There_are_unused_variables.value] += self.assigned_globals - self.used_globals
    def get_function_length(self,func_node):
        start = func_node.lineno - 1
        end = max(n.lineno for n in ast.walk(func_node) if hasattr(n, 'lineno'))
        lines = self.source_lines[start:end]

        if ast.get_docstring(func_node):
            doc_node = func_node.body[0]
            if isinstance(doc_node, ast.Expr) and isinstance(doc_node.value, ast.Str):
                doc_start = doc_node.lineno - 1
                doc_end = doc_node.end_lineno or doc_node.lineno
                lines = lines[:doc_start - start] + lines[(doc_end - start):]

        clean_lines = [line for line in lines if line.strip() and not line.strip().startswith("#")]
        return len(clean_lines)
def add_parents(tree):
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node