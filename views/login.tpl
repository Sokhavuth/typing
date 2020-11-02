<!--views/login.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{data['blogTitle']}}</title>
    <script src="/static/scripts/jQuery.js"></script>
    <script src="/static/scripts/login.js"></script>
    <link href="/static/styles/login.css" rel="stylesheet"></link>
    <link href="/static/images/site_logo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
  </head>
  <body>
    <div id="site">
      <form id="login" action='/login/user' method='post'>
        <div id='info'>ទំរង់បែបបទ​ចុះ​ឈ្មោះ</div>
        <dv class='message'>{{data['message']}}</dv>
        %data['message'] = ''
        <div class="wrapper">
          <a>Email:​</a><input 
          type="text" name="fusername" required />
          <a>ពាក្យ​សំងាត់ៈ</a><input class='password' type='password' name='fpassword' required />
          <a></a><input type='submit' value='បញ្ជូន' />
        </div>
      </form>
    </div><!--sites-->
  </body>
</html>