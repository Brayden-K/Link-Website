document.getElementsByTagName('html')[0].setAttribute('data-theme', getCookie('colorScheme'));

function colorScheme() {
  let currentScheme = getCookie('colorScheme');
  if (currentScheme == 'dark') {
    document.cookie = "colorScheme=light";
    document.querySelector('[data-theme]').setAttribute('data-theme', 'light');
    console.log('Changed from dark to light.');
  } else if (currentScheme == 'light') {
    document.cookie = "colorScheme=dark";
    console.log('Changed from light to dark.');
    document.querySelector('[data-theme]').setAttribute('data-theme', 'dark');
  } else {
    document.cookie = "colorScheme=dark";
    console.log('Default color scheme set to dark.')
    document.querySelector('[data-theme]').setAttribute('data-theme', 'dark');
  }
}

function getCookie(name) {
    // Split cookie string and get all individual name=value pairs in an array
    var cookieArr = document.cookie.split(";");
    
    // Loop through the array elements
    for(var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");
        
        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if(name == cookiePair[0].trim()) {
            // Decode the cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }
    
    // Return null if not found
    return null;
}