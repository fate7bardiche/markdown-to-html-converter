import markdown
import sys
from validate import validate
from io_utils import writeFlush
from path import expandPath


def main():
    command_args  = sys.argv
    validate(command_args)

    markdown_file_path = command_args[2]
    output_file_path = command_args[3]

    markdown_contents = ""
    with open(expandPath(markdown_file_path)) as markdown_file:
        markdown_contents = markdown_file.read()

    html = markdown.markdown(markdown_contents)

    with open(expandPath(output_file_path), "w") as f:
        f.write(html)

    writeFlush(f"{markdown_file_path}をMarkdownからHTMLに変換し、{output_file_path}に保存しました")
  
if __name__ == "__main__":
   main()