
/*function storifyThis(info, tab) {
  var element = buildElement(info, tab);
  return storifyThisElement(element);
}

chrome.contextMenus.create({
  'title':    'Click for downloadable links!!',
  'contexts': ['link'],
  'onclick':  downloadable
});
chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.connect(tab.id);
  downloadable(null, tab);
});*/

var x=0;

$("a").on('mouseover',function(e){
	e.preventDefault();
	
	if(x==0){
	var link=$(this).attr('href');
	//var d= document.createElement('div');
	//d.setAttribute('style','position:"absolute";left:"600px";top:600px');
	var popy=document.createElement('iframe');
	popy.setAttribute('src',link);
	popy.setAttribute('class','if');
	popy.setAttribute('height','600px');
	popy.setAttribute('width','600px');
	popy.setAttribute('style','position:absolute');
	$(this).append(popy);
	x=1;
}
	//d.appendChild(popy);


});

$(document).click(function (event) {            
    $('.if').hide();
    x=0;
});
