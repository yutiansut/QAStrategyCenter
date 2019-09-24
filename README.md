# QAStrategyCenter
StrategyTemplete


## QUANTAXIS Strategy Template


### 标准模板


```
"{{parameter}}"  ===render==> "parameter"

int("{{parameter}}")  /  {{parameter}}  ===render==> int("parameter") /  parameter
```

当你需要写入一个预设值时, 使用{{}} 来作为占位符, 并在占位符中写入你的预设变量

{{x}}  表示在渲染的时候, 把x的值 渲染进模板中

如 x= 1 , 则 a = {{x}} 会被渲染为  a = 1

### 渲染过程

基于```Jinja2```实现模板渲染, 参数二次填充

