#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require "mysql2"

#インスタンスを生成し、table変数に格納
cgi = CGI.new
table = cgi['table']

#DB接続
client = Mysql2::Client.new(host: "localhost", username: "goto", password: "", database: "goto_practice")

#新規追加ユーザ
new_name = cgi["namedata"]
new_jpn = cgi["jpnval"]
new_math = cgi["mathval"]
new_eng = cgi["engval"]
new_sci = cgi["scival"]

if cgi["namedata"] != "" then
  addNew = "INSERT INTO first (name, jpn, math, eng, sci, created, modified) VALUES ('#{new_name}','#{new_jpn}','#{new_math}','#{new_eng}','#{new_sci}',now(),now());"
  client.query(addNew)
  cgi["namedata"].clear
  print cgi.header( {
  "status"     => "REDIRECT",
  "Location"   => "http://10.172.81.244:510/"
})
else
  checkName = '<p>名前を入力してください</p>'
end

#データベースの値を取得するためのやーつら
id = []
name = []
jpn = []
math = []
eng = []
sci = []
created = []
modified = []

#全員表示
results = client.query("SELECT * FROM first").each do |f_data|
  id.push(f_data["id"])
  name.push(f_data["name"])
  jpn.push(f_data["jpn"])
  math.push(f_data["math"])
  eng.push(f_data["eng"])
  sci.push(f_data["sci"])
  created.push(f_data["created"])
  modified.push(f_data["modified"])
end

#指定したユーザのテスト結果を返す
if cgi["onlytest"] != "" then
	strdata = "<p>" +  cgi["onlytest"] + "</p>"
else
	strdata = '<p>誰のテスト結果が見たい？</p>'
end

#指定したIDのユーザデータ削除
del_user = cgi["deluser"]
    delcom = "DELETE FROM first WHERE id = '#{del_user}';"
    client.query(delcom)


#合計点求めたい
id_sum = []
name_sum = []
test_sum = []
#合計点
addSUM = "select id, name, jpn + math + eng + sci from first;"
getSUM = client.query(addSUM).each do |a_data|
  id_sum.push(a_data["id"])
  name_sum.push(a_data["name"])
  test_sum.push(a_data["jpn + math + eng + sci"])
end

#平均点を求めたい
jpn_avg =[]
math_avg =[]
eng_avg =[]
sci_avg =[]
#平均点
addAVG = "SELECT AVG(jpn),AVG(math),AVG(eng),AVG(sci) FROM first;"
get_AVG = client.query(addAVG).each do |b_data|
  jpn_avg.push(b_data["AVG(jpn)"])
  math_avg.push(b_data["AVG(math)"])
  eng_avg.push(b_data["AVG(eng)"])
  sci_avg.push(b_data["AVG(sci)"])
end



print "Content-type: text/html\n\n"

print <<EOM
<html>
<head>
<meta http-equiv="Content-type" content="text/html; charset=euc-jp">
<title>検索フォーム</title>

</head>
<body>
<h3>ユーザ追加フォーム</h2>
<form id="senddata1" method="POST">
  <table class="newUser">
  <tr>
    <th>名前:</th>
    <td><input type="text" name="namedata" value="" required></td>
  </tr>
  <tr>
    <th>国語:</th>
    <td><input type="number" name="jpnval" min=0 max=100 required></td>
  </tr>
  <tr>
    <th>数学:</th>
    <td><input type="number" name="mathval" min=0 max=100 required></td>
  </tr>
  <tr>
    <th>英語:</th>
    <td><input type="number" name="engval" min=0 max=100 required></td>
  </tr>
  <tr>
    <th>理科:</th>
    <td><input type="number" name="scival" min=0 max=100 required></td>
  </tr>
  </table>
  <button type="submit" name="newcreate">送信</button>
  #{checkName}
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
</form>
<form id="deldata" method="post">
  <p>削除したいユーザーID：
  <input type="number" name="deluser" min=0>
  <button type="submit" name="del_button">送信</button>
  </p>

<p>＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊</p>
</form>
<form method="GET">
<button type="button" onclick="showall()">ユーザ一覧表示</button>
EOM
puts ("<table id='alluser' border=1 style='display:none'>")
puts ("<tr>")
puts ('<th>id</th><th>name</th><th>jpn</th><th>math</th><th>eng</th><th>sci</th><th>created</th><th>modified</th>')
puts ("</tr>")
i = results.count
for i in 0..i -1
  puts ("<tr name='i'>")
  puts ("<form name='send_userlog' action='./change.cgi' method='post'>")
  puts ("<input type='hidden' name='param' value='#{id[i]}'>")
  puts ("</form>")
  puts ("<td>#{id[i]}</td><td>#{name[i]}</td><td>#{jpn[i]}</td><td>#{math[i]}</td><td>#{eng[i]}</td><td>#{sci[i]}</td><td>#{created[i]}</td><td>#{modified[i]}</td><td><a href='./change.cgi?id=#{id[i]}'>編集</a></td>")
  puts ("</tr>")
end
puts ("</table>")
puts ("<p>＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊</p>")
puts ("<p>指定ユーザのテスト結果")
puts ("<select name='onlytest'>")
i = results.count
for i in 0..i -1
puts ("<option value='#{name[i]}さんのテスト結果ーー>国語：#{jpn[i]}　数学：#{math[i]}　英語：#{eng[i]}　理科：#{sci[i]}'>#{name[i]}</option>")
#puts ("<option value='#{id[i]}'>#{name[i]}</option>")
end

print <<EOM
  </select>
  <input type="submit" value="検索">
  #{strdata}
</p>
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
<p>ユーザそれぞれの合計点</p>
EOM
puts ("<table id='sumuser' border=1>")
puts ("<tr>")
puts ('<th>name</th><th>合計点</th>')
puts ("</tr>")
for i in 0..i -1
  puts ("<tr>")
  puts ("<td>#{name_sum[i]}</td><td>#{test_sum[i]}</td>")
  puts ("</tr>")
end
puts ("</table>")
print <<EOM

<p>各教科の平均点</p>
<table id='avguser' border=1>
<tr>
  <td>教科</td><td>平均点</td>
</tr>
<tr>
  <td>国語</td><td>#{jpn_avg[0].floor}</td>
</tr>
<tr>
  <td>数学</td><td>#{math_avg[0].floor}</td>
</tr>
<tr>
  <td>英語</td><td>#{eng_avg[0].floor}</td>
</tr>
<tr>
  <td>理科</td><td>#{sci_avg[0].floor}</td>
</tr>
</table>

</form>
<script type="text/javascript">
function showall(){
  var showuser = document.getElementById("alluser");
  if(showuser.style.display=="block"){
		// noneで非表示
		showuser.style.display ="none";
	}else{
		// blockで表示
		showuser.style.display ="block";
	}
}

</script>
</body>
</html>
EOM
