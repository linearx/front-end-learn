### HTML表格

在HTML中一个很普通的任务是构建表格数据，有大量的元素和属性是来满足这种需求的

#### 1. HTML表格基础知识

表格是由行和列组成的结构化数据集(表格数据)，它能够使你简捷迅速地查找某个表示不同类型数据之间的某种关系的值。

表格的一个特点就是严格. 通过在行和列的标题之间进行视觉关联的方法，就可以让信息能够很简单地被解读出来

> HTML 表格 应该用于表格数据 ，这正是 HTML 表格设计出来的用途。不应当使用表格进行布局！
>
> 不幸的是, 许多人习惯用 HTML 表格来实现网页布局。这种做法以前是很常见的，因为以前 CSS 在不同浏览器上的兼容性比较糟糕 ; 表格布局现在不太普遍，但您可能仍然会在网络的某些角落看到它们



##### 1.1 表格标题th

表格中的标题是特殊的单元格，通常在行或列的开始处，定义行或列包含的数据类型。当标题明显突出的时候，你可以更加简单地找到你想找的数据，设计上也会看起来更好。

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Dogs table</title>
    <link href="minimal-table.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <h1>Dogs Table</h1>

    <table>
      <tr>
        <th>&nbsp;</th>
        <th>Knocky</th>
        <th>Flor</th>
        <th>Ella</th>
        <th>Juan</th>
      </tr>
      <tr>
        <td>Breed</td>
        <td>Jack Russell</td>
        <td>Poodle</td>
        <td>Streetdog</td>
        <td>Cocker Spaniel</td>
      </tr>
      <tr>
        <td>Age</td>
        <td>16</td>
        <td>9</td>
        <td>10</td>
        <td>5</td>
      </tr>
    </table>
  </body>
</html>
```

##### 1.2 单元格跨越多行和多列

有时我们希望单元格跨越多行或多列。以下是一个简单的例子，显示了一些常见动物的名字。在某些情况下，我们要显示动物名称旁边的男性和女性的名字。有时候我们又不需要。

使用表格元素的属性 `colspan` 和 `rowspan`即可实现上述效果。

```html
// Animals-table.html
//minimal-tab.css
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Animals table</title>
    <link href="minimal-table.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <h1>Animals table</h1>

    <table>
      <tr>
        <th colspan="2">Animals</th>
      </tr>
      <tr>
        <th colspan="2">Hippopotamus</th>
      </tr>
      <tr>
        <th rowspan="2">Horse</th>
        <td>Mare</td>
      </tr>
      <tr>
        <td>Stallion</td>
      </tr>
      <tr>
        <th>Crocodile</th>
      </tr>
      <tr>
        <th rowspan="2">Chicken</th>
        <td>Hen</td>
      </tr>
      <tr>
        <td>Rooster</td>
      </tr>
    </table>


  </body>
</html>
```



##### 1.3 为表格中的一列提供共同的样式

HTML有一种方法可以定义整列数据的样式信息：就是 **`<col>`** 和 **`<colgroup>`** 元素。 

它们存在是因为如果你想让一列中的每个数据的样式都一样，那么你就要为每个数据都添加一个样式，这样的做法是令人厌烦和低效的。

你通常需要在列中的每个 `<td>` 或 `<th>` 上定义样式，或者使用一个复杂的选择器，比如 [`:nth-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-child)

> HTML中定义表格是通过行+行上的单元格组成，并没有直接定义列。因此要对一列提供共同的样式相对而言较麻烦；
>
> 可以使用CSS的伪类nth-child，为每行(tr)的每第几个元素(对应第几列)进行设置；
>
> 也可以使用HTML中的col与colgroup标签标签

在table元素中添加colgroup标签，一个col元素对应表格中的一列。如下，若一个表格中有七列需要分别操作其样式，则需要使用七个col元素。

