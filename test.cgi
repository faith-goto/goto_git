#!/usr/local/bin/ruby


#ライブラリ読み込み
require "cgi"
require "mysql2"


#インスタンスを生成し、table変数に格納
cgi = CGI.new
table = cgi['table']

#DB接続
client = Mysql2::Client.new(host: "localhost", username: "goto", password: "", database: "goto_practice")

#データベースの値を取得するためのやーつら
id = []
name = []
testname = []
testday = []
jpn = []
math = []
eng = []
sci = []
soc = []

all_db_data = "SELECT
kojin.id, kojin.name,all_test.testname,all_test.testday, res_test.jpn, res_test.math, res_test.eng, res_test.sci, res_test.soc
FROM (kojin INNER JOIN res_test ON kojin.id = res_test.id)
INNER JOIN all_test ON all_test.id = res_test.id_test
ORDER BY res_test.id ASC;"

#全員表示
results = client.query(all_db_data).each do |a_data|
  id.push(a_data["id"])
  name.push(a_data["name"])
  testname.push(a_data["testname"])
  testday.push(a_data["testday"])
  jpn.push(a_data["jpn"])
  math.push(a_data["math"])
  eng.push(a_data["eng"])
  sci.push(a_data["sci"])
  soc.push(a_data["soc"])
end

#kojinテーブルの要素を取得
kojin_id = []
kojin_name = []
kojin_sex =[]

res_kojin = client.query("SELECT * FROM kojin;").each do |k_data|
  kojin_id.push(k_data["id"])
  kojin_name.push(k_data["name"])
  kojin_sex.push(k_data["sex"])
end

#all_testテーブルの要素取得
all_test_id = []
all_test_testname = []
all_test_testday = []

res_all_test = client.query("SELECT * FROM all_test;").each do |t_data|
  all_test_id.push(t_data["id"])
  all_test_testname.push(t_data["testname"])
  all_test_testday.push(t_data["testday"])
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

<<<<<<< HEAD
#テスト種目別データ
if cgi["select_testname"] !="" then

  testname_id =[]
  testname_name =[]
  testname_testname = []
  testname_jpn = []
  testname_math = []
  testname_eng = []
  testname_sci = []
  testname_soc = []
  testname_day = []

  select_testname = cgi["select_testname"]

  testnameDB = "SELECT kojin.id, kojin.name,all_test.testname,all_test.testday, res_test.jpn, res_test.math, res_test.eng, res_test.sci, res_test.soc FROM (kojin INNER JOIN res_test ON kojin.id = res_test.id) INNER JOIN all_test ON all_test.id = res_test.id_test WHERE all_test.id=#{select_testname} ORDER BY res_test.id ASC;"

  testnameUser = client.query(testnameDB).each do |d_data|
    testname_id.push(d_data["id"])
    testname_name.push(d_data["name"])
    testname_testname.push(d_data["testname"])
    testname_day.push(d_data["testday"])
    testname_jpn.push(d_data["jpn"])
    testname_math.push(d_data["math"])
    testname_eng.push(d_data["eng"])
    testname_sci.push(d_data["sci"])
    testname_soc.push(d_data["soc"])
  end

  testnamestr = "#{testname_testname[0]}"
else
  testnameUser = []
  testnamestr = "何のテストか"
end


=======
>>>>>>> addsignform
del_id = cgi["id"]
del_name = cgi["name"]
#テスト種目の文字列をIDに変換する
d = res_all_test.count
for d in 0..d -1
  if cgi["testname"] == all_test_testname[d] then
    del_testname = all_test_id[d]
  end
end
client.query("DELETE FROM res_test WHERE id='#{del_id}' AND name='#{del_name}' AND id_test='#{del_testname}'")

print "Content-type: text/html\n\n"

print <<EOM
<html>
  <head>
  <meta http-equiv="Content-type" content="text/html; charset=euc-jp">
  <meta http-equiv="refresh" content="60" >
  <title>検索フォーム</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

  <a href='./'>TOP</a>
  <a href='./signup.cgi'>個人情報登録</a>
