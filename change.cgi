#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require "mysql2"

print "Content-type: text/html\n\n"
print "test"
#インスタンスを生成し、id変数にindexから受け取った編集したいidを格納
cgi = CGI.new
cth_id = cgi["id"]
if cth_id == "" then
 cth_id = cgi["id"]
end


#DB接続
client = Mysql2::Client.new(host: "localhost", username: "goto", password: "", database: "goto_practice")

#データベースの値を取得するためのやーつら
id = []
name = []
jpn = []
math = []
eng = []
sci = []
created = []
modified = []
print "test"
print "cth_id: #{cth_id} /"
#編集したいIDのデータを個々に取得
client.query("SELECT * FROM first WHERE id=" + cth_id).each do |f_data|
  id.push(f_data["id"])
  name.push(f_data["name"])
  jpn.push(f_data["jpn"])
  math.push(f_data["math"])
  eng.push(f_data["eng"])
  sci.push(f_data["sci"])
  created.push(f_data["created"])
  modified.push(f_data["modified"])
end
print cth_id
print "test"
update_id = cgi["id"]
update_name = cgi["name_data"]
update_jpn = cgi["jpndata"]
update_math = cgi["mathdata"]
update_eng = cgi["engdata"]
update_sci = cgi["scidata"]



#addup="UPDATE first SET jpn=#{update_jpn.to_i}, math=#{update_math.to_i}, eng=#{update_eng.to_i}, sci=#{update_sci.to_i} WHERE id=#{update_id};"
#client.query(addup)
#addup = "UPDATE first SET jpn=54,math=14,eng=3,sci=2 WHERE id=#{update_id};"
#addup="UPDATE first SET jpn=#{jpn[0]}, math=#{math[0]}, eng=#{eng[0]}, sci=#{sci[0]} WHERE id=#{update_id};"
#client.query(addup)
=begin
if update_name != "" then
  addup = "UPDATE first SET jpn=54,math=14,eng=34,sci=20 WHERE id=150;"
  client.query(addup)
end
=end


print <<EOM
<html>
<head>
<meta http-equiv="Content-type" content="text/html; charset=euc-jp">
<title>修正フォーム</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
</head>

<body>
<h1>修正フォーム</h1>
<form id="updata" action="/change.cgi" method="POST">
<table class="change_User" border=1>
<tr>
  <th>ID:#{id[0]}</th>
  <td><input type="hidden" name="id" value="#{id[0]}"></td>
</tr>
<tr>
  <th>名前:</th>
  <td><input type="text" name="name_data" value="#{name[0]}" required></td>
</tr>
<tr>
  <th>国語:</th>
  <td><input type="number" name="jpndata" value="#{jpn[0]}" min=0 max=100 required></td>
</tr>
<tr>
  <th>数学:</th>
  <td><input type="number" name="mathdata" value="#{math[0]}" min=0 max=100 required></td>
</tr>
<tr>
  <th>英語:</th>
  <td><input type="number" name="engdata" value="#{eng[0]}" min=0 max=100 required></td>
</tr>
<tr>
  <th>理科:</th>
  <td><input type="number" name="scidata" value="#{sci[0]}" min=0 max=100 required></td>
</tr>
</table>
<button type="submit" name="update_user" value="changebtn" onclick="disp()">修正</button>
</form>

<script type="text/javascript">
function disp(){

	// 「OK」時の処理開始 ＋ 確認ダイアログの表示
	if(window.confirm('修正してよろしいですか？')){
      submit();
  $("#updata").html('<input type="button" value="戻る" onclick="history.back()">');

	}
	else{
		window.alert('キャンセルされました'); // 警告ダイアログを表示
	}
	// 「キャンセル」時の処理終了

}
</script>
</body>
</html>
EOM
