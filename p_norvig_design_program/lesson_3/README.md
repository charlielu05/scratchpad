
# REGEX Review
```
lit(s) | lit('a') | {a}
seq(x,y) | seq(lit('a'), lit('b')) | {ab}
alt(x,y) | alt(lit('a'), lit('b')) | {a,b}
star(x) | star(lit('a')) | {"", a,aa,aaa...}
oneof(x) | oneof('abc') | {a,b,c}