#import json
import simplejson
#import json as simplejson

content = '''
<!DOCTYPE html>
<!--[if lt IE 7]>      <html lang="en" class="no-js lt-ie9 lt-ie8 lt-ie7 not-logged-in "> <![endif]-->
<!--[if IE 7]>         <html lang="en" class="no-js lt-ie9 lt-ie8 not-logged-in "> <![endif]-->
<!--[if IE 8]>         <html lang="en" class="no-js lt-ie9 not-logged-in "> <![endif]-->
<!--[if gt IE 8]><!--> <html lang="en" class="no-js not-logged-in "> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

        <title>Page Not Found &bull; Instagram</title>

        <script type="text/javascript">
  WebFontConfig = {
    custom: {
      families: ['proxima-nova:n4,n7'],
      urls: ['//d36xtkk24g8jdx.cloudfront.net/bluebar/2dc26eb/cache/fonts.css']
    }
  };
</script>
<script src="//d36xtkk24g8jdx.cloudfront.net/bluebar/2dc26eb/scripts/webfont.js" type="text/javascript" async></script>

        
    
        <meta name="robots" content="noimageindex">
        
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">


        
    <meta id="viewport" name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, minimum-scale=1, maximum-scale=1">


        <script type="text/javascript">
        (function() {
            var docElement = document.documentElement;
            var classRE = new RegExp('(^|\\s)no-js(\\s|$)');
            var className = docElement.className;
            docElement.className = className.replace(classRE, '$1js$2');
        })();
        </script>

        
    
        <script type="text/javascript">
            GATEKEEPERS = {
                banzai_logs: true
            };
        </script>
        
    
        <link rel="Shortcut Icon" type="image/x-icon" href="//d36xtkk24g8jdx.cloudfront.net/bluebar/2dc26eb/images/ico/favicon.ico">
    
    
        <link rel="apple-touch-icon-precomposed" href="//d36xtkk24g8jdx.cloudfront.net/bluebar/2dc26eb/images/ico/apple-touch-icon-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="//d36xtkk24g8jdx.cloudfront.net/bluebar/2dc26eb/images/ico/apple-touch-icon-72x72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="//d36xtkk24g8jdx.cloudfront.net/bluebar/2dc26eb/images/ico/apple-touch-icon-114x114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="//d36xtkk24g8jdx.cloudfront.net/bluebar/2dc26eb/images/ico/apple-touch-icon-144x144-precomposed.png">
    
    
    <link href="//d36xtkk24g8jdx.cloudfront.net/bluebar/2dc26eb/cache/distillery/dialog-main.css" type="text/css" rel="stylesheet"></link>

    

    </head>
    <body class=" p-error dialog-404">
        
    
        <div class="root">
        
            <div class="page">
                
                    
                        <header class="top-bar top-bar-new">
    <div class="top-bar-wrapper">
        <h1 class="logo"><a href="/">Instagram</a></h1>

        <div class="top-bar-left">
            <ul class="top-bar-actions">
                <li>
                    <a class="top-bar-home" href="/" label=Home><i></i></a>
                </li>
            </ul>
        </div>

        <div class="top-bar-right account-state" id="top_bar_right">
            <ul class="top-bar-actions">
                
                
                <li id="link_profile" class="link-signin">
                    <a href="/accounts/login/" class="loginLink">
                        <i></i>
                        <strong>Log in</strong>
                    </a>
                </li>
                
            </ul>
        </div>
    </div>
</header> <!-- .top-bar -->
                    
                

                
                <div class="main">
                    
	<div class="error-container">
	

	<h2>Page Not Found</h2>

	<p>
        This page could not be found.
        <br />
        You might have followed an incorrect link.
    </p>


	</div>

                </div> <!-- .main -->
                

            </div> <!-- .page -->

            
            <footer class="page-footer" role="contentinfo">
                <div class="wrapper">
                    <nav>
                        <ul>
                            <li><a href="/about/us/">About us</a></li>
                            <li><a href="http://help.instagram.com/">Support</a></li>
                            <li><a href="http://blog.instagram.com/">Blog</a></li>
                            <li><a href="http://instagram.com/press/">Press</a></li>
                            <li><a href="/developer/">API</a></li>
                            <li><a href="/about/jobs/">Jobs</a></li>
                            <li><a href="/about/legal/privacy/">Privacy</a></li>
                            <li><a href="/about/legal/terms/">Terms</a></li>
                        </ul>
                    </nav>

                    <p class="copyright">&copy; 2014 Instagram</p>
                </div>
            </footer>
            
        
        <div id="reactModalMountPoint"></div>
    </div> <!-- .root -->
    
    

        
    <script type="text/javascript">
window._strings = {

"%(count)s comments": "%(count)s comments",
"%(count)s followers": "%(count)s followers",
"%(count)s following": "%(count)s following",
"%(count)s likes": "%(count)s likes",
"%(count)s more comments": "%(count)s more comments",
"%(count)s new posts": "%(count)s new posts",
"%(count)s people liked this photo": "%(count)s people liked this photo",
"%(count)s photos,": "%(count)s photos,",
"%(count)s posts": "%(count)s posts",
"%(count)s+ new posts": "%(count)s+ new posts",
"%(day)s %(month_name)s %(year)s": "%(day)s %(month_name)s %(year)s",
"%(days)s days ago": "%(days)s days ago",
"%(days)sd": "%(days)sd",
"%(followerCount)s followers": "%(followerCount)s followers",
"%(hours)s hours ago": "%(hours)s hours ago",
"%(hours)sh": "%(hours)sh",
"%(likes)s likes, %(comments)s comments": "%(likes)s likes, %(comments)s comments",
"%(mediaCount)s photos": "%(mediaCount)s photos",
"%(minutes)s minutes ago": "%(minutes)s minutes ago",
"%(minutes)sm": "%(minutes)sm",
"%(months)s months ago": "%(months)s months ago",
"%(seconds)s seconds ago": "%(seconds)s seconds ago",
"%(seconds)ss": "%(seconds)ss",
"%(user)s on Instagram": "%(user)s on Instagram",
"%(username)s on Instagram": "%(username)s on Instagram",
"%(weeks)s weeks ago": "%(weeks)s weeks ago",
"%(weeks)sw": "%(weeks)sw",
"%(year)s %(month)s": "%(year)s %(month)s",
"1": "1",
"1 comment": "1 comment",
"1 day ago": "1 day ago",
"1 follower": "1 follower",
"1 hour ago": "1 hour ago",
"1 like": "1 like",
"1 minute ago": "1 minute ago",
"1 month ago": "1 month ago",
"1 more comment": "1 more comment",
"1 new post": "1 new post",
"1 photo>": "1 photo\u003E",
"1 second ago": "1 second ago",
"1 week ago": "1 week ago",
"2": "2",
"3": "3",
"AM": "AM",
"About us": "About us",
"Account Insights - Instagram": "Account Insights \u002D Instagram",
"Add a caption...": "Add a caption...",
"Add a comment": "Add a comment",
"All items loaded": "All items loaded",
"Apr": "Apr",
"April": "April",
"Are you sure you want to delete this comment?": "Are you sure you want to delete this comment?",
"Are you sure?": "Are you sure?",
"Audience": "Audience",
"Aug": "Aug",
"August": "August",
"Badges": "Badges",
"Blog": "Blog",
"By using this embed, you agree to Instagram\\'s <a href=\"http://instagram.com/about/legal/terms/api/\">API Terms of Use</a>.": "By using this embed, you agree to Instagram\u005C\u0027s \u003Ca href\u003D\u0022http://instagram.com/about/legal/terms/api/\u0022\u003EAPI Terms of Use\u003C/a\u003E.",
"Cancel": "Cancel",
"Content unavailable": "Content unavailable",
"Copy Embed Code": "Copy Embed Code",
"Copy this code:": "Copy this code:",
"Couldn\\'t post comment": "Couldn\u005C\u0027t post comment",
"Dec": "Dec",
"December": "December",
"Delete": "Delete",
"Edit Profile": "Edit Profile",
"Embed": "Embed",
"Feb": "Feb",
"February": "February",
"Follow": "Follow",
"Follow %(username)s on Instagram": "Follow %(username)s on Instagram",
"Follow friends and interesting people to see their photos here.": "Follow friends and interesting people to see their photos here.",
"Following": "Following",
"Forgot your password?": "Forgot your password?",
"Fri": "Fri",
"Friday": "Friday",
"Here are some suggestions.": "Here are some suggestions.",
"Home": "Home",
"Jan": "Jan",
"January": "January",
"Jobs": "Jobs",
"Jul": "Jul",
"July": "July",
"Jun": "Jun",
"June": "June",
"Leave a comment...": "Leave a comment...",
"Like": "Like",
"Likes": "Likes",
"Load More...": "Load More...",
"Load more": "Load more",
"Load more...": "Load more...",
"Loading more...": "Loading more...",
"Loading...": "Loading...",
"Log Out": "Log Out",
"Log in": "Log in",
"Mar": "Mar",
"March": "March",
"May": "May",
"Mon": "Mon",
"Monday": "Monday",
"More": "More",
"Next photo": "Next photo",
"No Recent Photos": "No Recent Photos",
"No likes yet.": "No likes yet.",
"No photos to show.": "No photos to show.",
"Nov": "Nov",
"November": "November",
"Now": "Now",
"Oct": "Oct",
"October": "October",
"Open in App": "Open in App",
"Others": "Others",
"PM": "PM",
"Password:": "Password:",
"Paste it on your website, blog, or wherever you want to link to your profile!": "Paste it on your website, blog, or wherever you want to link to your profile!",
"People you follow": "People you follow",
"Performance": "Performance",
"Photo by %(username)s": "Photo by %(username)s",
"Posts": "Posts",
"Press": "Press",
"Press Page - Instagram": "Press Page \u002D Instagram",
"Previous Posts": "Previous Posts",
"Previous photo": "Previous photo",
"Privacy": "Privacy",
"Report inappropriate": "Report inappropriate",
"Requested": "Requested",
"Retry": "Retry",
"Sat": "Sat",
"Saturday": "Saturday",
"Select your badge:": "Select your badge:",
"Sep": "Sep",
"September": "September",
"Summary": "Summary",
"Sun": "Sun",
"Sunday": "Sunday",
"Support": "Support",
"Terms": "Terms",
"This user is private": "This user is private",
"Thu": "Thu",
"Thursday": "Thursday",
"To follow %(username)s, you need to log in.": "To follow %(username)s, you need to log in.",
"Toggle like": "Toggle like",
"Tue": "Tue",
"Tuesday": "Tuesday",
"Username:": "Username:",
"Video by %(username)s": "Video by %(username)s",
"View Photo Page": "View Photo Page",
"View Profile": "View Profile",
"View Video Page": "View Video Page",
"View on Instagram": "View on Instagram",
"Wed": "Wed",
"Wednesday": "Wednesday",
"When you are finished following people,": "When you are finished following people,",
"Write a comment...": "Write a comment...",
"Yes": "Yes",
"You must log in to add a comment.": "You must log in to add a comment.",
"You must log in to like this photo.": "You must log in to like this photo.",
"You need to be following %(username)s to like or comment": "You need to be following %(username)s to like or comment",
"Your username or password was incorrect.": "Your username or password was incorrect.",
"am": "am",
"banner photo": "banner photo",
"nd": "nd",
"pm": "pm",
"rd": "rd",
"reload this page": "reload this page",
"st": "st",
"th": "th"
};
</script>
    <script src=//d36xtkk24g8jdx.cloudfront.net/bluebar/2dc26eb/scripts/polyfills/es5-shim.min.js></script>
<script src=//d36xtkk24g8jdx.cloudfront.net/bluebar/2dc26eb/scripts/polyfills/es5-sham.min.js></script>
<script type="text/javascript">window._sharedData = {"static_root":"\/\/d36xtkk24g8jdx.cloudfront.net\/bluebar\/2dc26eb","platform":{"is_touch":false,"app_platform":"web"},"hostname":"api.instagram.com","entry_data":{},"country_code":"VE","config":{"viewer":null,"csrf_token":"NOTPROVIDED"}};</script>
<script src="//d36xtkk24g8jdx.cloudfront.net/bluebar/2dc26eb/cache/bundles/webpack-common.js"></script>
    
    <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-18105282-1']);
        _gaq.push(['_setDomainName', 'instagram.com']);
        _gaq.push(['_setAllowLinker', true]);
        
        _gaq.push(['_trackPageview']);
        (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();
    </script>
    

    </body>
</html>
'''

simplejson.loads(content)

