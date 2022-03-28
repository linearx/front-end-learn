#### CSS语法 [MDN CSS教程](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/First_steps/What_is_CSS)

##### 模块 



##### 选择器 [MDN选择器](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Selectors)

`*{}` 通配选择器

> 通配选择器可以与命名空间结合，但官方并不推荐使用通配选择器，因为其性能较低
>
> - *[lang^=en]匹配所有命名空间下lang属性前两位包含"en"的标签
> - *.warining 匹配所有命名空间下class为waring的元素
> - *#maincontent 匹配所有命名空间下id为maincontent的元素
> - div * 匹配div命名空间下的所有元素。
>
> ---
>
> - `ns|*` - 会匹配`ns`命名空间下的所有元素
> - `*|*` - 会匹配所有命名空间下的所有元素
> - `|*` - 会匹配所有没有命名空间的元素
> - **注意没有看见有`*|ns`的写法，但有出现 `*[]`的用法**

`div{}` 元素/标签选择器，能够匹配任意类型的HTML元素。

`.box{}` 类选择器

`#unique{}`  id选择器

`a[title]{}` 标签属性选择器

`a:hover { }` **伪类选择器，用于样式化一个元素的特定状态**

> 常用伪类

`p::first-line{}` **伪元素选择器，用于选择一个元素的某个部分而不是元素自身**

> 常用伪元素

##### 选择器运算符——将多个选择器组合从而更复杂的选择元素；注意经过运算符计算后，通常是选择后面的元素

`article p` 后代选择器（空格为后代运算符），如果第二个选择器匹配的元素具有与第一个选择器匹配的祖先则它们将被选择

`article > p` 子代选择器(>为子代选择器)，只会匹配那些作为第一个元素的**直接后代(**子元素)的第二元素

`h1+p` 相邻兄弟选择器，当第二个元素紧跟在第一个元素**之后**，并且两个元素都是属于同一个父元素的子元素，则第二个元素将被选中

`h1 ~ p` 通用兄弟选择器，位置无须紧邻，只须同层级，`A~B` 选择`A`元素**之后**所有同层级`B`元素。

```html
<!DOCTYPE HTML>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CSS Tutorial</title>
 
  <!-- Links to an external Style Sheet -->
  <link rel="stylesheet" type="text/css" href="mainstyle.css">
</head>
 
<body>
  <h1>CSS Tutorial</h1>
 
  <p>A CSS3 Tutorial that will cover pretty much everything in one tutorial</p>
 
  <h2>Let's Get Started</h2>
 
  <div>
    <h3>My Favorite Sites</h3>
    <ul>
      <li><a class="sitelink" href="google.com">Google</a></li>
      <li><a class="sitelink" href="reddit.com">Reddit</a></li>
      <li><a class="sitelink" href="amazon.com">Amazon</a></li>
    </ul>
  </div>
 
  <p id="tonyquote">We wake up on a box,
    eat breakfast from a box, go to work in a box,
    sit in a box office all day, have lunch from a box,
    then go home in a box, have dinner from a box,
    in front of the box.<span id="tonyname"> - Tony Robbins</span></p>
 
    <p class="sitelink">I also like <a href="youtube.com">YouTube</a></p>
 
    <div id="tutorials">
      <ol>
        <li>Rails</li>
        <li>NodeJS</li>
        <li>Android Games</li>
      </ol>
      <ul>
        <li>SASS</li>
        <li>HAML</li>
      </ul>
    </div>
 
    <h3>Favorite Video Games</h3>
    <p>List of my current <a href="nintendogames">favorite video games</a></p>
    <ul>
      <li alt="nintendo">Super Mario 3D Land</li>
      <li alt="nintendo">Monster Hunter 4 Ultimate</li>
      <li alt="nintendo">Pokemon Omega Ruby</li>
      <li alt="klei entertainment">Don't Starve</li>
    </ul>
 
  </body>
  </html>
```



```css
@import "heading.css";
@import "paragraph.css";
 
/* @import rules must precede all others */
 
* { font-family: "Arial Black", Gadget, sans-serif;}
 
div * { font-family: "Comic Sans MS", cursive, sans-serif; }
 
.sitelink { font-family: Georgia, serif; }
 
#tonyquote{
  font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
  color: black;
}
 
p.sitelink {
  font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;
  color: black;
}
 
span#tonyname {
  font-family: "Times New Roman", Times, serif;
  color: blue;
}
 
#tutorials ol li {
  color: purple;
}
 
#tutorials ul li {
  color: green;
}
 
h3 + p{
  font-style: italic;
}
 
h3 + p > a {
  color: red;
}
 
p[class] {
  background: gray;
}
 
p[id] {
  background: yellow;
}
 
*[alt~="nintendo"] {background: orange;}
```



