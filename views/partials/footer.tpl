
<footer >
  <div class="footer region">© 2020 <a href="https://www.khmerweb.app/">Khmer Web</a></div>
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