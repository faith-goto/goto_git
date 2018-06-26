#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require "mysql2"

#インスタンスを生成し、table変数に格納
cgi = CGI.new

#DB接続
client = Mysql2::Client.new(host: "localhost", username: "goto", password: "", database: "goto_practice")

#kojinテーブルの要素を取得
kojin_id = []
kojin_name = []
kojin_sex =[]
kojin_birthday = []

res_kojin = client.query("SELECT * FROM kojin;").each do |k_data|
  kojin_id.push(k_data["id"])
  kojin_name.push(k_data["name"])
  kojin_sex.push(k_data["sex"])
  kojin_birthday.push(k_data["birthday"])

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

id = cgi["new_id"]
id_test = cgi["new_test"]
jpn = cgi["jpnval"]
math = cgi["mathval"]
eng = cgi["engval"]
sci = cgi["scival"]
soc = cgi["socval"]
cthid = id.to_i
cthid -= 1
name = kojin_name[cthid]

if cgi["new_id"] != "" then
  client.query("INSERT INTO res_test (id,name,id_test,jpn,math,eng,sci,created,modified,soc) VALUES (#{id},'#{name}',#{id_test},#{jpn},#{math},#{eng},#{sci},now(),now(),#{soc});")
end


print "Content-type: text/html\n\n"

print <<EOM
<html>
  <head>
  <meta http-equiv="Content-type" content="text/html; charset=euc-jp">
  <title>検索フォーム</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

  <a href='./'>TOP</a>
  <a href='./test.cgi'>複数データ管理</a>

  </head>
  <body>

  <h2>ユーザ別テストデータ</h2>
  <form id='report_form' method='POST'>
  <table class="report_data">
  <tr>
    <th>名前:</th>
  <td><select name='new_id'>
EOM

  i = res_kojin.count
  puts ("<option disabled selected>誰のテストデータを入力するか</option>")
  for i in 0..i -1
  puts ("<option value='#{kojin_id[i]}'>#{kojin_id[i]}:#{kojin_name[i]}</option>")
  end

print <<EOM
  </select></td>
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
  <tr>
    <th>社会:</th>
    <td><input type="number" name="socval" min=0 max=100 required></td>
  </tr>
  <tr>
    <th>テスト種目:</th>
  <td><select name='new_test'>
EOM

  i = res_all_test.count
  puts ("<option disabled selected>何のテスト？</option>")
  for i in 0..i -1
  puts ("<option value='#{all_test_id[i]}'>#{all_test_testname[i]}</option>")
  end

print <<EOM
  </select></td>
  </tr>

  </table>
  <input type="submit" value="出力" >
  </form>


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
