
<footer >
  <div class="footer region">Khmer Web Typing © 2020 </div>
</footer>
<script>
$(".keyboard-base .key").on({
    keypress: function(event){
      if(event.which != 32)
        var key = String.fromCharCode(event.which).toUpperCase();
      else if(event.which == 32){
        event.preventDefault();
        var key = "Space";
      }
      typing.checkKey(key)
    } 
});
</script>
</div><!--sites-->
</body>
</html>