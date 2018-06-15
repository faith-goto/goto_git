#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require "mysql2"

#インスタンスを生成し、table変数に格納
cgi = CGI.new
table = cgi['table']

#DB接続
client = Mysql2::Client.new(host: "localhost", username: "goto", password: "", database: "goto_practice")


arr = []
#arr配列にデータベースの値を格納。
client.query("SELECT * FROM first").each do |row|
 arr.push(row)
end



if cgi["textdata"] != "" then
	strdata = '<p>' + cgi["textdata"] + '</p>'
else
	strdata = '<p>未入力です</p>'
end

print "Content-type: text/html\n\n"

greeting = "Hello Goto"

print <<EOM
<html>
<head>
<meta http-equiv="Content-type" content="text/html; charset=euc-jp">
<title>検索フォーム</title>
</head>
<body>
<h2>検索フォーム</h2>
<form method="GET">
	<p>テーブル名:
  <select name="data1">
	<option value="user">user</option>
	<option value="organization">organization</option>
	<option value="first">first</option>
	</select>
  </p>

	<p>ID:<input type="number" min="1" name="data2"></p>
  <input type="text" name="textdata" value="">
	<input type="submit" value="入力文字を表示">
  	#{strdata}

	<p><input type="submit" value="検索"></p>
  <button type="button">ユーザ一覧表示</button>
  #{arr}
  #{table}
</form>

</body>
</html>
EOM
