<h1 align="center">Member Manage Page</h1>

<div style="text-align: center;">
    <a href="/add" > new member </a>
</div>
<table border="1" align="center">
%for i,m in enumerate(item_list):
 %if i==0:
 <tr>
   <td>{{m["id"]}}</td>
   <td>{{m["name"]}}</td>
   <td>飲む</td>
   <td>入金</td>
   <td>{{m["money"]}}</td>
   <td>{{m["lucky"]}}</td>
   <td>削除</td>
 </tr>
 %else:
 <tr>
   <td>{{m["id"]}}</td>
   <td>{{m["name"]}}</td>
   <td><a href="/update" >Modify</a></td>
   <td><a href="/charge/{{m["id"]}}" >Charge</a></td>
   <td>{{m["money"]}}</td>
   <td>{{m["lucky"]}}</td>

   <td><a href="/del/{{m["id"]}}">delete</a></td>
 </tr>
 %end
%end
</table>
