<h1>Which Drink?</h1>
%id = id
{{id}}
<form action="/update" method="POST">
  <!-- <input type="text" name="item_name" placeholder="name"/> -->
  <input type="hidden" name="id" value="{{id}}" />
  <input type="hidden" name="type" value="drink" />
  <button type="submit" name="money" value="-20" >Drink Black</button><br>
  <button type="submit" name="money" value="-25" >Drink with Milk</button><br>
  <button type="submit" name="money" value="-40" >Drink Latte</button>
</form>