<h1>How much charge?</h1>
%id = id
{{id}}
<form action="/update" method="POST">
  <!-- <input type="text" name="item_name" placeholder="name"/> -->
  <input type="hidden" name="id" value="{{id}}" />
  <input type="hidden" name="type" value="deposit" />
  <button type="submit" name="money" value="50" >deposit 50</button><br>
  <button type="submit" name="money" value="100" >deposit 100</button><br>
  <button type="submit" name="money" value="200" >deposit 200</button><br>
  <button type="submit" name="money" value="500" >deposit 500</button>
</form>