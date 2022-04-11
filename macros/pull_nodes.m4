m4_divert(-1)
m4_changequote(<|,|>)

m4_define(<|strip|>, <|m4_translit($1, <|
|>)|>)

m4_define(Print,<|m4_divert(1)$1<||>m4_divert(-1)|>)

m4_define(<|m4_form|>, <|m4_define(<|m4form|>,$1)|>)
m4_define(<|rm_newlines|>, <|m4_patsubst($1,<|
|>)|>)

m4_define(<|Cell|>, <|Print(<|m4form<||>_$1 = cell("$3", rm_newlines($2), "rm_newlines($4)", flag="rm_newlines($5)", name="m4form<||>_$1", form="m4form"),
|>)|>)
m4_define(<|CV|>, <|Cv('strip(m4_ifelse(<|$#|>,1,m4form,$1))_<||>strip(m4_ifelse(<|$#|>,1,$1,$2))')|>)
m4_define(<|SUM|>, <|$@, |>)
m4_define(<|SUM|>, <|m4_ifelse(<|$1|>,<||>,0,
<|CV(strip($1)) + SUM(m4_shift($@))|>)|>)

m4_define(IF, <|(($2) if ($1) else ($3))|>)
m4_define(FirstPart, <|$1|>)
m4_define(SecondPart, <|$2|>)

m4_define(Fswitch, <|m4_ifelse($#,1, $1, <|IF(fstatus()=='FirstPart$1', SecondPart$1,Fswitch(m4_shift($@)))|>) |>)

Print(<|
cell_list = dict(
|>)


Everything else got written to diversion 1; write the final end paren to 2
m4_divert(2) )
m4_divert(-1)
