#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require "mysql2"
<<<<<<< HEAD
require "date"
=======
>>>>>>> addsignform

#インスタンスを生成し、table変数に格納
cgi = CGI.new

<<<<<<< HEAD
#当日の日付要素を取得
d = Date.today

=======
>>>>>>> addsignform
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

<<<<<<< HEAD
if cgi["namedata"] != "" && cgi["sex"] != "" && cgi["year"] !="" && cgi["month"] !="" && cgi["day"] !="" then
  lastY = year.to_i
  lastM = month.to_i
  lastD = day.to_i
  lastYMD = Date.valid_date?(lastY,lastM,lastD)
  if lastYMD then
    signup_com = "INSERT INTO kojin (name,sex,birthday) VALUES ('#{name}','#{sex}','#{year}-#{month}-#{day}');"
    client.query(signup_com)
  else
    errortest = "生年月日が正しくありません"
  end
end



print "Content-type: text/html\n\n"

=======
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

>>>>>>> addsignform
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
<<<<<<< HEAD
      <select name="sex" required>
        <option disabled selected>---</option>
        <option value="mele">男性</option>
        <option value="femele">女性</option>
        <option value="gender">回答しない</option>
=======
      <select name="sex">
        <option disabled selected>---</option>
        <option value="mele">男性</option>
        <option value="femele">女性</option>
        <option value="">回答しない</option>
>>>>>>> addsignform
      </td>
    </tr>
    <tr>
      <th>生年月日:</th>
      <td>
<<<<<<< HEAD
      <select name="year" required>
EOM

i=1980
puts ("<option disabled selected>---</option>")
for i in i .. d.year
  puts ("<option value='#{i}'>#{i}</option>")
end

print <<EOM
      </select>年
      <select name="month">
EOM
i=1
puts ("<option disabled selected>---</option>")
        for i in i .. 12
          puts ("<option value='#{i}'>#{i}</option>")
        end
print <<EOM
      </select>月
      <select name="day">

EOM

puts ("<option disabled selected>---</option>")
i = 1
for i in i..31
  puts ("<option value='#{i}'>#{i}</option>")
end

print <<EOM
      </select>日
      </td>
      </tr>
    </table>
    <button type="submit">送信</button>
  </form>
  #{errortest}

  <script type="text/javascript">

=======
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
>>>>>>> addsignform
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
