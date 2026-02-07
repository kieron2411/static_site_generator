from block_markdown import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
)
from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
)
from convert import text_node_to_html_node           
from inline_markdown import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = block_to_html_node(block, block_type)
        block_nodes.append(block_node)
    return ParentNode("div", block_nodes)

def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def block_to_html_node(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        cleaned = block.replace("\n", " ").strip()
        return ParentNode("p", text_to_children(cleaned))
    elif block_type == BlockType.HEADING:
        count = 0
        for ch in block:
            if ch == "#" and count < 6:
                count += 1
            else:
                break
        text = block[count + 1 :].strip()
        tag = f"h{count}"
        return ParentNode(tag, text_to_children(text))
    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")
        cleanlines = []
        for line in lines:
            line = line[1:].lstrip()
            cleanlines.append(line)
        text = " ".join(cleanlines).strip()
        return ParentNode("blockquote", text_to_children(text))
    elif block_type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        item_nodes = []
        for line in lines:
            cleaned = line[2:].lstrip()
            children = text_to_children(cleaned)
            item_node = ParentNode("li", children)
            item_nodes.append(item_node)
        return ParentNode("ul", item_nodes)
    elif block_type == BlockType.ORDERED_LIST:
        lines = block.split("\n")
        item_nodes = []
        for line in lines:
            cleaned = line.lstrip("0123456789.").lstrip()
            children = text_to_children(cleaned)
            item_node = ParentNode("li", children)
            item_nodes.append(item_node)
        return ParentNode("ol", item_nodes)
    elif block_type == BlockType.CODE:
        code_text = block[4:-3]
        code_node = LeafNode("code", code_text)
        return ParentNode("pre", [code_node])
