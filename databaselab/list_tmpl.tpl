<head>
  <title>Tokunaga Lab Coffee</title>
  <style>
  </style>
  <link rel="stylesheet" href="h1.css">
</head>

<h1 align="center" class="cp_h1title">Deposit manager</h1>

<!-- <a href="/add" > new </a>  -->
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

 </tr>
 %else:
 <tr>
   <td>{{m["id"]}}</td>
   <td>{{m["name"]}}</td>
   <td><a href="/Drink/{{m["id"]}}" >Drink</a></td>
   <td><a href="/charge/{{m["id"]}}" >Charge</a></td>
   <td>{{m["money"]}}</td>
   <td>{{m["lucky"]}}</td>
   

   <!-- <td><a href="/del/{{m["id"]}}">delete</a></td>  delete member -->
 </tr>
 %end
%end
</table>