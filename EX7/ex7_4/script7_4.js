$(document).ready(function() {
	$('h1').click(function() {
	  $(this).toggleClass('blink');
	});
  
	$('#colorSelector').change(function() {
	  var color = $(this).val();
	  $('body').css('background-color', color);
	});
  
	$('.accordion-header').click(function() {
	  $(this).toggleClass('active');
	  var content = $(this).next('.accordion-content');
	  if (content.css('max-height')) {
		content.css('max-height', null);
	  } else {
		content.css('max-height', content.prop('scrollHeight') + 'px');
	  }
	});
  });

  

















  