<h1>Member_list</h1>
<a href="/add" > new </a>  <!--add item -->
<table border="1">
%for i,m in enumerate(item_list):
 %if i==0:
 <tr>
   <td>{{m["id"]}}</td>
   <td>{{m["name"]}}</td>
   <td>{{m["money"]}}</td>
   <td>{{m["lucky"]}}</td>
   <td></td>
   <td></td>
 </tr>
 %else:
 <tr>
   <td>{{m["id"]}}</td>
   <td>{{m["name"]}}</td>
   <td>{{m["money"]}}</td>
   <td>{{m["lucky"]}}</td>
   <td><a href="/update" >Drink</a></td> <!-- drink -->
   <td><a href="/del/{{m["id"]}}">delete</a></td> <!-- delete member -->
 </tr>
 %end
%end
</table>
