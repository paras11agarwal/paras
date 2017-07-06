'use strict';

//---tested for stackexchange,learnxinyminutes,stackoverflow,learnxinyminutes,materailizecss.com
//getting pre tag from website
Array.from(document.getElementsByTagName('pre')).forEach(function (block) 
{
		//adding an event listener listening for double click
		block.addEventListener('dblclick', function (event)
		{	
			//creating a range objects  
			var range = document.createRange();			
			range.selectNode(block);
			try {
				window.getSelection().addRange(range);
				//to copy the block of code
				document.execCommand('copy');
				window.getSelection().removeAllRanges();
				//applying a border for 
				block.style.outline = '2px solid #F00';
				setTimeout(function () {
				//to remove the outer border after 500ms
			    return block.style.outline = 'none';
				}, 500);

			}			
			catch (error) {
			console.log('Failed to copy your code', error);
		}
	});

});


/*Array.from(document.getElementsByTagName('tbody')).forEach(function (block) 
{
		block.addEventListener('dblclick', function (event) {	
		var range = document.createRange();
		range.selectNode(block);
		try {
			window.getSelection().addRange(range);
			document.execCommand('copy');
			window.getSelection().removeAllRanges();
			block.style.outline = '2px solid #0D0';
			setTimeout(function () {
			  return block.style.outline = 'none';
			}, 500);
		} catch (error) {
			console.log('Failed to copy your code', error);
		}
	});
});
*/