```html
        <colgroup>
            <col>
            <col>
            <col style="background-color: #97DB9A;">
            <col style="width: 42px;">
            <col style="background-color: #97DB9A;">
            <col style="background-color: #DCC48E; border: 4px solid #C1437A;">
            <col style="width: 42px;">
        </colgroup>
```



```html
// colgroup-and-group.html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>School timetable</title>
    <style>
    html {
      font-family: sans-serif;
    }

    table {
      border-collapse: collapse;
      border: 2px solid rgb(200,200,200);
      letter-spacing: 1px;
      font-size: 0.8rem;
    }

    td, th {
      border: 1px solid rgb(190,190,190);
      padding: 10px 20px;
    }

    td {
      text-align: center;
    }

    caption {
      padding: 10px;
    }
    </style>
  </head>
  <body>
    <h1>School timetable</h1>

    <table>
        <colgroup>
            <col>
            <col>
            <col style="background-color: #97DB9A;">
            <col style="width: 42px;">
            <col style="background-color: #97DB9A;">
            <col style="background-color: #DCC48E; border: 4px solid #C1437A;">
            <col style="width: 42px;">
        </colgroup>
      <tr>
        <td>&nbsp;</td>
        <th>Mon</th>
        <th>Tues</th>
        <th>Wed</th>
        <th>Thurs</th>
        <th>Fri</th>
        <th>Sat</th>
        <th>Sun</th>
      </tr>
      <tr>
        <th>1st period</th>
        <td>English</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>German</td>
        <td>Dutch</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
      </tr>
      <tr>
        <th>2nd period</th>
        <td>English</td>
        <td>English</td>
        <td>&nbsp;</td>
        <td>German</td>
        <td>Dutch</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
      </tr>
      <tr>
        <th>3rd period</th>
        <td>&nbsp;</td>
        <td>German</td>
        <td>&nbsp;</td>
        <td>German</td>
        <td>Dutch</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
      </tr>
      <tr>
        <th>4th period</th>
        <td>&nbsp;</td>
        <td>English</td>
        <td>&nbsp;</td>
        <td>English</td>
        <td>Dutch</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
      </tr>
    </table>
  </body>
</html>
```

#### 2. HTML表格高级特性和可访问性

表格的标题/摘要，以及将你表格中的各行分组成头部、正文、页脚部分，提高视力受损用户的可访问性。

##### 2.1使用 caption为你的表格增加一个标题

通过 `<caption>` 元素你可以为你的表格增加一个标题，再把 `<caption>`元素放入 `<table>` 元素中。

```html
<table>
  <caption>Dinosaurs in the Jurassic period</caption>

</table>
```

标题意味着包含对于表格内容的描述，这对那些希望可以快速浏览网页中的表格对他们是否有帮助的读者们来说，是非常好的功能。

##### 2.2为表格添加thead tfoot 和tbody结构

由于你的表格在结构上有点复杂，如果把它们定义得更加结构化，那会帮助我们更能了解结构。一个明确的方法是使用 `<thead>`, `<tfoot>`,和 `<tbody>`，这些元素允许你把表格中的部分标记为表头、页脚、正文部分。

- `<thead> `需要嵌套在 table 元素中，放置在头部的位置，因为它通常代表第一行，第一行中往往都是每列的标题，但是不是每种情况都是这样的。如果你使用了 `<col>/<colgroup>` 元素，那么 `<thead>`元素就需要放在它们的下面。

- `<tfoot> `需要嵌套在 table 元素中，放置在底部 (页脚)的位置，一般是最后一行，往往是对前面所有行的总结，比如，你可以按照预想的方式将`<tfoot>`放在表格的底部，或者就放在 `<thead>` 的下面。(浏览器仍将它呈现在表格的底部)

-  `<tbody>` 需要嵌套在 table 元素中，放置在 `<thead>`的下面或者是 `<tfoot>` 的下面，这取决于你如何设计你的结构

  >  `<tbody>` 总是包含在每个表中，如果你没有在代码中指定它，那就是隐式存在的。隐式形式表示浏览器会自动将其生成，而无需自己去写。