<<<<<<< HEAD
  <a href='./report.cgi'>テスト入力フォーム</a>
=======
>>>>>>> addsignform
  </head>
  <body>

  <h1>テストデータ</h1>
  <form id="test_data" method="POST" action="/test.cgi">
    <table id="first_table" border=1>

    <tr align="center">
    <th>生徒ID</th><th>名前</th><th>テスト種目</th><th>実施日</th><th>国語</th><th>数学</th><th>英語</th><th>理科</th><th>社会</th><th>合計点</th><th>平均点</th><th>編集</th><th>削除</th>
    </tr>
EOM
#全体表示するゾーン
    i=results.count
    for i in 0..i -1
      puts ("<tr name ='i' align='center'>")
      puts ("<td>#{id[i]}</td><td>#{name[i]}</td><td>#{testname[i]}</td><td>#{testday[i]}</td><td>#{jpn[i]}</td><td>#{math[i]}</td><td>#{eng[i]}</td><td>#{sci[i]}</td><td>#{soc[i]}</td>")
      puts ("<td>#{jpn[i]+math[i]+eng[i]+sci[i]+soc[i]}</td>")
      puts ("<td>#{(jpn[i]+math[i]+eng[i]+sci[i]+soc[i])/5}</td>")
      puts ("<td><a href='./change_test.cgi?id=#{id[i]}&name=#{name[i]}&testname=#{testname[i]}&testday=#{testday[i]}&jpn=#{jpn[i]}&math=#{math[i]}&eng=#{eng[i]}&sci=#{sci[i]}&soc=#{soc[i]}'>編集</a></td>")

      puts ("<td><a href='./test.cgi?id=#{id[i]}&name=#{name[i]}&testname=#{testname[i]}' onClick='disp()'>削除</a></td>")
      puts ("</tr>")
    end

print <<EOM
    </table>
    </form>
<!- 指定したユーザのみ表示 -->
    <h2>ユーザ別テストデータ</h2>
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
    <input type="submit" value="検索" >
    </p>
    </form>
    <table id='second_table' border=1>
    <tr>
    <th>テスト種目</th><th>実施日</th><th>国語</th><th>数学</th><th>英語</th><th>理科</th><th>社会</th>
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

    <h2>テスト種目別データ表示</h2>
    <form id='select_test_form' method='POST'>
    <select name="select_testname">
EOM

a = res_all_test.count
puts ("<option disabled selected>何のテストデータが見たい？</option>")
for a in 0..a -1
puts ("<option value='#{all_test_id[a]}'>#{all_test_id[a]}:#{all_test_testname[a]}</option>")
end

print <<EOM
    </select>
    <input type="submit" value="検索" >
    </form>
    <table id='third_table' border=1>
    <tr>
    <th>生徒ID</th><th>名前</th><th>テスト種目</th><th>実施日</th><th>国語</th><th>数学</th><th>英語</th><th>理科</th><th>社会</th>
    </tr>
EOM

t = testnameUser.count
for t in 0..t -1
  puts ("<tr>")
  puts ("<td>#{testname_id[t]}</td><td>#{testname_name[t]}</td><td>#{testname_testname[t]}</td><td>#{testname_day[t]}</td><td>#{testname_jpn[t]}</td><td>#{testname_math[t]}</td><td>#{testname_eng[t]}</td><td>#{testname_sci[t]}</td><td>#{testname_soc[t]}</td>")
#puts ("<td>#{testname_id[t]}</td><td>#{testname_name[t}</td><td>#{testname_testname[t]}</td><td>#{testname_day[t]}</td><td>#{testname_jpn[t]}</td><td>#{testname_math[t]}</td><td>#{testname_eng[t]}</td><td>#{testname_sci[t]}</td><td>#{testname_soc[t]}</td>")
  puts ("</tr>")
end

print <<EOM
#{testnamestr}
  <script type="text/javascript">
  function disp(){
    if(window.confirm("本当に削除しますか")){

    }else{
      window.alert("キャンセルされました");
     }
  }
  </script>
  </body>
</html>
EOM
