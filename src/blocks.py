from enum import Enum
from .helper import markdown_to_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    heading_tuple = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(heading_tuple):
        return BlockType.HEADING

    lines = block.split("\n")
    code_mark = "```"
    if lines[0].startswith(code_mark) and lines[-1].startswith(code_mark):
        return BlockType.CODE
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    if block.startswith("1. "):
        counter = 1
        for line in lines:
            if not line.startswith(str(counter) + ". "):
                return BlockType.PARAGRAPH
            counter += 1
        return BlockType.OLIST
    
    return BlockType.PARAGRAPH