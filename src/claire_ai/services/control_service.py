import re
from typing import Tuple
from rich.table import Table
import pyperclip

class ControlService:
    def __init__(self) -> None:
        pass

    def get_code_blocks(self, text: str) -> Tuple[int, str] | Tuple[int, list[str]]:
        if not text.strip():
            raise ValueError("Text value can't be empty.")
        
        code_blocks = re.findall(r'```(.*?)\n(.*?)```', text, flags=re.DOTALL)

        if not code_blocks:
            return -1, text
        
        return len(code_blocks), code_blocks

    def copy_code_block_from_blocks(self, number: int, code_blocks: list[str]):
        if not code_blocks:
            raise ValueError("Code blocks can't be empty.")
        if not (number > 0 and number <= len(code_blocks)):
            raise ValueError("Number can't be negative or outside the length of code blocks.")
        
        block = code_blocks[number - 1]
        if block:
            if len(block) == 2:
                block = block[1]
            pyperclip.copy(block)
            return 200

    def copy_text(self, text: str):
        if text.strip() == "":
            raise ValueError("Text value can't be empty.")
        
        pyperclip.copy(text)
        return 200

    def get_table_code_blocks(self, code_blocks: list[str]):
        table = Table(show_lines=True)
        table.add_column("Index", justify="center", no_wrap=True)
        table.add_column("Code Block")

        data: list[list[str, str]] = []
        for i, block in enumerate(code_blocks):
            if not block:
                continue

            if len(block) > 1:
                block = block[1]
            else:
                block = block[0]

            data.append(
                [
                    str(i + 1), f"{block[:100]}\n(...)"
                ] 
            )

        for row in data:
            table.add_row(*row)
        
        return table