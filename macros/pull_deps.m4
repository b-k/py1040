m4_divert(-1)
m4_changequote(<|,|>)

m4_define(<|strip|>, <|m4_translit($1, <|
|>)|>)

m4_define(Print,<|m4_divert(1)$1<||>m4_divert(-1)|>)

If this is a new dict, close the last dict. We'll use sed to close the final dict.
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