##### 2.3 scope属性

 scope 属性，可以添加在`<th>` 元素中，用来帮助屏幕阅读设备更好地理解那些标题单元格，这个标题单元格到底是列标题呢，还是行标题。屏幕阅读设备会识别这种结构化的标记，并一次读出整列或整行

```html
<thead>
  <tr>
    <th scope="col">Purchase</th>
    <th scope="col">Location</th>
    <th scope="col">Date</th>
    <th scope="col">Evaluation</th>
    <th scope="col">Cost (€)</th>
  </tr>
</thead>
-----------------------------------------------------
<tr>
  <th scope="row">Haircut</th>
  <td>Hairdresser</td>
  <td>12/09</td>
  <td>Great idea</td>
  <td>30</td>
</tr>
```

##### 2.4 使用id和headers属性创造标题与单元格的联系

如果要替代 scope 属性，可以使用 id 和 headers 属性来创造标题与单元格之间的联系。使用方法如下:

- 为每个<th> 元素添加一个唯一的 id 。
- 为每个 <td> 元素添加一个 headers 属性。每个单元格的headers 属性需要包含它从属于的所有标题的id，之间用空格分隔开。

```html
<thead>
  <tr>
    <th id="purchase">Purchase</th>
    <th id="location">Location</th>
    <th id="date">Date</th>
    <th id="evaluation">Evaluation</th>
    <th id="cost">Cost (€)</th>
  </tr>
</thead>
<tbody>
<tr>
  <th id="haircut">Haircut</th>
  <td headers="location haircut">Hairdresser</td>
  <td headers="date haircut">12/09</td>
  <td headers="evaluation haircut">Great idea</td>
  <td headers="cost haircut">30</td>
</tr>

  ...

</tbody>
```

##### 2.5 示例

```html

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>太阳系行星数据</title>
    <link href="minimal-table.css" rel="stylesheet">
  </head>
  <body>
    <div>
      <table>
        <colgroup>
          <col>
          <col>
          <col style="border: 2px solid black;">
        </colgroup>
        <thead>
          <caption>太阳系行星数据</caption>
          <tr>
            <th colspan="2">&nbsp;</th>
            <th> 名字 </th>
            <th> 质量 (10<sup>24</sup>kg) </th>
            <th> 直径 (km) </th>
            <th> 密度 (kg/m<sup>3</sup>) </th>
            <th> 重力 (m/s<sup>2</sup>) </th>
            <th> 天长 (hours) </th>
            <th> 与太阳距离 (10<sup>6</sup>km) </th>
            <th> 平均温度 (°C) </th>
            <th> 卫星数量 </th>
            <th> 备注 </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th rowspan="4" colspan="2">类地行星</th>
            <th>水星</th>
            <td>0.330</td>
            <td>4,879</td>
            <td>5427</td>
            <td>3.7 </td>
            <td>4222.6</td>
            <td>57.9</td>
            <td>167</td>
            <td>0</td>
            <td>与太阳最近</td>
          </tr>
          <tr>
            <th>金星</th>
          </tr>
          <tr>
            <th>地球</th>
          </tr>
          <tr>
            <th>火星</th>
          </tr>
          <tr>
            <th rowspan="4" scope="row">类木行星</th>
            <th rowspan="2" scope="row">气巨星</th>
            <th>木星</th>
          </tr>
          <tr>
            <th>土星</th>
          </tr>
          <tr>
            <th rowspan="2" scope="row">冰巨星</th>
            <th>天王星</th>
          </tr>
          <tr>
            <th>海王星</th>
          </tr>
          <tr>
            <th colspan="2" scope="row">矮行星</th>
            <th>冥王星</th>
          </tr>
        </tbody>
      </table>
    </div>

  </body>
</html>
```

