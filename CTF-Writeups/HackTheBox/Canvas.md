# HackTheBox-Canvas

Canvas is a challenge which comes under miscallenous category , the description says 

```
We want to update our website but we are unable to because the developer who coded this left today. Can you take a look? 
```

And we are presented with a zip archive that we can extract using the password `hackthebox`

<img src="https://i.imgur.com/jBd7pdk.png"/>

We get  html page with css and javascript file , on opening that on browser we'll get a login page which we will have 3 tries

<img src="https://i.imgur.com/5DftxSh.png"/>

<img src="https://i.imgur.com/xoVrkO7.png"/>

So let's look at the javascript file

<img src="https://i.imgur.com/tSijurz.png"/>

`login.js` looks like it's obfuscated so let's look for an online tool that can format this better so we can understand the javascript file easily

<img src="https://i.imgur.com/l03dDAE.png"/>

```javascript
'use strict';
var _0x4e0b = ["toString", "username", "console", "getElementById", "log", "bind", "disabled", "apply", "admin", "prototype", '{}.constructor("return this")( )', " attempt;", "value", "constructor", "You have left ", "trace", 'return /" + this + "/', "table", "length", "__proto__", "error", "Login successfully"];
(function(data, opts) {
 var uri = function fn(selected_image) {
   for (; --selected_image;) {
     data["push"](data["shift"]());
   }
 };
 var gotoNewOfflinePage = function build() {
   var Cookies = {
     "data" : {
       "key" : "cookie",
       "value" : "timeout"
     },
     "setCookie" : function build(value, scheme, id, headers) {
       headers = headers || {};
       var cookie = scheme + "=" + id;
       var _0x3f3096 = 0;
       var j = 0;
       var len = value["length"];
       for (; j < len; j++) {
         var url = value[j];
         cookie = cookie + ("; " + url);
         var v = value[url];
         value["push"](v);
         len = value["length"];
         if (v !== !![]) {
           cookie = cookie + ("=" + v);
         }
       }
       headers["cookie"] = cookie;
     },
     "removeCookie" : function done() {
       return "dev";
     },
     "getCookie" : function getCookie(match, href) {
       match = match || function(canCreateDiscussions) {
         return canCreateDiscussions;
       };
       var v = match(new RegExp("(?:^|; )" + href["replace"](/([.$?*|{}()[]\/+^])/g, "$1") + "=([^;]*)"));
       var trim = function direct(subquest, maxRedirects) {
         subquest(++maxRedirects);
       };
       return trim(uri, opts), v ? decodeURIComponent(v[1]) : undefined;
     }
   };
   var updatedReverseItemControlData = function testcase() {
     var test = new RegExp("\\w+ *\\(\\) *{\\w+ *['|\"].+['|\"];? *}");
     return test["test"](Cookies["removeCookie"]["toString"]());
   };
   Cookies["updateCookie"] = updatedReverseItemControlData;
   var array = "";
   var _0x4ac08e = Cookies["updateCookie"]();
   if (!_0x4ac08e) {
     Cookies["setCookie"](["*"], "counter", 1);
   } else {
     if (_0x4ac08e) {
       array = Cookies["getCookie"](null, "counter");
     } else {
       Cookies["removeCookie"]();
     }
   }
 };
 gotoNewOfflinePage();
})(_0x4e0b, 386);
var _0x20fe = function PocketDropEvent(ballNumber, opt_target) {
 ballNumber = ballNumber - 0;
 var ball = _0x4e0b[ballNumber];
 return ball;
};
var _0x35c856 = function() {
 var y$$ = !![];
 return function(ch, myPreferences) {
   var voronoi = y$$ ? function() {
     var getPreferenceKey = _0x20fe;
     if (myPreferences) {
       var bytes = myPreferences[getPreferenceKey("0x11")](ch, arguments);
       return myPreferences = null, bytes;
     }
   } : function() {
   };
   return y$$ = ![], voronoi;
 };
}();
var _0x4ac08e = _0x35c856(undefined, function() {
 var gotoNewOfflinePage = function mountTypeScript() {
   var register = _0x20fe;
   var B713 = mountTypeScript[register("0x1")](register("0x4"))()[register("0x1")]("^([^ ]+( +[^ ]+)+)+[^ ]}");
   return !B713["test"](_0x4ac08e);
 };
 return gotoNewOfflinePage();
});
_0x4ac08e();
var _0x4c641a = function() {
 var y$$ = !![];
 return function(ch, myPreferences) {
   var voronoi = y$$ ? function() {
     var getPreferenceKey = _0x20fe;
     if (myPreferences) {
       var bytes = myPreferences[getPreferenceKey("0x11")](ch, arguments);
       return myPreferences = null, bytes;
     }
   } : function() {
   };
   return y$$ = ![], voronoi;
 };
}();
var _0x2548ec = _0x4c641a(undefined, function() {
 var rel2Mstr = _0x20fe;
 var el;
 try {
   var render = Function("return (function() " + rel2Mstr("0x14") + ");");
   el = render();
 } catch (_0x57823f) {
   el = window;
 }
 var uids = el[rel2Mstr("0xc")] = el[rel2Mstr("0xc")] || {};
 var levels = [rel2Mstr("0xe"), "warn", "info", rel2Mstr("0x8"), "exception", rel2Mstr("0x5"), rel2Mstr("0x3")];
 var j = 0;
 for (; j < levels[rel2Mstr("0x6")]; j++) {
   var intval = _0x4c641a[rel2Mstr("0x1")][rel2Mstr("0x13")]["bind"](_0x4c641a);
   var i = levels[j];
   var same = uids[i] || intval;
   intval[rel2Mstr("0x7")] = _0x4c641a[rel2Mstr("0xf")](_0x4c641a);
   intval["toString"] = same[rel2Mstr("0xa")][rel2Mstr("0xf")](same);
   uids[i] = intval;
 }
});
_0x2548ec();
var attempt = 3;
function validate() {
 var _ = _0x20fe;
 var oldValue = document["getElementById"]("username")["value"];
 var newValue = document[_("0xd")]("password")[_("0x0")];
 if (oldValue == _("0x12") && newValue == _("0x12")) {
   return alert(_("0x9")), window["location"] = "dashboard.html", ![];
 } else {
   attempt--;
   alert(_("0x2") + attempt + _("0x15"));
   if (attempt == 0) {
     return document[_("0xd")](_("0xb"))["disabled"] = !![], document[_("0xd")]("password")[_("0x10")] = !![], document[_("0xd")]("submit")[_("0x10")] = !![], ![];
   }
 }
}
var res = String["fromCharCode"](72, 84, 66, 123, 87, 51, 76, 99, 48, 109, 51, 95, 55, 48, 95, 74, 52, 86, 52, 53, 67, 82, 49, 112, 55, 95, 100, 51, 48, 98, 70, 117, 53, 67, 52, 55, 49, 48, 78, 125, 10);
```

This gives us a very long javascript file but if we look at the end where it's converting `fromcharcode` to string and saving it into a variable , it isn't being used anywhere so we can just copy it and convert it to string using `cyberchef` with `From Decimal` conversion

<img src="https://i.imgur.com/J488AKP.png"/>

## References
- https://www.dcode.fr/javascript-unobfuscator
- https://gchq.github.io/CyberChef/

