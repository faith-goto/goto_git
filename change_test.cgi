#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require "mysql2"

print "Content-type: text/html\n\n"

#インスタンスを生成し、id変数にindexから受け取った編集したいidを格納したい

cgi = CGI.new
id = cgi["id"]
name=cgi["name"]
testname = cgi["testname"]
testday = cgi["testday"]
jpn = cgi["jpn"]
math = cgi["math"]
eng = cgi["eng"]
sci = cgi["sci"]
soc = cgi["soc"]
#テスト種目のID種痘
test_id = []

#DB接続
client = Mysql2::Client.new(host: "localhost", username: "goto", password: "", database: "goto_practice")

#all_testテーブルの要素取得
all_test_id = []
all_test_testname = []
all_test_testday = []

res_all_test = client.query("SELECT * FROM all_test;").each do |t_data|
  all_test_id.push(t_data["id"])
  all_test_testname.push(t_data["testname"])
  all_test_testday.push(t_data["testday"])
end

i = res_all_test.count
for i in 0..i -1
  if testname == all_test_testname[i] then
    test_id = all_test_id[i]
  end
end

print <<EOM
<html>
<head>
<meta http-equiv="Content-type" content="text/html; charset=euc-jp">
<title>修正フォーム</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
</head>

<body>
<h1>修正フォーム</h1>
<form id="updata" action="/change_test.cgi" method="POST">
<table class="change_User" border=1>
<tr>
  <th>ID:#{id}</th>
  <td><input type="hidden" name="id" value="#{id}"></td>
</tr>
<tr>
  <th>名前:</th>
  <td><input type="text" name="name" value="#{name}" required></td>
</tr>
<tr>
  <th>テスト種目:</th>
  <td><input type="text" name="testname" value="#{testname}" required></td>
</tr>
<tr>
  <th>実施日:</th>
  <td><input type="text" name="testday" value="#{testday}" required></td>
</tr>
<tr>
  <th>国語:</th>
  <td><input type="number" name="jpn" value="#{jpn}" min=0 max=100 required></td>
</tr>
<tr>
  <th>数学:</th>
  <td><input type="number" name="math" value="#{math}" min=0 max=100 required></td>
</tr>
<tr>
  <th>英語:</th>
  <td><input type="number" name="eng" value="#{eng}" min=0 max=100 required></td>
</tr>
<tr>
  <th>理科:</th>
  <td><input type="number" name="sci" value="#{sci}" min=0 max=100 required></td>
</tr>
<tr>
  <th>社会:</th>
  <td><input type="number" name="soc" value="#{soc}" min=0 max=100 required></td>
</tr>
</table>
<button type="submit" name="update_user" value="changebtn" onclick="location.reload();">修正</button>
</form>
<input type="button" value="戻る" onclick="window.location.href='http://10.172.81.244:510/test.cgi'">
</body>
</html>
EOM

addup="UPDATE res_test SET jpn=#{jpn}, math=#{math}, eng=#{eng}, sci=#{sci}, soc=#{soc} WHERE id=#{id} AND name='#{name}' AND id_test=#{test_id};"
client.query(addup)
