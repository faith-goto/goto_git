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
  addNew = "INSERT INTO res (name, jpn, math, eng, sci, created, modified) VALUES ('#{new_name}','#{new_jpn}','#{new_math}','#{new_eng}','#{new_sci}',now(),now());"
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
results = client.query("SELECT * FROM first;").each do |f_data|
  id.push(f_data["id"])
  name.push(f_data["name"])
  jpn.push(f_data["jpn"])
  math.push(f_data["math"])
  eng.push(f_data["eng"])
  sci.push(f_data["sci"])
  created.push(f_data["created"])
  modified.push(f_data["modified"])
end


kojin_id = []
kojin_name = []
kojin_sex =[]

res_kojin = client.query("SELECT * FROM kojin;").each do |k_data|
  kojin_id.push(k_data["id"])
  kojin_name.push(k_data["name"])
  kojin_sex.push(k_data["sex"])
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

#指定したユーザのテスト結果を返す(脳筋)
if cgi["onlytest"] != "" then
	strdata = cgi["onlytest"]
  sel_id =[]
  sel_name =[]
  sel_jpn = []
  sel_math = []
  sel_eng = []
  sel_sci = []
  sel_created = []
  sel_modified = []

  #SELECTでユーザ取得
  selUser = client.query("SELECT * FROM first WHERE name='"+strdata+"';").each do |c_data|
    sel_id.push(c_data["id"])
    sel_name.push(c_data["name"])
    sel_jpn.push(c_data["jpn"])
    sel_math.push(c_data["math"])
    sel_eng.push(c_data["eng"])
    sel_sci.push(c_data["sci"])
    sel_created.push(c_data["created"])
    sel_modified.push(c_data["modified"])
  end
else
  selUser = []
end

#指定したユーザのテスト結果を返す(ID別)
if cgi["select_id_only"] != "" then
	onlydata = cgi["select_id_only"]
  only_id =[]
  only_name =[]
  only_testname = []
  only_jpn = []
  only_math = []
  only_eng = []
  only_sci = []
  only_soc = []
  only_day = []

  onlyDB = "SELECT kojin.id, kojin.name,all_test.testname,all_test.testday, res_test.jpn, res_test.math, res_test.eng, res_test.sci,res_test.soc
  FROM (kojin INNER JOIN res_test ON kojin.id = res_test.id)
  INNER JOIN all_test
  ON all_test.id = res_test.id_test
  AND kojin.id ='#{onlydata}';"

  onlyUser = client.query(onlyDB).each do |d_data|
    only_id.push(d_data["id"])
    only_name.push(d_data["name"])
    only_testname.push(d_data["testname"])
    only_day.push(d_data["testday"])
    only_jpn.push(d_data["jpn"])
    only_math.push(d_data["math"])
    only_eng.push(d_data["eng"])
    only_sci.push(d_data["sci"])
    only_soc.push(d_data["soc"])
  end
  onlystr = "ID:#{onlydata}      #{only_name[0]} の全テストデータ"
else
  onlyUser = []
  onlystr = "複数テーブルを用いたユーザのテスト結果(同性同名分けるよVer)"
end



print "Content-type: text/html\n\n"

print <<EOM
<html>
<head>
<meta http-equiv="Content-type" content="text/html; charset=euc-jp">
<title>検索フォーム</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

<a href='./test.cgi'>複数データ管理</a>
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
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
</form>
<form id="deldata" method="post">
  <p>削除したいユーザーID：
    <input type="number" name="deluser" min=0>
    <button type="submit" name="del_button">送信</button>
  </p>

<p>＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊</p>
</form>
<form method="GET">
<button type="button" onclick="showall()">ユーザ一覧表示</button>
<table id='alluser' border=1 style='display:none'>
<tr>
<th>id</th><th>名前</th><th>国語</th><th>数学</th><th>英語</th><th>理科</th><th>作成</th><th>修正</th>
</tr>
EOM

i = results.count
for i in 0..i -1
  puts ("<tr name='i'>")
  puts ("<input type='hidden' name='param' value='#{id[i]}'>")
  puts ("</form>")
  puts ("<td>#{id[i]}</td><td>#{name[i]}</td><td>#{jpn[i]}</td><td>#{math[i]}</td><td>#{eng[i]}</td><td>#{sci[i]}</td><td>#{created[i]}</td><td>#{modified[i]}</td><td><a href='./change.cgi?id=#{id[i]}'>編集</a></td>")
  puts ("</tr>")
end

print <<EOM
</table>
<p>＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊</p>

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

＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
<p>ユーザそれぞれの合計点</p>
<table id='sumuser' border=1>
<tr>
<th>name</th><th>合計点</th>
</tr>

EOM

for i in 0..i -1
  puts ("<tr>")
  puts ("<td>#{name_sum[i]}</td><td>#{test_sum[i]}</td>")
  puts ("</tr>")
end

print <<EOM
</table>

<p>＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊</p>

<form id='select_user' method='POST'>
<p>指定ユーザのテスト結果(同性同名同一Ver)
<select name='onlytest'>
EOM

i = results.count
puts ("<option disabled selected>誰のテストデータが見たい？</option>")
for i in 0..i -1
puts ("<option value='#{name[i]}'>#{name[i]}</option>")
end

print <<EOM
  </select>
  <input type="submit" value="検索">
  </p>
  </form>

<table id='catch_seluser' border=1>
<tr>
<th>ID</th><th>名前</th><th>国語</th><th>数学</th><th>英語</th><th>理科</th>
</tr>
EOM


k = selUser.count
for k in 0..k -1
  puts ("<tr>")
  puts ("<td>#{sel_id[k]}</td><td>#{sel_name[k]}</td><td>#{sel_jpn[k]}</td><td>#{sel_math[k]}</td><td>#{sel_eng[k]}</td><td>#{sel_sci[k]}</td>")
  puts ("</tr>")
end

print <<EOM
</table>
<p></p>
＊＊＊＊＊＊＊＊＊＊＊以下、複数テーブルにおけるデータ管理＊＊＊＊＊＊＊＊＊＊
<form id='select_user_only' method='POST'>
<p>#{onlystr}
<select name='select_id_only'>
EOM

i = res_kojin.count
puts ("<option disabled selected>誰のテストデータが見たい？</option>")
for i in 0..i -1
puts ("<option value='#{kojin_id[i]}'>#{kojin_id[i]}:#{kojin_name[i]}</option>")
end


print <<EOM
</select>
<input type="submit" value="検索">
</p>
</form>
<table id='catch_user_only' border=1>
<tr>
<th>テスト名</th><th>テスト実施日</th><th>国語</th><th>数学</th><th>英語</th><th>理科</th><th>社会</th>
</tr>
EOM

k = onlyUser.count
for k in 0..k -1
  puts ("<tr>")
  puts ("<td>#{only_testname[k]}</td><td>#{only_day[k]}</td><td>#{only_jpn[k]}</td><td>#{only_math[k]}</td><td>#{only_eng[k]}</td><td>#{only_sci[k]}</td><td>#{only_soc[k]}</td>")
  puts ("</tr>")
end

print <<EOM
</table>

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
