m4_divert(-1)
m4_changequote(<|,|>)

m4_define(<|strip|>, <|m4_translit($1, <|
|>)|>)

m4_define(Print,<|m4_divert(1)$1<||>m4_divert(-1)|>)

At the top of a form redefine the form name used here (without the _)
m4_define(<|m4_form|>, <|m4_define(<|m4form|>,$1)|>)

m4_define(<|Cell|>, <|Print(m4form<||>_$1 = [)$4<||>Print(<|],
|>)|>)

m4_define(<|CV|>, <|m4_divert(1)"strip(m4_ifelse(<|$#|>,1,m4form,$1))_<||>strip(m4_ifelse(<|$#|>,1,$1,$2))", m4_divert(-1)|>)
m4_define(<|SUM|>, <|m4_divert(1)$@,<||>m4_divert(-1)|>)
m4_define(<|SUM|>, <|m4_ifelse(<|$1|>,<||>,,
<|m4_divert(1)"m4form<||>_<||>strip($1)", SUM(m4_shift($@))|>)m4_divert(-1)|>)
Print(<|
deps = dict (
|>)

Everything else got written to diversion 1; write the final end paren to 2
m4_divert(2) )
m4_divert(-1)
