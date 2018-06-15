#!/usr/local/bin/ruby
print "Content-type: text/html\n\n"

greeting = "Hello Goto"

print <<EOM
<html>
<head>
</head>
<body>
#{greeting}, world!
</body>
</html>
EOM
