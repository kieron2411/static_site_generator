from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        if block != "":
            blocks.append(block.strip())
    return blocks

def block_to_block_type(block):
    #check for headings
    count = 0
    for i in range(6):
        if block[i] == "#":
            count += 1
        else:
            break
    if 1 <= count <= 6 and block[count] == " ":
        return BlockType.HEADING
    
    #check for code block
    if block[0:4] == "```\n" and block[-3:] == "```":
        return BlockType.CODE
    
    #check for quote block
    lines = block.split("\n")
    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    
    #check for unordered list
    is_un_list = True
    for line in lines:
        if not line.startswith("- "):
            is_un_list = False
            break
    if is_un_list:
        return BlockType.UNORDERED_LIST
    
    #check for ordered list
    is_list = True
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i + 1}. "):
            is_list = False
            break
    if is_list:
        return BlockType.ORDERED_LIST
    
    #if none of above then paragraph
    return BlockType.PARAGRAPH