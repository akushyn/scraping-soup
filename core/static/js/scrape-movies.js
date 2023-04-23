$(document).ready(function() {
  // Handle the button click event
  $('#scrape_movies_btn').click(function() {
    // Make an AJAX request to retrieve the data
    $.ajax({
      url: '/scrape-movies/',
      type: 'GET',
      success: function(data) {
        alert('Scraped successfully.');
      },
      error: function() {
        alert('An error occurred while scraping the data.');
      }
    });
  });
});
