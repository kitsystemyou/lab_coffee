<head>
  <title>Tokunaga Lab Coffee</title>
  <style>

  </style>
  <link rel="stylesheet" href="/files/h1.css">
  <!-- <link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/dark.css'> -->
</head>

<h1 align="center" class="cp_h1title">Deposit manager</h1>

<body>
<!-- <a href="/add" > new </a>  -->
  <table border="1" align="center" style="table-layout: fixed" width="60%">
    %for i,m in enumerate(item_list):
      %if i==0:
      <tr>

        <td>{{m["name"]}}</td>
        <td>飲む</td>
        <td>入金</td>
        <td>{{m["money"]}}</td>
        <td>{{m["lucky"]}}</td>

      </tr>
      %else:
      <tr>

        <td>{{m["name"]}}</td>
        <td><a href="/drink/{{m["id"]}}" >Drink</a></td>
        <td><a href="/charge/{{m["id"]}}" >Charge</a></td>
        <td>{{m["money"]}}</td>
        <td>{{m["lucky"]}}</td>
        

        <!-- <td><a href="/del/{{m["id"]}}">delete</a></td>  delete member -->
      </tr>
      %end
    %end
  </table>

</body>
