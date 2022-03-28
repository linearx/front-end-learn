### 枚举属性

##### for/in 循环

当要对一个对象可以获取得到的属性名进行迭代的时候，可以使用for-in的写法

**`for...in`语句**以任意顺序遍历一个对象的除[Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)以外的[可枚举](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Enumerability_and_ownership_of_properties)属性，包括**继承的可枚举属性**。语法如下，有`for (variable in objecy){statement}`

> for in写法不应当用来迭代关注索引顺序的Array，这与Python有较大的不同。
>
> 这是因为for in关注的是

##### Object.keys()

##### Object.getOwnPropertyNames()

##### Object.getOwnPropertySymbols()



