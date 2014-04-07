$('.article').readmore({
	maxHeight: 200,
	heightMargin: 16,
	moreLink: '<a class="read-more" href="#">Read More</a>',
	lessLink: '<a class="read-more" href="#">Close</a>',
	afterToggle: function(trigger, element, expanded) {
    	if(! expanded) { // The "Close" link was clicked
      		$('html, body').animate( { scrollTop: element.offset().top }, {duration: 100 } );
    	}
  	}
});