---

##### 文本样式

```html
<!DOCTYPE HTML>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CSS Tutorial</title>
 
  <link rel="stylesheet" type="text/css" href="stylesheet2.css">
</head>
 
<body>
 
<p id="lorem">
  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
  eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
  enim ad minim veniam, quis nostrud exercitation ullamco laboris
  nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
  in reprehenderit in voluptate velit esse cillum dolore eu fugiat
  nulla pariatur. Excepteur sint occaecat cupidatat non proident,
  sunt in culpa qui officia deserunt mollit anim id est laborum.
</p>
 
<!-- Demonstrate Font Properties -->
 
<p id="fsNormal">Font Style Normal</p>
<p id="fsItalic">Font Style Italic</p>
<p id="fsOblique">Font Style Oblique</p>
<p id="fvNormal">Font Varient Normal</p>
<p id="fvSmallCaps">Font Varient Small-Caps</p>
<p id="fwNormal">Font Weight Normal</p>
<p id="fwBold">Font Weight Bold</p>
<p id="fwBolder">Font Weight Bolder</p>
<p id="fwLighter">Font Weight Lighter</p>
<p id="fszMedium">Font Size Medium</p>
<p id="fszXXSmall">Font Size XX-Small</p>
<p id="fszSmall">Font Size Small</p>
<p id="fszXXLarge">Font Size XX-Large</p>
<p id="fszLarge">Font Size Large</p>
<p id="fszPrct">Font Size 200%</p>
<p id="fsz25pt">Font Size 25pt</p>
<p id="lhNormal">Font Line Height Normal</p>
<p id="lh25pt">Font Line Height 25pt</p>
<p id="lh200Prct">Font Line Height 200%</p>
 
<!-- Demonstrate Font Properties End -->
 
</body>
</html>
```



```css
#lorem {
  /*  Inside Border
      padding 10px 10px 10px 10px : Top, Right, Bottom, Left
      padding 10px 25px 15px : Top, Right / Left, Bottom
      padding 10px 15px : Top / Bottom, Left / Right
  */
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 20px;
  padding-right: 20px;
 
  /*  Outside Border
      margin 10px 10px 10px 10px : Top, Right, Bottom, Left
      margin 10px 25px 15px : Top, Right / Left, Bottom
      margin 10px 15px : Top / Bottom, Left / Right
  */
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 10px;
  margin-right: 10px;
 
  /*
      border: 5px solid green;
      border-width, border-style, border-color
      none, dotted, dashed, solid, double, groove, ridge, inset, outset
  */
  border-top: 5px solid #00308F;
  border-bottom: 5px dotted #00308F;
  border-left: 5px dashed #00308F;
  border-right: 5px double #00308F;
 
  /*
  background: color position/size repeat origin clip attachment
  image|initial|inherit;
  background-position: left top bottom right
  (If you only specify one the other value will be center)
  background-size: auto length;
  background-repeat: repeat repeat-x repeat-y no-repeat
  background: #F2F3F4 url("Repeat.png") repeat;
  */
  background: #F2F3F4;
 
  /*
  font: font-style font-variant font-weight font-size/line-height font-family;
  font-style: normal, italic, oblique
  font-varient: normal, small-caps
  font-weight: normal, bold, bolder, lighter, 100 - 900
  font-size: medium, xx-small - small, xx-large - large, %, length in pt
  line-height: normal, length in pt, %
  font-family: "Times New Roman", Georgia, Serif
  */
 
  color: black;
}
 
#fsNormal {
  font-style: normal;
}
 
#fsItalic {
  font-style: italic;
}
 
#fsOblique {
  font-style: oblique;
}
 
#fvNormal {
  font-variant: normal;
}
 
#fvSmallCaps {
  font-variant: small-caps;
}
 
#fwNormal {
  font-weight: normal;
}
 
#fwBold {
  font-weight: bold;
}
 
#fwBolder {
  font-weight: bolder;
}
 
#fwLighter {
  font-weight: lighter;
}
 
#fszMedium {
  font-size: medium;
}
 
#fszXXSmall {
  font-size: xx-small;
}
 
#fszSmall {
  font-size: small;
}
 
#fszXXLarge {
  font-size: xx-large;
}
 
#fszLarge {
  font-size: large;
}
 
#fszPrct {
  font-size: 200%;
}
 
#fsz25pt {
  font-size: 25pt;
}
 
#lhNormal {
  line-height: normal;
}
 
#lh25pt {
  line-height: 25pt;
}
 
#lh200prct {
  line-height: 200%;
}
 
#lh200prct {
  line-height: 200%;
}
```

https://www.newthinktank.com/2015/04/learn-css3-one-video/