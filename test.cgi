#!/usr/local/bin/ruby


#ライブラリ読み込み
require "cgi"
require "mysql2"


#インスタンスを生成し、table変数に格納
cgi = CGI.new
table = cgi['table']

#DB接続
client = Mysql2::Client.new(host: "localhost", username: "goto", password: "", database: "goto_practice")


print "Content-type: text/html\n\n"

print <<EOM
<html>
  <head>
  <meta http-equiv="Content-type" content="text/html; charset=euc-jp">
  <title>検索フォーム</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script> 

  <a href='./'>TOP</a>
  </head>
  <body>
  <p>Hello</p>
  </body>
</html>
EOM
