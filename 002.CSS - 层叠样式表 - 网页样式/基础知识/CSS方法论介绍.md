https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Organizing

#### 1. OOCSS

OOCSS的基本理念是将你的CSS分解成可复用的对象，于是你可以在你的站点上任何需要的地方使用





#### 2. BEM 块级元素修饰字符

http://getbem.com/ 

BEM — Block Element Modifier is a methodology that helps you to create reusable components and code sharing in front-end development

BEM即为块级元素修饰字符（Block Element Modifier）。

- 在BEM中，一个块，例如一个按钮、菜单或者标志，就是独立的实体。

- 一个元素就像一个列表项或者标题一样，被绑定到它所在的块。

- 修饰字符是标记到一个块或者元素的标识，能够改变样式或者行为。

- 你能认出使用BEM的代码，因为代码中在CSS的类里使用了多余的一个下划线和连字符。http://getbem.com/naming/

- ```html
  <form class="form form--theme-xmas form--simple">
    <input class="form__input" type="text" />
    <input
      class="form__submit form__submit--disabled"
      type="submit" />
  </form>
  ```

  

#### 3. CSS构建体系

另一种组织CSS的方法是利用一些对于前端开发者可用的工具，它们让你可以稍微更程式化地编写CSS。

有很多工具，我们将它们分成**预处理工具**和**后处理工具**。

- 预处理工具以你的原文件为基础运行，将它们转化为样式表；如Sass
- 后处理工具使用你已完成的样式表，然后对它做点手脚——也许是优化它以使它加载得更快。

##### 3.1定义变量

CSS现在有原生的[自定义属性](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Using_CSS_custom_properties)，所以这个功能越来越没那么重要了，但是你使用Sass的可能原因之一为，能够作为设置定义用于一个项目的所有颜色和字体，之后这些变量在项目中可用。这意味着如果你意识到你用了错误的蓝色阴影，你只需要在一个地方修改。

如果我们创建了在下面的第一行里面叫做`$base-color`的变量，我们之后可以在样式表的任何需要这一颜色的地方使用它。

```css
$base-color: #c6538c;

.alert {
  border: 1px solid $base-color;
}
```

编译完CSS后，你会在最终的样式表里面得到下面的CSS：

```css
.alert {
  border: 1px solid #c6538c;
}
```

##### 3.2 编译组件样式表

一种组织CSS的方式是将样式表分成小的样式表。

在使用Sass时，你可以在另一个层次上理解，然后得到许多小样式表——甚至到了每个组件都有一个独立样式表的地步。使用Sass中的include功能，这些都可以被编译为一个、或者少数几个真正链接到你的网站的样式表。

##### 3.3 后处理以进行优化

如果你对加入例如许多额外的注释和空格，增大你的样式表大小有所关心的话，那么后处理会通过在生产版本中略去任何不必要的东西的方式，优化CSS。

后处理解决方案中，通过这种方式实现的一个例子是[cssnano](https://cssnano.co/)。