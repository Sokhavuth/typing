
<footer >
  <div class="footer region">Khmer Web Typing © 2020 </div>
</footer>
<script>
$(".keyboard-base .key").on({
    keypress: function(event){
      var key = String.fromCharCode(event.which);
      if(event.which == 32)
        event.preventDefault();
      
      typing.checkKey(key)
    }
    
});
</script>
</div><!--sites-->
</body>
</html>