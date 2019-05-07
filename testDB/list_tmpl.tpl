<h1>item_list</h1>
<a href="/add" > new </a>  <!--add item -->
<table border="1">
%for item in item_list:
 <tr>
   <td>{{item["id"]}}</td>
   <td>{{item["name"]}}</td>
   <td><a href="/del/{{item["id"]}}">delete</a></td> <!-- delete item -->
 </tr>
%end
　<a href="/update" > update </a>  <!--update item -->
</table>
