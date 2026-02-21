class DocstringGenerator:

    def generate(self, function_name):
        doc = f'''"""
{function_name} function.

Parameters:
    None

Returns:
    None
"""'''
        return doc
