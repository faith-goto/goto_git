
#ライブラリ読み込み
require "mysql2"


#DB接続
client = Mysql2::Client.new(host: "localhost", username: "goto", password: "", database: "goto_practice")
client.query("SELECT name FROM first").each do |row|
  p row
end
