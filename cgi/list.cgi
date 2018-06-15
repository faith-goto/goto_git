#!/usr/local/bin/ruby

#ライブラリ読み込み
require "cgi"
require "mysql2"

#インスタンスを生成し、table変数に格納
cgi = CGI.new
table= cgi['table']

#DB接続
#client = Mysql2::Client.new(host: "localhost", username: "yoshihara", password: "", database: "practice")

# HTMLとして画面に返す
print "Content-type: text/html\n\n"
puts ("<html>")
puts ("<head>")
puts ("<title>#{table}テーブルの表示</title>")
puts ("<meta charset='utf-8'>")
puts ("</head>")
puts ("<body>")
puts ("<h1>#{table}テーブル</h1>")
puts ("<table border=1>")
puts ("<tr>")

case table
#userテーブルの内容を表示
when "user" then
  id = []
  username = []
  organization_id = []
  email = []
  password = []
  login_num = []
  results = client.query("SELECT id, username, organization_id, email, password, login_num FROM #{table} ORDER BY id ASC")
  results.each do |u_data|
    id.push(u_data["id"])
    username.push(u_data["username"])
    organization_id.push(u_data["organization_id"])
    email.push(u_data["email"])
    password.push(u_data["password"])
    login_num.push(u_data["login_num"])
  end
  puts ('<th>id</th><th>username</th><th>organization</th><th>email</th><th>password</th><th>login_num</th>')
  puts ("</tr>")
  i = results.count
  for i in 0..i-1
    puts ("<tr>")
    puts ("<td>#{id[i]}</td><td>#{username[i]}</td><td>#{organization_id[i]}</td><td>#{email[i]}</td><td>#{password[i]}</td><td>#{login_num[i]}</td>")
    puts ("</tr>")
  end
#organizationテーブルの内容を表示
when "organization"  then
  id = []
  name = []
  postal_code = []
  adress = []
  tel = []
  results = client.query("SELECT id, name, postal_code, adress, tel FROM #{table} ORDER BY id ASC")
  results.each do |o_data|
    id.push(o_data["id"])
    name.push(o_data["name"])
    postal_code.push(o_data["postal_code"])
    adress.push(o_data["adress"])
    tel.push(o_data["tel"])
  end
  puts ('<th>id</th><th>name</th><th>postal_code</th><th>adress</th><th>tel</th>')
  puts ("</tr>")
  i = results.count
  for i in 0..i-1
    puts ("<tr>")
    puts ("<td>#{id[i]}</td><td>#{name[i]}</td><td>#{postal_code[i]}</td><td>#{adress[i]}</td><td>#{tel[i]}</td>")
    puts ("</tr>")
  end
#firstテーブルの内容を表示
when "first"  then
  results = client.query("SELECT id, name, jpn, math, eng, sci, created, modifined FROM #{table} ORDER BY id ASC")
  id = []
  name = []
  jpn = []
  math = []
  eng = []
  sci = []
  created = []
  modifined = []
  results.each do |f_data|
    id.push(f_data["id"])
    name.push(f_data["name"])
    jpn.push(f_data["jpn"])
    math.push(f_data["math"])
    eng.push(f_data["eng"])
    sci.push(f_data["sci"])
    created.push(f_data["created"])
    modifined.push(f_data["modifined"])
  end
  puts ('<th>id</th><th>name</th><th>jpn</th><th>math</th><th>eng</th><th>sci</th><th>created</th><th>modifined</th>')
  puts ("</tr>")
  i = results.count
  for i in 0..i-1
    puts ("<tr>")
    puts ("<td>#{id[i]}</td><td>#{name[i]}</td><td>#{jpn[i]}</td><td>#{math[i]}</td><td>#{eng[i]}</td><td>#{sci[i]}</td><td>#{created[i]}</td><td>#{modifined[i]}</td>")
    puts ("</tr>")
  end
#検索フォームの表示
when "serch" then
  results = client.query("SELECT id, name, jpn, math, eng, sci, created, modifined FROM #{table} ORDER BY id ASC")
  id = []
  name = []
  jpn = []
  math = []
  eng = []
  sci = []
  created = []
  modifined = []
  results.each do |f_data|
    id.push(f_data["id"])
    name.push(f_data["name"])
    jpn.push(f_data["jpn"])
    math.push(f_data["math"])
    eng.push(f_data["eng"])
    sci.push(f_data["sci"])
    created.push(f_data["created"])
    modifined.push(f_data["modifined"])
  end
  puts ('<h1>検索フォーム</h1>')
  puts ('<form>テーブル名')
  puts ('</from>')
end
puts ("</table>")
puts ("</body>")
puts ("</html>")
