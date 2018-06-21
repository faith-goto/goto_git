#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require "mysql2"

print "Content-type: text/html\n\n"

#インスタンスを生成し、id変数にindexから受け取った編集したいidを格納
cgi = CGI.new
cth_id = cgi["id"]

#DB接続
client = Mysql2::Client.new(host: "localhost", username: "goto", password: "", database: "goto_practice")

#データベースの値を取得するためのやーつら
c_id = []
c_name = []
c_jpn = []
c_math = []
c_eng = []
c_sci = []
c_created = []
c_modified = []

#編集したいIDのデータを個々に取得する
client.query("SELECT * FROM first WHERE id=" + cth_id).each do |f_data|
  c_id.push(f_data["id"])
  c_name.push(f_data["name"])
  c_jpn.push(f_data["jpn"])
  c_math.push(f_data["math"])
  c_eng.push(f_data["eng"])
  c_sci.push(f_data["sci"])
  c_created.push(f_data["created"])
  c_modified.push(f_data["modified"])
end

id = cgi["id"]
name = cgi["name"]
jpn = cgi["jpn"]
math = cgi["math"]
eng = cgi["eng"]
sci = cgi["sci"]

if name != "" || jpn != "" || math != "" || eng!= "" || sci!="" then
  c_id[0] = id
  c_name[0] = name
  c_jpn[0] = jpn
  c_math[0] = math
  c_eng[0] = eng
  c_sci[0] = sci
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
<form id="updata" action="/change.cgi" method="POST">
<table class="change_User" border=1>
<tr>
  <th>ID:#{id}</th>
  <td><input type="hidden" name="id" value="#{id}"></td>
</tr>
<tr>
  <th>名前:</th>
  <td><input type="text" name="name" value="#{c_name[0]}" required></td>
</tr>
<tr>
  <th>国語:</th>
  <td><input type="number" name="jpn" value="#{c_jpn[0]}" min=0 max=100 required></td>
</tr>
<tr>
  <th>数学:</th>
  <td><input type="number" name="math" value="#{c_math[0]}" min=0 max=100 required></td>
</tr>
<tr>
  <th>英語:</th>
  <td><input type="number" name="eng" value="#{c_eng[0]}" min=0 max=100 required></td>
</tr>
<tr>
  <th>理科:</th>
  <td><input type="number" name="sci" value="#{c_sci[0]}" min=0 max=100 required></td>
</tr>
</table>
<button type="submit" name="update_user" value="changebtn" onclick="location.reload();">修正</button>
</form>
<input type="button" value="戻る" onclick="window.location.href='http://10.172.81.244:510/'">

<script type="text/javascript">
function disp(){

	// 「OK」時の処理開始 ＋ 確認ダイアログの表示
	if(window.confirm('修正してよろしいですか？')){
  $("#af_jpn").html('a');
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

if cth_id == "" then
 cth_id = cgi["id"]
else
end

addup="UPDATE first SET jpn=#{jpn}, math=#{math}, eng=#{eng}, sci=#{sci} WHERE id=#{cth_id};"
client.query(addup)
