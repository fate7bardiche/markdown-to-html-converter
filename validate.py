from io_utils import writeFlush, flushError

def validate(command_args):
    validateArgsLength(command_args)
    validateCommand(command_args)
    validateMarkdownExtention(command_args)
      
# 引数の個数を検証
def validateArgsLength(command_args):
    length = len(command_args)
    if(length < 4):
        flushError(f"引数が{4 - length}個足りません")

# 指定されたコマンドがmarkdownであることを検証
def validateCommand(command_args):
    command = command_args[1]
    if(not command == "markdown"):
        flushError(f"{command}コマンドは存在しません。markdownコマンドを入力してください")

# Markdownファイルの拡張子がmdであることを検証
def validateMarkdownExtention(command_args):
    markdown_file_path = command_args[2]
    lastDotIndex = f"{markdown_file_path}".rfind(".")
    extention = markdown_file_path[lastDotIndex + 1:]
    writeFlush(extention)
    if(not extention == "md"):
        flushError("Markdownファイルは拡張子がmdである必要があります")