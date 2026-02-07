import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks2(self):
        md = """
This is a paragraph


This is another paragraph with 2 empty lines instead of 1



This is a final paragraph with 3 empty lines
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph",
                "This is another paragraph with 2 empty lines instead of 1",
                "This is a final paragraph with 3 empty lines"
            ],
        )

    def test_block_type_heading(self):
        block = """
# This is a heading
""".strip()
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING,
        )

    def test_block_type_code(self):
        block = """
```
This is some code
```
""".strip()
        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE
        )

    def test_block_type_quote(self):
        block = """
> This is a quote
> This is another line of quotation
> And one more line
""".strip()
        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE
        )
    
    def test_block_type_unordered(self):
        block = """
- This is a list item
- This is another list item
- And one more too
""".strip()
        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST
        )

    def test_block_type_ordered(self):
        block = """
1. This is an ordered list item
2. This is the second item
3. This is the third item
""".strip()
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )

    def test_block_type_paragraph(self):
        block = """
#This is a broken heading and so will display as a paragraph type
""".strip()
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )