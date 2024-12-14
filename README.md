# markdown-to-html-converter
## 概要
本プロジェクトは、Markdownで記載されたドキュメントをHTMLに変換するスクリプトです。

## 使用方法
```
$ python3 file-converter.py markdown doc/input_markdown.md doc/output_html.html
```

- 実行ファイル: file-converter.py
- 第一引数: コマンドです。現在markdownのみです。
- 第二引数: 入力ファイル名です。、拡張子がmdである必要があります。
- 第三引く数: 変換したhtmlを保存したいファイル名です。拡張子は問いません。