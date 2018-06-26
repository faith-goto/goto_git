#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require "mysql2"

#インスタンスを生成し、table変数に格納
cgi = CGI.new

#DB接続
client = Mysql2::Client.new(host: "localhost", username: "goto", password: "", database: "goto_practice")

=begin
必要なもの
id,name,sex,birthday
mysql> INSERT INTO kojin (name,sex,birthday) VALUES ('hoge huge','mele','2018-06-06');
=end

name = cgi["namedata"]
sex = cgi["sex"]
year = cgi["year"]
month= cgi["month"]
day = cgi["day"]

=begin
if cgi["namedata"] != "" then
  client.query(addNew)
  cgi["namedata"].clear
  print cgi.header( {
  "status"     => "REDIRECT",
  "Location"   => "http://10.172.81.244:510/"
})
=end
if cgi["namedata"] != "" then
signup_com = "INSERT INTO kojin (name,sex,birthday) VALUES ('#{name}','#{sex}','#{year}-#{month}-#{day}');"
  client.query(signup_com)
end


print "Content-type: text/html\n\n"

print "name:#{name}"
print "sex:#{sex}"
print "year:#{year}"
print "month:#{month}"
print "day:#{day}"

print <<EOM
<html>
  <head>
  <meta http-equiv="Content-type" content="text/html; charset=euc-jp">
  <title>個人情報追加フォーム</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

  <a href='./'>TOP</a>
  <a href='./test.cgi'>複数データ管理</a>
  </head>
  <body>

  <h3>個人情報新規登録</h2>
  <form id="signup_form" method="POST">
    <table class="signup_data">
    <tr>
      <th>名前:</th>
      <td><input type="text" name="namedata" value="" required></td>
    </tr>
    <tr>
      <th>性別:</th>
      <td>
      <select name="sex">
        <option disabled selected>---</option>
        <option value="mele">男性</option>
        <option value="femele">女性</option>
        <option value="">回答しない</option>
      </td>
    </tr>
    <tr>
      <th>生年月日:</th>
      <td>
      <select name="year">
        <option disabled selected>---</option>
        <option value="1900">1900</option>
      </select>年
      <select name="month">
        <option disabled selected>---</option>
        <option values="1">1</option>
      </select>月
      <select name="day">
        <option disabled selected>---</option>
        <option values="1">1</option>
      </select>日
      </td>
    </tr>
    </table>
    <button type="submit">送信</button>
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
